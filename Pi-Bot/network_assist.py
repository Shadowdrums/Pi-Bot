import os
import psutil
from scapy.all import sniff, ARP
import socket
import netifaces as ni
import subprocess
import speedtest

known_devices = set()
DATA_THRESHOLD = 1000000  # 1 MB

def get_subnet():
    ip_address = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
    subnet = '.'.join(ip_address.split('.')[:-1]) + '.0/24'
    return subnet

def map_network_topology():
    subnet = get_subnet()
    cmd = f"nmap -sn {subnet}"
    result = os.popen(cmd).read()
    return result

def packet_callback(packet):
    print(packet.show())

def start_packet_sniffing(interface='eth0', count=10):
    sniff(iface=interface, count=count, prn=packet_callback)

def scan_wifi():
    cmd = "sudo iwlist wlan0 scan | grep 'ESSID'"
    networks = os.popen(cmd).read()
    return networks

def check_ssh_status():
    try:
        result = subprocess.check_output("systemctl is-active ssh", shell=True).decode().strip()
        return f"SSH Service is {result}."
    except:
        return "Unable to check SSH service status."

def perform_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    return f"Download Speed: {download_speed:.2f} Mbps, Upload Speed: {upload_speed:.2f} Mbps"

def new_device_alert(pkt):
    if ARP in pkt and pkt[ARP].op in (1, 2):
        if pkt[ARP].psrc not in known_devices:
            known_devices.add(pkt[ARP].psrc)
            print(f"\n[ALERT] New device detected: {pkt[ARP].psrc}\n")

def data_transfer_alert():
    old_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        if new_value - old_value > DATA_THRESHOLD:
            print(f"\n[ALERT] High data usage detected! Transfer of {(new_value - old_value) / (1024 * 1024):.2f} MB in a short time.\n")
        old_value = new_value

def main():
    for line in map_network_topology().splitlines():
        ip = line.split()[1]
        known_devices.add(ip)

    print("Starting Network Monitoring...")
    sniff(prn=new_device_alert, filter="arp", store=0, count=0)  # Continuous sniffing for new devices

    while True:
        print("\n--- Network Monitoring ---")
        print("1. Network Topology Mapping")
        print("2. Packet Sniffing")
        print("3. Wi-Fi Scanning")
        print("4. Check SSH Service Status")
        print("5. Perform Internet Speed Test")
        print("6. Display current network I/O")
        print("7. Display active network connections")
        print("8. Display network interface details")
        print("9. Exit")
            
        choice = input("\nChoose an option: ")
        if choice == '1':
            print(map_network_topology())
        elif choice == '2':
            start_packet_sniffing()
        elif choice == '3':
            print(scan_wifi())
        elif choice == '4':
            print(check_ssh_status())
        elif choice == '5':
            print(perform_speed_test())
        elif choice == '6':
            print(psutil.net_io_counters())
        elif choice == '7':
            print(psutil.net_connections())
        elif choice == '8':
            print(psutil.net_if_addrs())
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
