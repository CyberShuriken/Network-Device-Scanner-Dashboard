# 📡 Network Device Scanner + Dashboard

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Scapy](https://img.shields.io/badge/Scapy-2.4%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A network reconnaissance tool that scans your local network (LAN) to discover connected devices, identifies their manufacturers via MAC address lookup, and visualizes the results on a modern web dashboard.

## 🧐 The Problem

Understanding who and what is connected to your network is the first step in securing it. Unauthorized devices (rogue IoT gadgets, neighbors stealing WiFi) can be security risks. Command-line tools like `nmap` are powerful but can be intimidating for non-technical users.

## 💡 The Solution

This tool combines the power of **Scapy** (for packet crafting and ARP scanning) with a user-friendly **Flask** dashboard.

It automatically:
1.  **Scans** the local subnet using ARP requests.
2.  **Resolves** MAC addresses to manufacturers (e.g., "Apple", "Espressif", "Nest").
3.  **Flags** unknown or suspicious devices for review.

## 🚀 Features

- **One-Click Scan**: Simple web interface to trigger scans.
- **Device Identification**: Automatically looks up MAC OUI vendors.
- **Visual Dashboard**: Clean, responsive UI with color-coded status.
- **Suspicious Device Flagging**: Highlights devices with unknown vendors.

## 🛠️ Installation

### Prerequisites
- **Python 3.8+**
- **Npcap** (Required for Windows): Download and install from [npcap.com](https://npcap.com/). Ensure "Install Npcap in WinPcap API-compatible Mode" is checked.

### Steps

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/CyberShuriken/Network-Device-Scanner-Dashboard.git
    cd Network-Device-Scanner-Dashboard
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

**Important:** This tool requires Administrator/Root privileges to send raw packets.

1.  **Run the application (as Admin)**:
    - **Windows**: Open Command Prompt/PowerShell as Administrator.
    - **Linux/Mac**: Use `sudo python app.py`.

    ```bash
    python app.py
    ```

2.  **Access the Dashboard**:
    Open your browser and go to `http://localhost:5000`.

3.  **Scan**:
    Click the **"Scan Network"** button and wait for the results!

## 🧠 Skills Demonstrated

- **Network Fundamentals**: Understanding ARP (Address Resolution Protocol) and subnets.
- **Packet Crafting**: Using Scapy to build and send custom network frames.
- **Full-Stack Python**: Integrating a backend scanner with a frontend web UI.
- **API Integration**: Using MAC vendor databases to enrich raw network data.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

