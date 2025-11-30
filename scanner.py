import scapy.all as scapy
from mac_vendor_lookup import MacLookup
import socket

class NetworkScanner:
    def __init__(self):
        self.mac_lookup = MacLookup()
        # Initialize the vendor DB (downloads/updates it)
        try:
            self.mac_lookup.update_vendors()
        except:
            print("Could not update vendor DB, using cached version.")

    def get_local_ip(self):
        # Helper to get local IP to guess subnet
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Doesn't need to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def get_active_subnets(self):
        """
        Returns a list of tuples (ip, subnet_cidr) for all active interfaces.
        """
        subnets = []
        try:
            # scapy.get_if_list() returns interface names/GUIDs
            for iface in scapy.get_if_list():
                try:
                    ip = scapy.get_if_addr(iface)
                    if ip and ip != "0.0.0.0" and ip != "127.0.0.1" and not ip.startswith("169.254"):
                        # Assume /24 for simplicity
                        subnet = ".".join(ip.split('.')[:3]) + ".1/24"
                        subnets.append((ip, subnet))
                except:
                    continue
        except Exception as e:
            print(f"Error listing interfaces: {e}")
            # Fallback to socket method if scapy fails
            local_ip = self.get_local_ip()
            subnet = ".".join(local_ip.split('.')[:3]) + ".1/24"
            subnets.append((local_ip, subnet))
            
        # Remove duplicates
        return list(set(subnets))

    def scan(self, ip_range=None):
        ranges_to_scan = []
        
        if ip_range:
            ranges_to_scan.append(ip_range)
        else:
            # Auto-detect all subnets
            active = self.get_active_subnets()
            for ip, subnet in active:
                print(f"Detected Interface: {ip} -> Subnet: {subnet}")
                ranges_to_scan.append(subnet)

        all_clients = []
        
        for subnet in ranges_to_scan:
            print(f"Scanning {subnet}...")
            
            try:
                # Create ARP Request
                arp_request = scapy.ARP(pdst=subnet)
                broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
                arp_request_broadcast = broadcast/arp_request
                
                # Send & Receive
                # timeout=2 to be a bit more patient
                answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
                
                for element in answered_list:
                    ip = element[1].psrc
                    mac = element[1].hwsrc
                    
                    # Lookup Vendor
                    try:
                        vendor = self.mac_lookup.lookup(mac)
                    except:
                        vendor = "Unknown"
                        
                    client_dict = {
                        "ip": ip, 
                        "mac": mac, 
                        "vendor": vendor,
                        "is_suspicious": vendor == "Unknown"
                    }
                    
                    # Avoid duplicates if scanning overlapping ranges
                    if not any(c['ip'] == ip for c in all_clients):
                        all_clients.append(client_dict)
                        
            except Exception as e:
                print(f"Error scanning {subnet}: {e}")
            
        return all_clients

if __name__ == "__main__":
    scanner = NetworkScanner()
    results = scanner.scan()
    for client in results:
        print(client)
