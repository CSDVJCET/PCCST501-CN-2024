"""
build_all_course_ppts_master.py
Generates all 36 individual topic PPTX presentations, 4 Module Master Decks,
and the Complete Master Course Deck for PCCST501 Computer Networks.
Prepared exclusively for:
Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
"""

import os
import ppts_module1_detailed as m1
import ppts_module2_detailed as m2
import ppts_module3_detailed as m3
import ppts_module4_detailed as m4
from build_master_ppts_framework import init_prs, create_title_slide

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "assets", "ppts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

TOPIC_BUILDERS = [
    # --- Module 1 ---
    ("M1.1_Internet_Overview.pptx", m1.build_m1_1),
    ("M1.2_Protocol_Layering.pptx", m1.build_m1_2),
    ("M1.3_Application_Layer_Paradigms.pptx", m1.build_m1_3),
    ("M1.4_WWW_and_HTTP.pptx", m1.build_m1_4),
    ("M1.5_FTP_Protocol.pptx", m1.build_m1_5),
    ("M1.6_Email_SMTP_MIME.pptx", m1.build_m1_6),
    ("M1.7_DNS_System.pptx", m1.build_m1_7),
    ("M1.8_P2P_BitTorrent.pptx", m1.build_m1_8),
    ("M1.9_Application_Layer_Case_Study.pptx", m1.build_m1_9),
    ("Module_1_Application_Layer.pptx", m1.build_module_1_master),

    # --- Module 2 ---
    ("M2.1.1_Transport_Layer_Services.pptx", m2.build_m2_1_1),
    ("M2.1.2_Transport_Protocols_UDP.pptx", m2.build_m2_1_2),
    ("M2.1.3_TCP_Architecture_Handshake.pptx", m2.build_m2_1_3),
    ("M2.1.4_TCP_Congestion_Flow_Control.pptx", m2.build_m2_1_4),
    ("M2.1.5_Socket_Programming_IO_Multiplexing.pptx", m2.build_m2_1_5),
    ("M2.2.1_Network_Layer_Introduction.pptx", m2.build_m2_2_1),
    ("M2.2.2_IPv4_Subnetting_CIDR.pptx", m2.build_m2_2_2),
    ("M2.2.3_Unicast_Routing_Dijkstra_RIP.pptx", m2.build_m2_2_3),
    ("M2.2.4_Multicast_Routing_Protocols.pptx", m2.build_m2_2_4),
    ("M2.2.5_NextGen_IPv6.pptx", m2.build_m2_2_5),
    ("M2.2.6_QoS_Traffic_Shaping.pptx", m2.build_m2_2_6),
    ("M2.3_Linux_Kernel_TCP_IP_Routing.pptx", m2.build_m2_3),
    ("Module_2_Transport_and_Network_Layer.pptx", m2.build_module_2_master),

    # --- Module 3 ---
    ("M3.1_DataLink_Layer_Framing.pptx", m3.build_m3_1),
    ("M3.2_Error_Detection_Correction_Flow.pptx", m3.build_m3_2),
    ("M3.3_Multiple_Access_Protocols.pptx", m3.build_m3_3),
    ("M3.4_Link_Layer_Addressing_ARP.pptx", m3.build_m3_4),
    ("M3.5_Ethernet_Protocols_IEEE_802.3.pptx", m3.build_m3_5),
    ("M3.5V_VLAN_IEEE_802.1Q.pptx", m3.build_m3_5v),
    ("M3.6_Connecting_Devices.pptx", m3.build_m3_6),
    ("M3.7_Wireless_LAN_IEEE_802.11.pptx", m3.build_m3_7),
    ("M3.8_Mobile_IP_Architecture.pptx", m3.build_m3_8),
    ("M3.9_Linux_Raw_Sockets_PF_PACKET.pptx", m3.build_m3_9),
    ("Module_3_DataLink_Layer_and_WLAN.pptx", m3.build_module_3_master),

    # --- Module 4 ---
    ("M4.1_Network_Management_SNMP.pptx", m4.build_m4_1),
    ("M4.2_ASN.1_and_MIB.pptx", m4.build_m4_2),
    ("M4.3_Data_Signals_Channel_Capacity.pptx", m4.build_m4_3),
    ("M4.4_Digital_Transmission_Line_Coding.pptx", m4.build_m4_4),
    ("M4.5_Analog_Transmission_Multiplexing.pptx", m4.build_m4_5),
    ("M4.6_Transmission_Media.pptx", m4.build_m4_6),
    ("Module_4_Network_Management_and_Physical_Layer.pptx", m4.build_module_4_master),
]

def build_complete_course_deck():
    """Generates the master 150+ slide complete course deck across all 4 modules."""
    prs = init_prs()
    create_title_slide(
        prs, "COMPLETE COURSE DECK", "PCCST501 Computer Networks",
        "KTU 2024 Scheme Curriculum • Modules 1 to 4 Complete Comprehensive Lecture Deck",
        "PCCST501 Master"
    )
    m1.build_module_1_master(prs)
    m2.build_module_2_master(prs)
    m3.build_module_3_master(prs)
    m4.build_module_4_master(prs)
    out_path = os.path.join(OUTPUT_DIR, "PCCST501_Complete_Course_Deck.pptx")
    prs.save(out_path)
    print(f"Generated Master Course Deck: {out_path} ({len(prs.slides)} slides)")

def main():
    print("===================================================================")
    print("Building Professional Presentation Decks for Prof. Anju Markose...")
    print("===================================================================")
    for filename, builder_fn in TOPIC_BUILDERS:
        prs = builder_fn()
        out_path = os.path.join(OUTPUT_DIR, filename)
        prs.save(out_path)
        print(f"  [+] Generated: {filename:<48} | Slides: {len(prs.slides)}")
    
    build_complete_course_deck()
    print("\nAll PPTX presentation decks successfully generated and saved to assets/ppts/")

if __name__ == "__main__":
    main()
