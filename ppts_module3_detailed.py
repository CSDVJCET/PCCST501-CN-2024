"""
ppts_module3_detailed.py
Comprehensive, classroom-ready presentation decks for Module 3: Data Link Layer, MAC Protocols & Wireless LANs.
Prepared exclusively for:
Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
PCCST501 Computer Networks (KTU 2024 Scheme)
"""

from build_master_ppts_framework import (
    init_prs, create_title_slide, create_content_slide, 
    create_comparison_slide, create_numerical_slide, create_code_slide, create_exam_booster_slide
)

def build_m3_1(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.1", "Data Link Layer Design & Framing Techniques",
        "Node-to-Node Link Services, Character Count, Byte Stuffing (Flag/ESC), Bit Stuffing (HDLC), Physical Coding Violations",
        "Module 3"
    )
    
    create_content_slide(prs, "3.1.1 Data Link Layer Design & Link Abstraction", "M3.1 FRAMING BASICS", [
        ("Node-to-Node Service Mission", "Responsible for transferring datagrams from one node (host, router, switch) to an adjacent node over an individual physical communication link."),
        ("Link Layer Responsibilities", "1. **Framing**: Encapsulating L3 datagrams into L2 frames with header and trailer. 2. **Link Access**: MAC protocols coordinate shared medium access. 3. **Reliable Delivery**: Flow control and ARQ on error-prone wireless links. 4. **Error Detection & Correction**: Parity, Checksum, CRC, Hamming codes."),
        ("Framing Methods Overview", "1. Character Count, 2. Byte Stuffing (Character-oriented), 3. Bit Stuffing (Bit-oriented), 4. Physical Layer Coding Violations (e.g., Manchester invalid transitions).")
    ], "Framing Taxonomy", [
        "Byte Count: Header count field",
        "Byte Stuffing: Flag + ESC bytes",
        "Bit Stuffing: 5 consecutive 1s rule",
        "Physical Violations: Line coding",
        "FCS: CRC trailer at end"
    ])
    
    create_comparison_slide(prs, "3.1.2 Stuffing Techniques: Byte Stuffing vs Bit Stuffing", "M3.1 STUFFING COMPARISON",
        "Byte Stuffing (Character-Oriented Framing)", [
            ("Delimiter", "Frame begins and ends with dedicated Flag Byte `FLAG` (e.g., `0x7E` in PPP)"),
            ("Escape Mechanism", "If `FLAG` occurs inside payload data, sender inserts an Escape Byte `ESC` (`0x7D`) immediately before it"),
            ("ESC in Data", "If `ESC` itself appears in data, sender escapes it with another `ESC` (`ESC ESC`)"),
            ("Receiver Action", "Receiver strips any `ESC` byte and treats following byte as raw data")
        ],
        "Bit Stuffing (Bit-Oriented Framing / HDLC)", [
            ("Delimiter Pattern", "Frame delimited by 8-bit flag pattern `01111110` (`0x7E`) at start and end"),
            ("Sender Rule", "Whenever sender encounters **5 consecutive 1s** in data stream (`11111`), it automatically stuffs a **`0` bit** immediately after it"),
            ("Receiver Rule", "Whenever receiver detects 5 consecutive 1s: if 6th bit is `0`, it de-stuffs (discards) the `0`; if 6th bit is `1` and 7th is `0`, it recognizes `FLAG`"),
            ("Advantage", "Completely arbitrary payload length; zero character-set dependency")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M3.1", "Data Link Layer Framing", "K2 Understand",
        [
            "Explain the four framing methods used in the Data Link Layer with neat diagrams. (8 Marks)",
            "Given the data bit stream `01101111110111110010`, show the transmitted bit sequence after bit stuffing in HDLC. (5 Marks)"
        ],
        [
            "Bit stuffing inserts a 0 after five consecutive 1s to prevent false flag detection.",
            "Byte stuffing uses escape characters (`ESC`) to preserve transparency in character protocols.",
            "Framing enables receivers to reliably locate the start and end of frames in raw bit streams."
        ]
    )
    return prs

def build_m3_2(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.2", "Data Link Control: Error Detection, Correction & Flow Control",
        "Hamming Distance, 2D Parity, Internet Checksum, CRC-32 Modulo-2 Division, Hamming (7,4) Code, Stop-and-Wait, Go-Back-N, Selective Repeat",
        "Module 3"
    )
    
    create_content_slide(prs, "3.2.1 Block Coding & Hamming Distance Theory", "M3.2 ERROR CONTROL THEORY", [
        ("Block Coding Principles", "Dataword of $k$ bits encoded into Codeword of $n$ bits ($n > k$) by appending $r = n - k$ redundant parity bits."),
        ("Hamming Distance $d(x,y)$", "The number of bit positions in which two codewords $x$ and $y$ differ (computed by taking XOR and counting number of 1s)."),
        ("Minimum Hamming Distance ($d_{min}$)", "The smallest Hamming distance between any pair of valid codewords in the codebook."),
        ("Error Detection Capability", "To detect up to $s$ bit errors: $d_{min} \\ge s + 1$ (e.g., Simple Parity has $d_{min} = 2$, detects single-bit errors $s = 1$)."),
        ("Error Correction Capability", "To correct up to $t$ bit errors: $d_{min} \\ge 2t + 1$ (e.g., Single-bit error correction $t = 1$ requires $d_{min} \\ge 3$).")
    ], "Hamming Distance Rules", [
        "Detect s errors: d_min >= s + 1",
        "Correct t errors: d_min >= 2t + 1",
        "Simple Parity: d_min = 2",
        "Hamming (7,4): d_min = 3",
        "r parity bits: 2^r >= k + r + 1"
    ])
    
    create_numerical_slide(
        prs, "3.2.2 Worked KTU Numerical: CRC Modulo-2 Polynomial Division", "M3.2 CRC WORKED PROBLEM",
        "A data bit stream D = 10100100 is to be transmitted using CRC generator polynomial G(x) = x^4 + x^2 + 1 (binary generator G = 10101). (a) Determine the 4-bit CRC Checksum (Frame Check Sequence FCS), (b) What codeword is transmitted? (c) Show that receiver detects zero remainder in the absence of bit errors.",
        [
            "Generator G(x) = x^4 + x^2 + 1 -> Degree r = 4 -> Generator bit string G = 10101 (5 bits).",
            "Step 1: Append r = 4 zeros to data D: D' = 10100100 0000 (12 bits).",
            "Step 2: Perform Modulo-2 binary division (XOR operations) of D' by G.",
            "Step 3: Remainder of division is the 4-bit CRC Checksum R."
        ],
        [
            (1, "Dividend: 101001000000 | Divisor: 10101"),
            (2, "10100 XOR 10101 -> Remainder 00001; bring down bits -> 0001100..."),
            (3, "Continuing Modulo-2 XOR division yields 4-bit Remainder R = 1100."),
            (4, "Transmitted Codeword T = Data + CRC = 10100100 1100 (12 bits)."),
            (5, "Receiver Divides T (101001001100) by G (10101) -> Remainder = 0000 (Valid / No errors!).")
        ],
        "CRC Checksum = 1100 | Transmitted Codeword = 101001001100",
        "Modulo-2 addition and subtraction are both identical to bitwise XOR with zero carries/borrows."
    )
    
    create_numerical_slide(
        prs, "3.2.3 Worked KTU Numerical: Hamming (7,4) Single-Bit Error Correction", "M3.2 HAMMING CODE WORKED",
        "A 4-bit dataword D = 1011 (d4=1, d3=0, d2=1, d1=1) is encoded using Hamming (7,4) code with parity bits at positions 1, 2, 4. (a) Generate 7-bit codeword. (b) If received word is R = 1011011, calculate syndrome bits (s3, s2, s1) and locate the erroneous bit position.",
        [
            "Bit positions 1 to 7: p1 (pos 1), p2 (pos 2), d1 (pos 3), p4 (pos 4), d2 (pos 5), d3 (pos 6), d4 (pos 7).",
            "p1 checks positions with bit 1 set (1, 3, 5, 7): p1 = d1 XOR d2 XOR d4.",
            "p2 checks positions with bit 2 set (2, 3, 6, 7): p2 = d1 XOR d3 XOR d4.",
            "p4 checks positions with bit 4 set (4, 5, 6, 7): p4 = d2 XOR d3 XOR d4.",
            "Syndrome S = (s4 s2 s1) indicates decimal error bit position (0 = no error)."
        ],
        [
            (1, "p1 = 1 XOR 1 XOR 1 = 1 | p2 = 1 XOR 0 XOR 1 = 0 | p4 = 1 XOR 0 XOR 1 = 0"),
            (2, "Generated Codeword: (p1, p2, d1, p4, d2, d3, d4) = (1, 0, 1, 0, 1, 0, 1) -> 1010101"),
            (3, "Received Word R = (r1..r7) = (1, 1, 0, 1, 1, 0, 1) (bit 2 corrupted!)"),
            (4, "s1 = r1 XOR r3 XOR r5 XOR r7 = 1 XOR 0 XOR 1 XOR 1 = 1"),
            (5, "s2 = r2 XOR r3 XOR r6 XOR r7 = 1 XOR 0 XOR 0 XOR 1 = 0"),
            (6, "s4 = r4 XOR r5 XOR r6 XOR r7 = 1 XOR 1 XOR 0 XOR 1 = 1 -> Syndrome = 101_2 = Pos 5 (d2 corrupted!)")
        ],
        "Syndrome S = 101 (Binary 5) -> Bit position 5 is inverted and corrected!",
        "Hamming (7,4) code can correct any single-bit error and detect any double-bit error."
    )
    
    create_comparison_slide(prs, "3.2.4 Sliding Window Flow Control: Stop-and-Wait vs GBN vs Selective Repeat", "M3.2 ARQ PROTOCOLS",
        "Stop-and-Wait ARQ", [
            ("Window Size", "$W_s = 1$, $W_r = 1$"),
            ("Sequence Bits", "1-bit ($m=1$, sequence numbers 0 and 1)"),
            ("Efficiency", "Extremely low on high-bandwidth-delay product links: $\\eta = 1 / (1 + 2a)$ where $a = t_{prop} / t_{trans}$"),
            ("Buffering", "1 frame buffer at sender and receiver")
        ],
        "Go-Back-N (GBN) ARQ", [
            ("Window Size", "$W_s = 2^m - 1$, $W_r = 1$ (Cumulative ACKs)"),
            ("On Loss", "Discards all subsequent out-of-order frames; retransmits entire window from lost frame"),
            ("Sender Buffer", "Buffers $W_s$ frames; receiver requires zero buffer"),
            ("Efficiency", "High efficiency unless error rate is severe")
        ],
        "Selective Repeat (SR) ARQ", [
            ("Window Size", "$W_s = 2^{m-1}$, $W_r = 2^{m-1}$ (Individual ACKs)"),
            ("On Loss", "Receiver buffers out-of-order frames; sender retransmits **only the lost frame**"),
            ("Buffer Needs", "Both sender and receiver maintain $2^{m-1}$ buffer queues"),
            ("Efficiency", "Optimal bandwidth utilization on noisy channels")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M3.2", "Error Detection & Flow Control", "K3 Apply",
        [
            "Explain CRC error detection with a polynomial division example. Why is CRC implemented in hardware with LFSR shift registers? (8 Marks)",
            "Derive the maximum sender window size for Go-Back-N ($2^m - 1$) and Selective Repeat ($2^{m-1}$). Explain why exceeding these limits causes protocol failure. (8 Marks)",
            "Explain Hamming (7,4) code with syndrome error correction calculation. (7 Marks)"
        ],
        [
            "CRC detects all single-bit, double-bit, odd numbers of errors, and burst errors up to generator polynomial degree $r$.",
            "Go-Back-N window is $2^m - 1$ to prevent receiver from mistaking duplicate frames for new ones.",
            "Selective Repeat requires equal sender and receiver window sizes bounded at $2^{m-1}$."
        ]
    )
    return prs

def build_m3_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.3", "Multiple Access Control (MAC) Protocols",
        "Random Access (Pure & Slotted ALOHA, CSMA, CSMA/CD, CSMA/CA), Controlled Access (Polling, Token Ring), Channelization (CDMA)",
        "Module 3"
    )
    
    create_comparison_slide(prs, "3.3.1 Random Access: Pure ALOHA vs Slotted ALOHA", "M3.3 ALOHA COMPARISON",
        "Pure ALOHA (Norman Abramson, 1970)", [
            ("Transmission Rule", "Transmit continuous frame whenever data is ready without sensing channel"),
            ("Vulnerable Period", "$V_p = 2 \\times T_{frame}$ (Collision occurs if any other node transmits within 2 frame times)"),
            ("Throughput Formula", "$S = G \\cdot e^{-2G}$ where $G$ = traffic load"),
            ("Maximum Efficiency", "Maximum throughput $S_{max} = 1 / (2e) \\approx 18.4\\%$ at $G = 0.5$"),
            ("Collisions", "High collision rate due to uncoordinated overlapping frames")
        ],
        "Slotted ALOHA (Roberts, 1972)", [
            ("Transmission Rule", "Time divided into discrete slots equal to $T_{frame}$. Nodes transmit strictly at slot boundaries"),
            ("Vulnerable Period", "$V_p = 1 \\times T_{frame}$ (Halves vulnerability interval)"),
            ("Throughput Formula", "$S = G \\cdot e^{-G}$"),
            ("Maximum Efficiency", "Maximum throughput $S_{max} = 1 / e \\approx 36.8\\%$ at $G = 1.0$ (Exactly doubles Pure ALOHA!)"),
            ("Synchronization", "Requires global slot synchronization across all nodes")
        ]
    )
    
    create_content_slide(prs, "3.3.2 CSMA/CD: Carrier Sense Multiple Access with Collision Detection", "M3.3 CSMA/CD PROTOCOL", [
        ("Carrier Sense (Listen Before Talk)", "Node listens to channel before transmitting. 1-persistent: transmits immediately when idle; Non-persistent: waits random backoff if busy; p-persistent: transmits with probability $p$ when idle."),
        ("Collision Detection (Listen While Talk)", "Node continuously monitors voltage/energy on wire while transmitting. If signal amplitude exceeds collision threshold, collision is detected immediately!"),
        ("Jam Signal & Abort", "Upon detecting collision, node aborts transmission immediately and broadcasts a 32-48 bit **Jam Signal** to ensure all other nodes detect the collision."),
        ("Minimum Frame Size Constraint ($L_{min}$)", "To ensure a sender does not finish transmitting before collision signal propagates back: $T_{frame} \\ge 2 \\times T_{prop} \\implies \\frac{L_{min}}{R} \\ge 2 \\cdot \\frac{d}{s} \\implies L_{min} = 2 \\times T_{prop} \\times R$."),
        ("Binary Exponential Backoff (BEB)", "After $k$-th collision ($k \\le 10$), node picks random wait slot $r \\in \\{0, 1, 2, \\dots, 2^k - 1\\}$ and waits $r \\times 512$ bit times. Aborts after 16 consecutive collisions.")
    ], "CSMA/CD Summary", [
        "1-persistent sense",
        "Jam signal on collision",
        "L_min = 2 * t_prop * R",
        "Standard Ethernet L_min = 64 Bytes (512 bits)",
        "Backoff range: [0, 2^k - 1]"
    ])
    
    create_numerical_slide(
        prs, "3.3.3 Worked KTU Numerical: CSMA/CD Minimum Frame Size", "M3.3 CSMA/CD NUMERICAL",
        "A 1 Gbps Ethernet LAN runs over a 1 km fiber link with propagation speed s = 2 * 10^8 m/s. Calculate the minimum frame size required for proper collision detection. If transmission rate is increased to 10 Gbps over the same link, what must the new minimum frame size be?",
        [
            "L_min = 2 * t_prop * R",
            "t_prop = d / s = 1000 m / (2 * 10^8 m/s) = 5 * 10^-6 s = 5 microseconds.",
            "Round-trip propagation time 2 * t_prop = 10 microseconds = 10^-5 seconds.",
            "L_min = 2 * t_prop * R (bits)."
        ],
        [
            (1, "For R = 1 Gbps = 10^9 bps:"),
            (2, "L_min = 10^-5 s * 10^9 bps = 10,000 bits = 10,000 / 8 = 1250 Bytes."),
            (3, "For R = 10 Gbps = 10^10 bps:"),
            (4, "L_min = 10^-5 s * 10^10 bps = 100,000 bits = 12,500 Bytes (12.5 KB)."),
            (5, "Conclusion: At 10 Gbps, minimum frame size becomes unfeasibly large; hence 10 Gigabit Ethernet mandates full-duplex point-to-point links (disabling CSMA/CD entirely).")
        ],
        "1 Gbps: L_min = 1250 Bytes | 10 Gbps: L_min = 12,500 Bytes",
        "CSMA/CD is only applicable on half-duplex shared media; full-duplex switched Ethernet does not require CSMA/CD."
    )
    
    create_exam_booster_slide(
        prs, "M3.3", "Multiple Access Protocols", "K3 Apply",
        [
            "Derive the maximum channel throughput for Pure ALOHA ($18.4\\%$) and Slotted ALOHA ($36.8\\%$) with vulnerable period diagrams. (8 Marks)",
            "Explain the working of CSMA/CD with the Binary Exponential Backoff (BEB) algorithm and minimum frame size derivation. (8 Marks)",
            "Explain Code Division Multiple Access (CDMA) using orthogonal Walsh chip sequences with an encoding and decoding example. (7 Marks)"
        ],
        [
            "Slotted ALOHA doubles Pure ALOHA efficiency by eliminating partial frame collisions.",
            "Minimum frame size in CSMA/CD guarantees collision detection before transmission ends ($L_{min} = 2 \\cdot t_{prop} \\cdot R$).",
            "CDMA allows simultaneous transmission over the same frequency band using orthogonal chip codes."
        ]
    )
    return prs

def build_m3_4(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.4", "Link-Layer Addressing & Address Resolution Protocol (ARP)",
        "48-Bit MAC Addresses (EUI-48), ARP Request (Broadcast) & ARP Reply (Unicast), ARP Cache & Timeout, Proxy ARP, Subnet Crossing",
        "Module 3"
    )
    
    create_content_slide(prs, "3.4.1 MAC Addressing & Address Resolution Protocol (ARP)", "M3.4 ARP PROTOCOL", [
        ("MAC Hardware Address (48 bits / 6 Bytes)", "Burned into NIC ROM (e.g., `1A:2B:3C:4D:5E:6F`). First 24 bits = OUI (Organizationally Unique Identifier assigned by IEEE); Last 24 bits = Vendor NIC serial number."),
        ("ARP Mission (RFC 826)", "Dynamically resolves a known 32-bit IP address into its corresponding 48-bit MAC address on the local physical subnet."),
        ("ARP Message Flow", "1. **ARP Request**: Host broadcasts frame (`FF:FF:FF:FF:FF:FF`) asking: 'Who owns IP 192.168.1.5? Send your MAC to 192.168.1.2'. \\n 2. **ARP Reply**: Target host unicasts reply containing its physical MAC address directly to the sender. \\n 3. **ARP Table**: Sender caches the mapping in its local ARP Cache table with a TTL timer (typically 20 minutes)."),
        ("Proxy ARP & Gratuitous ARP", "**Proxy ARP**: Router responds to ARP request on behalf of a remote node. **Gratuitous ARP**: Host announces its own IP/MAC to detect duplicate IP conflicts and update switch MAC tables.")
    ], "ARP Key Facts", [
        "ARP Request: L2 Broadcast (FF:..:FF)",
        "ARP Reply: L2 Unicast",
        "L2 Frame Type: 0x0806 (ARP)",
        "ARP Cache: Dynamic IP->MAC table",
        "Gratuitous ARP: IP conflict check"
    ])
    
    create_content_slide(prs, "3.4.2 Packet Forwarding Across Subnets (MAC & IP Rewriting)", "M3.4 SUBNET ROUTING", [
        ("Scenario: Host A (Subnet 1) sends packet to Host B (Subnet 2) via Router R", "Source Host A creates L3 IP packet: `Src IP = IP_A`, `Dst IP = IP_B` (IP addresses remain constant throughout end-to-end path)."),
        ("Hop 1 (Host A -> Router R)", "Host A inspects routing table; determines destination `IP_B` is outside local subnet. Encapsulates IP packet into L2 frame: `Src MAC = MAC_A`, `Dst MAC = MAC_Router_Interface_1` (uses ARP to find router MAC)."),
        ("Router R Processing", "Router decapsulates L2 frame, inspects L3 `Dst IP = IP_B`, consults FIB routing table, decrements TTL, recomputes IP checksum, and determines outgoing Interface 2."),
        ("Hop 2 (Router R -> Host B)", "Router encapsulates packet into a fresh L2 frame: `Src MAC = MAC_Router_Interface_2`, `Dst MAC = MAC_B` (via ARP on Subnet 2)."),
        ("Core Takeaway", "**IP addresses remain unchanged end-to-end; MAC addresses change at every single router hop!**")
    ], "Hop-by-Hop Headers", [
        "Hop 1: Src MAC_A -> Dst MAC_R1",
        "Hop 2: Src MAC_R2 -> Dst MAC_B",
        "End-to-End: Src IP_A -> Dst IP_B",
        "L2 MAC rewritten per hop",
        "L3 IP preserved end-to-end"
    ])
    
    create_exam_booster_slide(
        prs, "M3.4", "MAC Addressing & ARP", "K3 Apply",
        [
            "Explain the operation of Address Resolution Protocol (ARP) with request and reply frame structures. (7 Marks)",
            "Trace the step-by-step changes in Source/Destination IP and Source/Destination MAC addresses as a packet travels from Host A to Host B across an intermediate router. (8 Marks)"
        ],
        [
            "ARP bridges Layer 3 IP addresses to Layer 2 physical MAC addresses.",
            "ARP requests are L2 broadcasts (`FF:FF:FF:FF:FF:FF`); ARP replies are L2 unicasts.",
            "L3 IP addresses identify end hosts; L2 MAC addresses identify next-hop network interfaces."
        ]
    )
    return prs

def build_m3_5(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.5", "Ethernet Protocols & IEEE 802.3 Architecture",
        "Standard Ethernet (10M), Fast Ethernet (100M), Gigabit Ethernet (1G), 10GbE, IEEE 802.3 Frame Format (64B to 1518B)",
        "Module 3"
    )
    
    create_content_slide(prs, "3.5.1 IEEE 802.3 Ethernet Frame Format", "M3.5 ETHERNET FRAME", [
        ("Preamble (7 Bytes)", "7 bytes of alternating `10101010` patterns used to synchronize receiver clock circuitry."),
        ("Start of Frame Delimiter - SFD (1 Byte)", "1 byte pattern `10101011` indicating that destination MAC address begins immediately on the next bit."),
        ("Destination MAC Address (6 Bytes)", "48-bit hardware address of target NIC (or broadcast `FF:FF:FF:FF:FF:FF`)."),
        ("Source MAC Address (6 Bytes)", "48-bit hardware address of sending NIC."),
        ("Type / Length Field (2 Bytes)", "If $\\ge 1536$ (0x0600), specifies upper layer protocol (EtherType: IPv4 `0x0800`, ARP `0x0806`, IPv6 `0x86DD`). If $\\le 1500$, specifies frame payload length."),
        ("Payload / Data (46 to 1500 Bytes)", "Carries L3 datagram. Minimum payload is 46 bytes (padded with zeros if smaller) to enforce the 64-byte minimum frame size constraint."),
        ("Frame Check Sequence - FCS (4 Bytes)", "32-bit Cyclic Redundancy Check (CRC-32) computed over Dst MAC, Src MAC, Type, and Payload.")
    ], "Frame Sizes", [
        "Preamble + SFD: 8 Bytes",
        "Header + FCS: 18 Bytes",
        "Min Payload: 46 Bytes",
        "Max Payload (MTU): 1500 Bytes",
        "Min Frame Size: 64 Bytes",
        "Max Frame Size: 1518 Bytes"
    ])
    
    create_comparison_slide(prs, "3.5.2 Ethernet Speed Evolution: Standard to 10GbE", "M3.5 ETHERNET EVOLUTION",
        "Standard & Fast Ethernet", [
            ("Standard (10 Mbps)", "10Base5 (Thicknet coaxial), 10Base2 (Thinnet), 10Base-T (UTP Cat 3/5 with Hub/Switch). Uses Manchester line coding"),
            ("Fast Ethernet (100 Mbps)", "100Base-TX (Cat 5 UTP using 4B/5B and MLT-3 coding), 100Base-FX (Fiber). Introduces Auto-Negotiation")
        ],
        "Gigabit & 10G Ethernet", [
            ("Gigabit Ethernet (1 Gbps)", "1000Base-T (Cat 5e/6 UTP using 4 pairs full-duplex with 8B/10B coding), 1000Base-SX/LX (Fiber). Introduces Carrier Extension and Packet Bursting for half-duplex"),
            ("10 Gigabit Ethernet (10 Gbps)", "10GBase-T (Cat 6a/7) and 10GBase-SR/LR. Exclusively full-duplex switched connections; eliminates CSMA/CD completely")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M3.5", "IEEE 802.3 Ethernet", "K2 Understand",
        [
            "Draw the IEEE 802.3 Ethernet frame format and explain the function of each field. Why is the minimum frame size 64 bytes and maximum 1518 bytes? (8 Marks)",
            "Compare Standard Ethernet, Fast Ethernet, Gigabit Ethernet, and 10 Gigabit Ethernet with respect to medium, coding, and transmission modes. (7 Marks)"
        ],
        [
            "Preamble and SFD synchronize bit timing; FCS trailer provides CRC-32 error detection.",
            "64-byte minimum frame ensures collision detection in 10/100 Mbps CSMA/CD networks.",
            "10GbE operates strictly in full-duplex mode over switches and fiber links."
        ]
    )
    return prs

def build_m3_5v(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.5V", "Virtual Local Area Networks (VLANs - IEEE 802.1Q)",
        "Broadcast Containment, Port-Based vs Tagged VLANs, IEEE 802.1Q 4-Byte Tag (VID 1-4094), Access vs Trunk Ports, Router-on-a-Stick",
        "Module 3"
    )
    
    create_content_slide(prs, "3.5V.1 VLAN Motivation & IEEE 802.1Q Tagged Framing", "M3.5V VLAN ARCHITECTURE", [
        ("VLAN Motivation", "Physically co-located hosts can be partitioned into logical broadcast domains regardless of physical switch topology. Prevents broadcast storms, enhances security, and organizes departments logically (e.g., Faculty VLAN, Student VLAN, Lab VLAN)."),
        ("Port-Based VLAN (Untagged)", "Switch ports assigned static VLAN IDs. Traffic inside switch segregated by port group; frames on access links remain standard untagged Ethernet frames."),
        ("IEEE 802.1Q Tagged Frame (4 Bytes Inserted after Source MAC)", "1. **TPID (Tag Protocol Identifier - 16 bits)**: Set to `0x8100` (identifies frame as 802.1Q tagged). \\n 2. **PCP (Priority Code Point - 3 bits)**: IEEE 802.1p Quality of Service priority (0 to 7). \\n 3. **DEI (Drop Eligible Indicator - 1 bit)**: Set to 1 if frame can be dropped during congestion. \\n 4. **VID (VLAN Identifier - 12 bits)**: Uniquely identifies VLAN number (1 to 4094; 0 and 4095 reserved)."),
        ("Access Port vs Trunk Port", "**Access Port**: Connects end hosts; carries traffic for 1 untagged VLAN only. **Trunk Port**: Interconnects switches/routers; carries multiplexed tagged traffic for multiple VLANs simultaneously.")
    ], "IEEE 802.1Q Tag", [
        "TPID: 0x8100 (16 bits)",
        "PCP: 3 bits (QoS Priority)",
        "DEI: 1 bit (Drop eligibility)",
        "VID: 12 bits (4094 VLANs)",
        "Trunking: Carries tagged frames",
        "Access: Carries untagged frames"
    ])
    
    create_content_slide(prs, "3.5V.2 Inter-VLAN Routing: Router-on-a-Stick vs Layer 3 Switch", "M3.5V INTER-VLAN ROUTING", [
        ("Why Inter-VLAN Routing?", "By design, hosts on different VLANs cannot communicate at Layer 2 even if plugged into the same physical switch. Inter-VLAN routing requires Layer 3 packet forwarding."),
        ("Router-on-a-Stick (Legacy Approach)", "A single physical Ethernet interface on an external router is connected to a switch Trunk port. The router interface is divided into logical **Sub-interfaces** (e.g., `eth0.10`, `eth0.20`), each configured with the default gateway IP and 802.1Q encapsulation for its respective VLAN."),
        ("Layer 3 Switch (Modern Core Routing)", "Switches with built-in hardware ASIC routing capabilities. Configured with **Switched Virtual Interfaces (SVIs)** (`interface vlan 10`, `interface vlan 20`) providing multi-gigabit wire-speed inter-VLAN routing without external router bottleneck.")
    ], "Inter-VLAN Methods", [
        "Router-on-a-Stick: 1 Trunk link",
        "Sub-interfaces: eth0.10, eth0.20",
        "L3 Switch: Hardware SVI routing",
        "Wire-speed routing in L3 switch",
        "Isolates broadcast domains"
    ])
    
    create_exam_booster_slide(
        prs, "M3.5V", "Virtual LANs (VLANs)", "K3 Apply",
        [
            "Explain the benefits of VLANs and illustrate the 4-byte IEEE 802.1Q tag header format. (7 Marks)",
            "Differentiate between Access ports and Trunk ports on an Ethernet switch. (5 Marks)",
            "Explain Inter-VLAN routing using the Router-on-a-Stick architecture with a network diagram and configuration concepts. (7 Marks)"
        ],
        [
            "VLANs partition a single physical switch into multiple isolated broadcast domains.",
            "IEEE 802.1Q tag inserts 4 bytes (TPID 0x8100 + 12-bit VID for 4094 VLANs).",
            "Trunk links carry tagged multiplexed frames between switches and routers."
        ]
    )
    return prs

def build_m3_6(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.6", "Connecting Devices & Spanning Tree Protocol (STP)",
        "Repeaters, Hubs (L1), Bridges & Layer 2 Switches (MAC Learning), Spanning Tree Protocol (IEEE 802.1D STP), Routers & Layer 3 Switches",
        "Module 3"
    )
    
    create_comparison_slide(prs, "3.6.1 Connecting Devices Taxonomy & Collision/Broadcast Domains", "M3.6 CONNECTING DEVICES",
        "Layer 1: Repeaters & Hubs", [
            ("Operating Layer", "Physical Layer (L1)"),
            ("Function", "Regenerates and amplifies electrical/optical signals; broadcasts incoming bits to all ports"),
            ("Collision Domains", "Single shared collision domain across all ports"),
            ("Broadcast Domains", "Single broadcast domain"),
            ("Intelligence", "Zero intelligence / No buffering")
        ],
        "Layer 2: Bridges & Switches", [
            ("Operating Layer", "Data Link Layer (L2)"),
            ("Function", "Inspects MAC addresses; filters and forwards frames selectively using hardware MAC Learning table"),
            ("Collision Domains", "Microsegmentation: **Each individual port is an isolated collision domain**"),
            ("Broadcast Domains", "Single broadcast domain (unless partitioned via VLANs)"),
            ("Buffering", "Store-and-forward / Cut-through")
        ],
        "Layer 3: Routers & L3 Switches", [
            ("Operating Layer", "Network Layer (L3)"),
            ("Function", "Routes packets across heterogeneous networks using IP addresses"),
            ("Collision Domains", "Separate collision domain per port"),
            ("Broadcast Domains", "**Separates broadcast domains** (does not forward L2 broadcasts)"),
            ("Routing Table", "Maintains FIB routing table")
        ]
    )
    
    create_content_slide(prs, "3.6.2 Spanning Tree Protocol (IEEE 802.1D STP)", "M3.6 SPANNING TREE PROTOCOL", [
        ("The Layer 2 Loop Problem", "Redundant links between switches provide fault tolerance, but create disastrous **Broadcast Storms**, multiple frame copies, and MAC table instability."),
        ("STP Goal", "Logically disables redundant links by placing them in Blocking state, dynamically constructing a loop-free active tree topology while keeping backup paths on standby."),
        ("BPDU (Bridge Protocol Data Units)", "Switches exchange BPDUs containing: `Bridge ID = Priority (2B) + MAC Address (6B)` (Default priority = 32768)."),
        ("4-Step STP Algorithm", "1. **Root Bridge Election**: Switch with the lowest Bridge ID becomes the Root Bridge. \\n 2. **Root Port (RP) Selection**: On each non-root switch, the port with the lowest path cost to the Root Bridge is selected as RP. \\n 3. **Designated Port (DP) Selection**: On each LAN segment, the port with the lowest path cost to Root becomes DP. \\n 4. **Blocking State**: All remaining ports are placed in Blocking/Discarding state to break loops.")
    ], "STP Algorithm Steps", [
        "1. Lowest Bridge ID -> Root Bridge",
        "2. Lowest Cost to Root -> Root Port (RP)",
        "3. Lowest Cost per Link -> Designated Port (DP)",
        "4. Remaining Ports -> Blocked / Alternate",
        "Convergence time: ~30-50 seconds (RSTP: < 1s)"
    ])
    
    create_exam_booster_slide(
        prs, "M3.6", "Connecting Devices & STP", "K3 Apply",
        [
            "Compare Repeaters, Hubs, Switches, and Routers with respect to operating layer, collision domains, and broadcast domains. (8 Marks)",
            "Explain the working of the Spanning Tree Protocol (IEEE 802.1D) with Bridge ID, Root Bridge election, Root Ports, and Blocking ports. (8 Marks)"
        ],
        [
            "Hubs extend collision domains; Switches isolate collision domains; Routers isolate broadcast domains.",
            "Transparent switches dynamically populate MAC tables by inspecting source MACs of arriving frames.",
            "STP prevents broadcast storms by breaking physical switching loops into a single logical tree."
        ]
    )
    return prs

def build_m3_7(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.7", "Wireless LANs: IEEE 802.11 (Wi-Fi) Architecture",
        "BSS, AP, ESS, Distribution System, Hidden/Exposed Terminal Problems, CSMA/CA with RTS/CTS, SIFS/PIFS/DIFS, 802.11 Frame (4 Addresses)",
        "Module 3"
    )
    
    create_content_slide(prs, "3.7.1 IEEE 802.11 Architecture & Terminal Problems", "M3.7 WIRELESS ARCHITECTURE", [
        ("Basic Service Set (BSS)", "The fundamental building block consisting of wireless stations and a central Access Point (AP) in Infrastructure mode (or peer-to-peer in Ad-hoc / IBSS mode)."),
        ("Extended Service Set (ESS)", "Multiple BSSs interconnected via a wired Distribution System (DS) sharing a common SSID, enabling seamless roaming across campus."),
        ("Hidden Terminal Problem", "Nodes A and C cannot hear each other due to distance or physical obstacles, but both are in range of AP B. If A and C transmit simultaneously, their frames collide at B!"),
        ("Exposed Terminal Problem", "Node B is transmitting to A. Node C wants to transmit to D (away from A). C senses B transmitting and unnecessarily defers, wasting channel capacity."),
        ("Solution: CSMA/CA with RTS/CTS Handshake", "Sender transmits short **RTS (Request to Send)** frame (20B). AP replies with **CTS (Clear to Send)** broadcast (14B) containing Network Allocation Vector (NAV) reservation time, silencing hidden terminals.")
    ], "802.11 Topology", [
        "BSS: AP + Associated Stations",
        "ESS: Multiple BSSs + Wired DS",
        "Hidden Terminal: Collisions at AP",
        "RTS/CTS: Virtual carrier sensing",
        "NAV: Channel reservation timer"
    ])
    
    create_content_slide(prs, "3.7.2 CSMA/CA Protocol Timing Intervals & 4-Address Frame", "M3.7 CSMA/CA TIMING", [
        ("Inter-Frame Space (IFS) Hierarchy", "1. **SIFS (Short IFS)**: Highest priority; used for immediate ACKs, CTS, and fragmented frames. \\n 2. **PIFS (PCF IFS)**: Medium priority; used in polling mode. \\n 3. **DIFS (DCF IFS)**: Standard priority; minimum wait time before station can contend for channel."),
        ("Contention Window (CW) & Backoff", "Station waits DIFS; if idle, selects random backoff slot in $[0, CW]$. Counts down while channel is idle; freezes counter during busy periods."),
        ("IEEE 802.11 4-Address Frame Format", "Frame Control (2B) | Duration/ID (2B) | Address 1 (6B: Receiver MAC) | Address 2 (6B: Transmitter MAC) | Address 3 (6B: Original Source or Final Dest MAC) | Sequence Control (2B) | Address 4 (6B: Used strictly when bridging across WDS wireless distribution links) | Payload (0-2312B) | FCS (4B).")
    ], "Timing Hierarchy", [
        "SIFS < PIFS < DIFS < EIFS",
        "SIFS: ACKs & CTS (Highest priority)",
        "DIFS: Standard data contention",
        "Addr 1: Immediate Receiver",
        "Addr 2: Immediate Transmitter",
        "Addr 3: Original Source / Dest",
        "Addr 4: WDS Wireless Bridge"
    ])
    
    create_exam_booster_slide(
        prs, "M3.7", "IEEE 802.11 Wireless LANs", "K3 Apply",
        [
            "Explain the Hidden Terminal and Exposed Terminal problems in Wireless LANs. How does CSMA/CA with RTS/CTS resolve them? (8 Marks)",
            "Explain the timing relationships between SIFS, PIFS, and DIFS in IEEE 802.11 CSMA/CA with a neat timing diagram. (7 Marks)",
            "Explain the four MAC address fields in the IEEE 802.11 frame format. When is Address 4 used? (6 Marks)"
        ],
        [
            "Wireless radios cannot detect collisions while transmitting; hence Wi-Fi uses collision avoidance (CSMA/CA).",
            "RTS and CTS frames carry NAV reservation timers to silence hidden nodes.",
            "Address 4 is populated only when frames are bridged between two wireless APs in WDS mode."
        ]
    )
    return prs

def build_m3_8(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.8", "Mobile IP Architecture & Protocols",
        "Mobile Node (MN), Home Agent (HA), Foreign Agent (FA), Home Address (HoA), Care-of Address (CoA), Tunneling & Triangle Routing",
        "Module 3"
    )
    
    create_content_slide(prs, "3.8.1 Mobile IP Architecture & Entities (RFC 5944)", "M3.8 MOBILE IP BASICS", [
        ("The Mobility Challenge", "Standard IP routing uses destination IP prefixes. If a mobile laptop moves to a new subnet, changing its IP address terminates all active TCP connections! Mobile IP allows a host to retain its permanent IP transparently."),
        ("Mobile IP Entities", "1. **Mobile Node (MN)**: The roaming host. \\n 2. **Home Network & Home Agent (HA)**: The home subnet and the router acting on behalf of MN when away. \\n 3. **Foreign Network & Foreign Agent (FA)**: The visited subnet router assisting MN. \\n 4. **Correspondent Node (CN)**: The peer host communicating with MN."),
        ("Dual-Address Mechanism", "1. **Home Address (HoA)**: Permanent IP address assigned in home subnet (used for active TCP sessions). \\n 2. **Care-of Address (CoA)**: Temporary IP address associated with visited foreign network.")
    ], "Core Entities", [
        "MN: Mobile Node",
        "HA: Home Agent router",
        "FA: Foreign Agent router",
        "HoA: Permanent IP address",
        "CoA: Temporary visited IP",
        "CN: Correspondent Node"
    ])
    
    create_content_slide(prs, "3.8.2 Operational Phases: Registration, Tunneling & Triangle Routing", "M3.8 MOBILE IP PHASES", [
        ("Phase 1: Agent Discovery", "Foreign Agents broadcast periodic Agent Advertisements (ICMP extension); MN detects it has moved and obtains a CoA."),
        ("Phase 2: Registration", "MN sends Registration Request to FA -> FA forwards to Home Agent (HA) -> HA updates binding table (`HoA -> CoA`) and sends Registration Reply."),
        ("Phase 3: Data Transfer (IP-in-IP Encapsulation Tunneling)", "CN sends packet to `HoA` -> Routed to Home Network -> Home Agent intercepts packet via Proxy ARP -> HA encapsulates packet inside a new IP header (`Src IP = HA`, `Dst IP = CoA`) -> Transmits through IP tunnel to FA -> FA decapsulates and delivers to MN."),
        ("Reverse Path & Triangle Routing Problem", "MN sends directly to CN via standard IP routing. However, traffic from CN travels through HA -> FA -> MN (inefficient Triangle Routing). Solution: Route Optimization allows CN to cache MN's CoA and tunnel directly.")
    ], "Tunneling Flow", [
        "CN -> Home Agent (HoA)",
        "HA intercepts (Proxy ARP)",
        "HA tunnels to FA (IP-in-IP)",
        "FA decapsulates -> MN",
        "MN replies directly to CN",
        "Triangle Routing fixed via CoA cache"
    ])
    
    create_exam_booster_slide(
        prs, "M3.8", "Mobile IP Architecture", "K2 Understand",
        [
            "Explain the architecture and entities of Mobile IP (MN, HA, FA, HoA, CoA) with a neat diagram. (8 Marks)",
            "Explain the three operational phases of Mobile IP: Agent Discovery, Registration, and Encapsulation Tunneling. (8 Marks)",
            "What is the Triangle Routing problem in Mobile IP, and how does Route Optimization solve it? (6 Marks)"
        ],
        [
            "Mobile IP preserves TCP connection survivability during subnet roaming.",
            "Home Agent intercepts packets using Proxy ARP and encapsulates them via IP-in-IP tunneling to the Care-of Address.",
            "Triangle routing introduces latency by routing all forward traffic through the Home Agent."
        ]
    )
    return prs

def build_m3_9(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.9", "Linux Network Programming: Raw Sockets & PF_PACKET",
        "Data Link Provider Interface (DLPI), BSD Packet Filter (BPF), Linux PF_PACKET / AF_PACKET (SOCK_RAW, ETH_P_ALL), Promiscuous Sniffer",
        "Module 3"
    )
    
    code_sniffer_example = """#include <sys/socket.h>
#include <netinet/ether.h>
#include <net/if.h>
#include <sys/ioctl.h>

int main() {
    // 1. Create Raw Packet Socket to capture all Ethernet frames
    int raw_sock = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    
    // 2. Enable Promiscuous Mode on network interface eth0
    struct ifreq ifr;
    strcpy(ifr.ifr_name, "eth0");
    ioctl(raw_sock, SIOCGIFFLAGS, &ifr);
    ifr.ifr_flags |= IFF_PROMISC;
    ioctl(raw_sock, SIOCSIFFLAGS, &ifr);
    
    // 3. Capture and Dissect Raw Ethernet Frame
    unsigned char buffer[2048];
    while (1) {
        int len = recvfrom(raw_sock, buffer, sizeof(buffer), 0, NULL, NULL);
        struct ether_header *eth = (struct ether_header *)buffer;
        printf("Src MAC: %s -> Dst MAC: %s | Protocol: 0x%04X\\n",
               ether_ntoa((struct ether_addr *)eth->ether_shost),
               ether_ntoa((struct ether_addr *)eth->ether_dhost),
               ntohs(eth->ether_type));
    }
}"""
    create_code_slide(
        prs, "3.9.1 Hands-On: Packet Sniffing with Linux `PF_PACKET`", "M3.9 LINUX RAW SOCKETS",
        code_sniffer_example,
        [
            ("`AF_PACKET` / `PF_PACKET`", "Linux-specific socket domain allowing direct interaction with Layer 2 device drivers, bypassing the standard kernel TCP/IP protocol stack entirely."),
            ("`SOCK_RAW` vs `SOCK_DGRAM`", "`SOCK_RAW` provides raw Ethernet frames including L2 header and trailer; `SOCK_DGRAM` provides frames with L2 header stripped."),
            ("Protocol Filter `ETH_P_ALL`", "Captures all incoming and outgoing frames (IPv4, ARP, IPv6, STP, VLAN)."),
            ("Promiscuous Mode (`IFF_PROMISC`)", "Instructs the NIC hardware to disable MAC address filtering and deliver all overheard frames on the physical wire to the OS.")
        ],
        "Used by network diagnostic tools like Wireshark, tcpdump, and custom IDS packet analysis engines."
    )
    
    create_exam_booster_slide(
        prs, "M3.9", "Linux Raw Sockets", "K3 Apply",
        [
            "Explain the difference between standard Berkeley sockets (`AF_INET`) and Linux packet sockets (`AF_PACKET`). (6 Marks)",
            "Write a C program using `PF_PACKET` and `SOCK_RAW` to capture Ethernet frames and extract Source and Destination MAC addresses. (8 Marks)"
        ],
        [
            "`AF_PACKET` gives direct access to Layer 2 raw Ethernet frames.",
            "Promiscuous mode captures all frames on the shared link regardless of destination MAC.",
            "`ETH_P_ALL` captures all Layer 3 protocol payloads."
        ]
    )
    return prs

def build_module_3_master(prs=None):
    """Builds the comprehensive master deck combining all Module 3 topics."""
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "MODULE 3 MASTER DECK", "Data Link Layer, MAC Protocols & Wireless LANs",
        "Complete Lecture Slides for KTU PCCST501 Computer Networks | Topics M3.1 through M3.9",
        "Module 3 Master"
    )
    build_m3_1(prs)
    build_m3_2(prs)
    build_m3_3(prs)
    build_m3_4(prs)
    build_m3_5(prs)
    build_m3_5v(prs)
    build_m3_6(prs)
    build_m3_7(prs)
    build_m3_8(prs)
    build_m3_9(prs)
    return prs
