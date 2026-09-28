/*
 * PCCST501 Computer Networks - Module 3 Hands-on
 * Datalink Provider Interface & Linux PF_PACKET Raw Socket Sniffer
 * References: W. Richard Stevens, UNIX Network Programming Vol 1 (Chapter 29)
 * Intercepts and decodes raw IEEE 802.3 Ethernet frames directly from the NIC.
 * Author: Prof. Anju Markose | Dept. of CSE, VJCET
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <net/ethernet.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <netinet/udp.h>
#include <arpa/inet.h>
#include <linux/if_packet.h>
#include <net/if.h>

#define BUFFER_SIZE 65536

void print_ethernet_header(unsigned char* buffer) {
    struct ethhdr *eth = (struct ethhdr *)buffer;
    printf("\n==================== ETHERNET FRAME ====================\n");
    printf("Destination MAC : %.2X-%.2X-%.2X-%.2X-%.2X-%.2X\n",
           eth->h_dest[0], eth->h_dest[1], eth->h_dest[2],
           eth->h_dest[3], eth->h_dest[4], eth->h_dest[5]);
    printf("Source MAC      : %.2X-%.2X-%.2X-%.2X-%.2X-%.2X\n",
           eth->h_source[0], eth->h_source[1], eth->h_source[2],
           eth->h_source[3], eth->h_source[4], eth->h_source[5]);
    printf("EtherType       : 0x%04x (", ntohs(eth->h_proto));
    
    if (ntohs(eth->h_proto) == ETH_P_IP) printf("IPv4");
    else if (ntohs(eth->h_proto) == ETH_P_ARP) printf("ARP");
    else if (ntohs(eth->h_proto) == ETH_P_IPV6) printf("IPv6");
    else printf("Other");
    printf(")\n");
}

void print_ip_packet(unsigned char* buffer, int size) {
    struct ethhdr *eth = (struct ethhdr *)buffer;
    if (ntohs(eth->h_proto) != ETH_P_IP) return;

    struct iphdr *iph = (struct iphdr *)(buffer + sizeof(struct ethhdr));
    struct sockaddr_in source, dest;
    memset(&source, 0, sizeof(source));
    source.sin_addr.s_addr = iph->saddr;
    memset(&dest, 0, sizeof(dest));
    dest.sin_addr.s_addr = iph->daddr;

    printf("--- IPv4 Header ---\n");
    printf("IP Version      : %d\n", (unsigned int)iph->version);
    printf("Header Length   : %d Bytes\n", ((unsigned int)(iph->ihl)) * 4);
    printf("TTL             : %d\n", (unsigned int)iph->ttl);
    printf("Protocol        : %d (", (unsigned int)iph->protocol);
    if (iph->protocol == 6) printf("TCP");
    else if (iph->protocol == 17) printf("UDP");
    else if (iph->protocol == 1) printf("ICMP");
    else printf("Other");
    printf(")\n");
    printf("Source IP       : %s\n", inet_ntoa(source.sin_addr));
    printf("Destination IP  : %s\n", inet_ntoa(dest.sin_addr));
}

int main() {
    int raw_sock;
    unsigned char buffer[BUFFER_SIZE];
    struct sockaddr saddr;
    socklen_t saddr_len = sizeof(saddr);

    // 1. Create Raw Socket for PF_PACKET (requires root / sudo privileges)
    // htons(ETH_P_ALL) captures all Ethernet protocols
    raw_sock = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    if (raw_sock < 0) {
        perror("[-] Socket Error (Make sure to run with root/sudo)");
        return 1;
    }
    printf("[+] PF_PACKET Raw Socket Initialized successfully.\n");
    printf("[*] Sniffing live packets on all network interfaces... (Ctrl+C to stop)\n");

    int packet_count = 0;
    while (packet_count < 10) {
        int data_size = recvfrom(raw_sock, buffer, BUFFER_SIZE, 0, &saddr, &saddr_len);
        if (data_size < 0) {
            perror("[-] Recvfrom error");
            return 1;
        }
        packet_count++;
        printf("\n[#%d] Captured Packet (%d bytes)", packet_count, data_size);
        print_ethernet_header(buffer);
        print_ip_packet(buffer, data_size);
    }

    close(raw_sock);
    return 0;
}
