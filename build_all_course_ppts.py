"""
build_all_course_ppts.py
Master orchestrator script that compiles all topic-wise and module-level PPTX presentations.
Author: Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
"""

import os
import sys

from generate_comprehensive_ppts import (
    init_prs, create_title_slide
)
import ppts_module1
import ppts_module2
import ppts_module3
import ppts_module4

OUT_DIR = os.path.join(os.path.dirname(__file__), "assets", "ppts")

def generate_all():
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"[*] Generating all PowerPoint decks into: {OUT_DIR}")
    
    # ------------------ MODULE 1 TOPICS ------------------
    m1_topics = [
        ("M1.1_Internet_Overview.pptx", ppts_module1.build_m1_1),
        ("M1.2_Protocol_Layering.pptx", ppts_module1.build_m1_2),
        ("M1.3_Application_Layer_Paradigms.pptx", ppts_module1.build_m1_3),
        ("M1.4_WWW_and_HTTP.pptx", ppts_module1.build_m1_4),
        ("M1.5_FTP_Protocol.pptx", ppts_module1.build_m1_5),
        ("M1.6_Email_SMTP_MIME.pptx", ppts_module1.build_m1_6),
        ("M1.7_DNS_System.pptx", ppts_module1.build_m1_7),
        ("M1.8_P2P_BitTorrent.pptx", ppts_module1.build_m1_8),
        ("M1.9_Application_Layer_Case_Study.pptx", ppts_module1.build_m1_9),
        ("Module_1_Application_Layer.pptx", ppts_module1.build_module_1_master),
    ]
    
    for filename, builder in m1_topics:
        prs = builder()
        out_path = os.path.join(OUT_DIR, filename)
        prs.save(out_path)
        print(f"  [+] Generated {filename} ({len(prs.slides)} slides)")

    # ------------------ MODULE 2 TOPICS ------------------
    m2_topics = [
        ("M2.1.1_Transport_Layer_Services.pptx", ppts_module2.build_m2_1_1),
        ("M2.1.2_Transport_Protocols_UDP.pptx", ppts_module2.build_m2_1_2),
        ("M2.1.3_TCP_Architecture_Handshake.pptx", ppts_module2.build_m2_1_3),
        ("M2.1.4_TCP_Congestion_Flow_Control.pptx", ppts_module2.build_m2_1_4),
        ("M2.1.5_Socket_Programming_IO_Multiplexing.pptx", ppts_module2.build_m2_1_5),
        ("M2.2.1_Network_Layer_Introduction.pptx", ppts_module2.build_m2_2_1),
        ("M2.2.2_IPv4_Subnetting_CIDR.pptx", ppts_module2.build_m2_2_2),
        ("M2.2.3_Unicast_Routing_Dijkstra_RIP.pptx", ppts_module2.build_m2_2_3),
        ("M2.2.4_Multicast_Routing_Protocols.pptx", ppts_module2.build_m2_2_4),
        ("M2.2.5_NextGen_IPv6.pptx", ppts_module2.build_m2_2_5),
        ("M2.2.6_QoS_Traffic_Shaping.pptx", ppts_module2.build_m2_2_6),
        ("M2.3_Linux_Kernel_TCP_IP_Routing.pptx", ppts_module2.build_m2_3),
        ("Module_2_Transport_and_Network_Layer.pptx", ppts_module2.build_module_2_master),
    ]
    
    for filename, builder in m2_topics:
        prs = builder()
        out_path = os.path.join(OUT_DIR, filename)
        prs.save(out_path)
        print(f"  [+] Generated {filename} ({len(prs.slides)} slides)")

    # ------------------ MODULE 3 TOPICS ------------------
    m3_topics = [
        ("M3.1_DataLink_Layer_Framing.pptx", ppts_module3.build_m3_1),
        ("M3.2_Error_Detection_Correction_Flow.pptx", ppts_module3.build_m3_2),
        ("M3.3_Multiple_Access_Protocols.pptx", ppts_module3.build_m3_3),
        ("M3.4_Link_Layer_Addressing_ARP.pptx", ppts_module3.build_m3_4),
        ("M3.5_Ethernet_Protocols_IEEE_802.3.pptx", ppts_module3.build_m3_5),
        ("M3.5V_VLAN_IEEE_802.1Q.pptx", ppts_module3.build_m3_5v),
        ("M3.6_Connecting_Devices.pptx", ppts_module3.build_m3_6),
        ("M3.7_Wireless_LAN_IEEE_802.11.pptx", ppts_module3.build_m3_7),
        ("M3.8_Mobile_IP_Architecture.pptx", ppts_module3.build_m3_8),
        ("M3.9_Linux_Raw_Sockets_PF_PACKET.pptx", ppts_module3.build_m3_9),
        ("Module_3_DataLink_Layer_and_WLAN.pptx", ppts_module3.build_module_3_master),
    ]
    
    for filename, builder in m3_topics:
        prs = builder()
        out_path = os.path.join(OUT_DIR, filename)
        prs.save(out_path)
        print(f"  [+] Generated {filename} ({len(prs.slides)} slides)")

    # ------------------ MODULE 4 TOPICS ------------------
    m4_topics = [
        ("M4.1_Network_Management_SNMP.pptx", ppts_module4.build_m4_1),
        ("M4.2_ASN.1_and_MIB.pptx", ppts_module4.build_m4_2),
        ("M4.3_Data_Signals_Channel_Capacity.pptx", ppts_module4.build_m4_3),
        ("M4.4_Digital_Transmission_Line_Coding.pptx", ppts_module4.build_m4_4),
        ("M4.5_Analog_Transmission_Multiplexing.pptx", ppts_module4.build_m4_5),
        ("M4.6_Transmission_Media.pptx", ppts_module4.build_m4_6),
        ("Module_4_Network_Management_and_Physical_Layer.pptx", ppts_module4.build_module_4_master),
    ]
    
    for filename, builder in m4_topics:
        prs = builder()
        out_path = os.path.join(OUT_DIR, filename)
        prs.save(out_path)
        print(f"  [+] Generated {filename} ({len(prs.slides)} slides)")

    # ------------------ MASTER COMPLETE COURSE DECK ------------------
    prs_master = init_prs()
    create_title_slide(
        prs_master, "MASTER DECK", "PCCST501 Computer Networks",
        "Complete Lecture & Revision Course Deck (Modules 1 to 4) • KTU 2024 Scheme",
        "All Modules"
    )
    ppts_module1.build_module_1_master(prs_master)
    ppts_module2.build_module_2_master(prs_master)
    ppts_module3.build_module_3_master(prs_master)
    ppts_module4.build_module_4_master(prs_master)
    master_path = os.path.join(OUT_DIR, "PCCST501_Complete_Course_Deck.pptx")
    prs_master.save(master_path)
    print(f"  [+] Generated PCCST501_Complete_Course_Deck.pptx ({len(prs_master.slides)} slides)")
    print("\n[OK] All 41 topic & module presentation decks generated successfully!")

if __name__ == "__main__":
    generate_all()
