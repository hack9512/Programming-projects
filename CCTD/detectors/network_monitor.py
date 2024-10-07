from scapy.all import sniff
from scapy.layers.l2 import ARP  # Import ARP class to handle ARP packets

# Function to monitor the network
def detect_network_intrusions():
    print("Starting network intrusion detection...")

    # Start sniffing packets
    sniff(prn=process_packet, store=False)

# Function to process each captured packet
def process_packet(packet):
    # Check if the packet has an ARP layer
    if ARP in packet:
        if packet[ARP].op == 1:  # ARP request
            print(f"ARP Request: {packet[ARP].psrc} is asking about {packet[ARP].pdst}")
        elif packet[ARP].op == 2:  # ARP response
            print(f"ARP Response: {packet[ARP].hwsrc} has address {packet[ARP].psrc}")

if __name__ == "__main__":
    detect_network_intrusions()
