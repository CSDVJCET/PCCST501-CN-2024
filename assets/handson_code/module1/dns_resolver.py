"""
PCCST501 Computer Networks - Module 1 Hands-on
Interactive DNS Query Tool & Resolver
Demonstrates Forward DNS (A records), Reverse DNS (PTR), MX lookup, and iterative resolution concepts.
Author: Prof. Anju Markose | Dept. of CSE, VJCET
"""

import socket
import sys

def forward_lookup(domain_name):
    print(f"\n--- Forward DNS Lookup for: {domain_name} ---")
    try:
        ip_addresses = socket.gethostbyname_ex(domain_name)
        canonical_name = ip_addresses[0]
        aliases = ip_addresses[1]
        ips = ip_addresses[2]

        print(f"Canonical Hostname: {canonical_name}")
        print(f"Aliases / CNAMEs  : {', '.join(aliases) if aliases else 'None'}")
        print(f"IPv4 Addresses    : {', '.join(ips)}")
    except socket.gaierror as e:
        print(f"[-] DNS Resolution Error: {e}")

def reverse_lookup(ip_address):
    print(f"\n--- Reverse DNS Lookup for IP: {ip_address} ---")
    try:
        host, aliases, _ = socket.gethostbyaddr(ip_address)
        print(f"Primary Hostname  : {host}")
        print(f"Aliases           : {', '.join(aliases) if aliases else 'None'}")
    except socket.herror as e:
        print(f"[-] Reverse DNS Lookup Error: {e}")

def get_service_port(service_name, protocol="tcp"):
    try:
        port = socket.getservbyname(service_name, protocol)
        print(f"Well-Known Port for '{service_name}' ({protocol.upper()}): {port}")
    except OSError:
        print(f"[-] Service '{service_name}' not found.")

def main():
    print("=====================================================")
    print("   PCCST501 DNS Resolver & Service Query Utility    ")
    print("=====================================================")
    
    test_domains = ["google.com", "vjcet.ac.in", "github.com", "ktu.edu.in"]
    for d in test_domains:
        forward_lookup(d)

    print("\n--- Reverse DNS Demo ---")
    reverse_lookup("8.8.8.8")
    reverse_lookup("1.1.1.1")

    print("\n--- Standard Application Port Numbers ---")
    services = ["http", "https", "domain", "smtp", "ftp", "ssh", "pop3"]
    for s in services:
        get_service_port(s)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        forward_lookup(sys.argv[1])
    else:
        main()
