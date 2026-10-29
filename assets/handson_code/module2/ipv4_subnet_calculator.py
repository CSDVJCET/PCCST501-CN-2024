"""
PCCST501 Computer Networks - Module 2 Hands-on
IPv4 Subnetting & CIDR Address Calculator
Demonstrates Network Address, Broadcast Address, Subnet Mask, Usable Host Range, and Total Usable Hosts.
Author: Prof. Anju Markose | Dept. of CSE, VJCET
"""

import ipaddress
import sys

def calculate_subnet_details(cidr_string):
    try:
        net = ipaddress.IPv4Network(cidr_string, strict=False)
        print(f"\n=======================================================")
        print(f"       IPv4 Subnet Analysis for: {cidr_string}        ")
        print(f"=======================================================")
        print(f"CIDR Prefix Length      : /{net.prefixlen}")
        print(f"Subnet Mask (Dotted Dec): {net.netmask}")
        print(f"Wildcard Mask           : {net.hostmask}")
        print(f"Network Address         : {net.network_address}")
        print(f"Broadcast Address       : {net.broadcast_address}")
        
        # Usable Host Range
        hosts = list(net.hosts())
        if hosts:
            first_host = hosts[0]
            last_host = hosts[-1]
            total_usable = len(hosts)
            print(f"First Usable Host IP    : {first_host}")
            print(f"Last Usable Host IP     : {last_host}")
            print(f"Total Usable Hosts      : {total_usable:,} addresses")
        else:
            print(f"First Usable Host IP    : N/A (Point-to-Point /31 or Host /32)")
            print(f"Last Usable Host IP     : N/A")
            print(f"Total Usable Hosts      : 0")

        # Binary Representation
        net_bin = '.'.join([f"{int(o):08b}" for o in str(net.network_address).split('.')])
        mask_bin = '.'.join([f"{int(o):08b}" for o in str(net.netmask).split('.')])
        print(f"\nBinary Network Address  : {net_bin}")
        print(f"Binary Subnet Mask      : {mask_bin}")

        # Standard Class Breakdown
        first_octet = int(str(net.network_address).split('.')[0])
        if 1 <= first_octet <= 126:
            ip_class = "Class A (Default /8)"
        elif 128 <= first_octet <= 191:
            ip_class = "Class B (Default /16)"
        elif 192 <= first_octet <= 223:
            ip_class = "Class C (Default /24)"
        elif 224 <= first_octet <= 239:
            ip_class = "Class D (Multicast 224.0.0.0/4)"
        else:
            ip_class = "Class E (Experimental)"
        print(f"Traditional IPv4 Class  : {ip_class}")
        print(f"Is Private Network (RFC): {'Yes' if net.is_private else 'No (Public Internet)'}")
        print("=======================================================\n")
        
    except ValueError as e:
        print(f"[-] Invalid CIDR / IP input '{cidr_string}': {e}")

def main():
    examples = [
        "192.168.10.45/24",
        "172.16.50.100/20",
        "10.0.0.1/18",
        "192.168.1.130/26"
    ]
    if len(sys.argv) > 1:
        calculate_subnet_details(sys.argv[1])
    else:
        for ex in examples:
            calculate_subnet_details(ex)

if __name__ == "__main__":
    main()
