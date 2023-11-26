from scapy.all import sniff, IP
import socket

ipFilter = input("Nhap ip:")

def resolve_ip(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Không thể phân giải"

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if ip_src != ipFilter:
            return
        domain = resolve_ip(ip_dst)
        print(f"IP: {ip_dst} - Domain PTR: {domain}")

print("Bắt đầu bắt gói tin trên wlan0...")
sniff(iface="wlan0", prn=packet_callback, filter="ip", store=0)

