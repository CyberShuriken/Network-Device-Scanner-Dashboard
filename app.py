from flask import Flask, render_template, jsonify
from scanner import NetworkScanner
import threading

app = Flask(__name__)
scanner = NetworkScanner()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/scan')
def scan_network():
    # In a real app, this might be async or a background job
    # For this portfolio demo, we'll wait for the scan (1-2 seconds)
    results = scanner.scan()
    return jsonify(results)

if __name__ == '__main__':
    print("Starting Network Scanner Dashboard...")
    print("Note: Ensure you are running as Administrator/Root for ARP scanning to work.")
    app.run(debug=True, port=5000)
