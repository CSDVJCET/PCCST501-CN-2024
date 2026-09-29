"""
ppts_module3.py
Topic-wise slide deck builders for Module 3: Data Link Layer, MAC Protocols & Wireless LANs
Author: Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
"""

from generate_comprehensive_ppts import (
    init_prs, create_title_slide, create_content_slide, create_comparison_slide
)

def build_m3_1(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.1", "Data Link Layer & Framing Techniques",
        "Node-to-Node Delivery, Character Count, Byte Stuffing with Escape Characters & Bit Stuffing with Flags",
        "Module 3"
    )
    
    create_content_slide(prs, "3.1.1 Data Link Layer Role & Framing", "M3.1 FRAMING CONCEPTS", [
        ("Node-to-Node Delivery", "Data Link Layer encapsulates Network Layer datagrams into hardware Frames and delivers them across a single physical link between adjacent nodes."),
        ("Framing Concept", "Dividing the raw bit stream from the Physical Layer into discrete, manageable data units (frames) with identifiable boundaries."),
        ("Character Count Method", "Frame header includes a field specifying total number of characters in the frame. Flaw: If a transmission error corrupts the count field, sender and receiver lose synchronization permanently!"),
        ("Byte Stuffing (Character-Oriented)", "Frame delimited by special flag bytes (e.g. `FLAG` = `0x7E`). Whenever `FLAG` or `ESC` occurs in payload data, sender inserts an escape byte (`ESC` = `0x1B`) before it. Receiver removes `ESC`."),
        ("Bit Stuffing (Bit-Oriented - HDLC/PPP)", "Frame delimited by special flag pattern `01111110` (six consecutive 1s). Whenever sender detects FIVE consecutive 1s in payload, it automatically stuffs a '0' bit. Receiver strips the stuffed '0' after five 1s.")
    ], "Bit Stuffing Rule", [
        "Flag: 01111110 (6 ones)",
        "Sender: Stuffs '0' after 5 ones",
        "Example Data: 01111110",
        "Transmitted: 011111010",
        "Receiver: Strips '0' after 5 ones"
    ])
    
    return prs

def build_m3_2(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.2", "Error Control & Flow Control in Data Link Layer",
        "CRC-32 Modulo-2 Polynomial Division, Hamming (7,4) Error Correction, Stop-and-Wait, Go-Back-N & Selective Repeat",
        "Module 3"
    )
    
    create_content_slide(prs, "3.2.1 Error Detection: Cyclic Redundancy Check (CRC)", "M3.2 CRC POLYNOMIAL", [
        ("CRC Concept", "Powerful polynomial-based error detection method based on binary Modulo-2 division (XOR operations without carry)."),
        ("Generator Polynomial $G(x)$", "Agreed polynomial of degree $r$ (represented as an $(r+1)$-bit divisor). E.g., CRC-32 has $r=32$ bits."),
        ("Sender FCS Generation", "Append $r$ zeros to the data block $D$. Perform Modulo-2 division of $D \\cdot 2^r$ by divisor $G$. The remainder $R$ (of length $r$ bits) is the Frame Check Sequence (FCS). Frame sent is $T = D \\cdot 2^r \\oplus R$."),
        ("Receiver Verification", "Receiver divides arriving frame $T$ by divisor $G$. If remainder is EXACTLY ZERO, frame is accepted as error-free; otherwise discarded."),
        ("Error Detection Strength", "Detects all single-bit errors, all double errors, all odd numbers of bit errors, and all burst errors of length $\\le r$.")
    ], "CRC Algorithm Steps", [
        "1. Let divisor G have length k",
        "2. Append (k - 1) zeros to Data",
        "3. Divide using XOR Modulo-2",
        "4. Remainder = FCS (Checksum)",
        "5. Transmit Data + FCS",
        "6. Receiver Remainder must be 0"
    ])
    
    create_content_slide(prs, "3.2.2 Error Correction: Hamming Code (7,4)", "M3.2 HAMMING CODE", [
        ("Hamming Distance ($d_{min}$)", "To detect $e$ errors, minimum Hamming distance must be $d_{min} \\ge e + 1$. To correct $t$ errors, $d_{min} \\ge 2t + 1$."),
        ("Hamming (7,4) Code Structure", "Transmits 4 data bits ($d_1, d_2, d_3, d_4$) with 3 parity check bits ($p_1, p_2, p_3$) at power-of-2 positions ($1, 2, 4$). Total codeword = 7 bits."),
        ("Parity Bit Assignment (Even Parity)", "$p_1$ checks bits (1, 3, 5, 7); $p_2$ checks bits (2, 3, 6, 7); $p_4$ checks bits (4, 5, 6, 7)."),
        ("Syndrome Word Calculation", "Receiver calculates syndrome bits $s_3 s_2 s_1$. If syndrome is `000`, no error occurred. If syndrome equals binary integer $k$ ($1 \\le k \\le 7$), bit position $k$ is inverted and corrected!")
    ], "Hamming Key Rules", [
        "Parity bit positions: 1, 2, 4, 8...",
        "Parity bits formula: 2^p >= m + p + 1",
        "Syndrome indicates exact bit error position",
        "Detects 2-bit, corrects 1-bit errors"
    ])
    
    create_comparison_slide(prs, "3.2.3 Sliding Window Flow Control: Stop-and-Wait vs GBN vs SR", "M3.2 ARQ PROTOCOLS",
        "Go-Back-N ARQ (GBN)", [
            ("Sender Window", "Size $N > 1$; unacked frames inflight"),
            ("Receiver Window", "Size = 1; accepts frames strictly in-order"),
            ("On Out-of-Order Frame", "Discards frame and re-sends ACK for last in-order frame"),
            ("On Timeout", "Retransmits ALL $N$ unacknowledged frames"),
            ("Sequence Numbers", "Requires sequence numbers $\\ge N + 1$")
        ],
        "Selective Repeat ARQ (SR)", [
            ("Sender Window", "Size $N > 1$"),
            ("Receiver Window", "Size $N > 1$; buffers out-of-order frames"),
            ("On Damaged Frame", "Sends Negative ACK (NAK) or waits for timeout"),
            ("On Timeout", "Retransmits ONLY the specific damaged/lost frame"),
            ("Sequence Numbers", "Requires sequence numbers $\\ge 2N$")
        ]
    )
    
    return prs

def build_m3_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.3", "Multiple Access Protocols (MAC)",
        "Random Access (ALOHA, CSMA/CD, CSMA/CA), Controlled Access (Polling, Token Ring) & Channelization (CDMA)",
        "Module 3"
    )
    
    create_comparison_slide(prs, "3.3.1 Random Access: Pure ALOHA vs Slotted ALOHA", "M3.3 ALOHA PROTOCOLS",
        "Pure ALOHA (Abramson, 1970)", [
            ("Transmission Rule", "Nodes transmit frames immediately whenever data is ready"),
            ("Vulnerable Period", "$2 \\times T_{frame}$ (collision if any other node transmits within $\\pm T_{frame}$)"),
            ("Throughput Equation", "$S = G \\cdot e^{-2G}$ (where $G$ is traffic load)"),
            ("Maximum Throughput", "$S_{max} = \\frac{1}{2e} \\approx 18.4\\%$ (achieved at $G = 0.5$)")
        ],
        "Slotted ALOHA (Roberts, 1972)", [
            ("Transmission Rule", "Time divided into synchronized slots ($T_{slot} = T_{frame}$). Nodes transmit only at slot boundary"),
            ("Vulnerable Period", "$1 \\times T_{frame}$ (halved compared to Pure ALOHA)"),
            ("Throughput Equation", "$S = G \\cdot e^{-G}$"),
            ("Maximum Throughput", "$S_{max} = \\frac{1}{e} \\approx 36.8\\%$ (achieved at $G = 1.0$)")
        ]
    )
    
    create_content_slide(prs, "3.3.2 CSMA/CD (Carrier Sense Multiple Access with Collision Detection)", "M3.3 CSMA/CD", [
        ("Carrier Sensing", "Listen Before Talk: Station senses channel before transmitting (1-persistent: transmits immediately when idle; Non-persistent: waits random delay if busy; p-persistent: transmits with probability $p$)."),
        ("Collision Detection (Listen While Talk)", "Station monitors signal energy while transmitting. If signal energy exceeds normal threshold, collision detected $\\implies$ abort immediately and transmit a 32-bit Jam Signal."),
        ("Binary Exponential Backoff Algorithm", "After $n$-th collision ($1 \\le n \\le 10$), choose random slot delay $k \\in [0, 2^n - 1]$. Wait time $= k \\times 51.2\\,\\mu\\text{s}$. Abort if $n = 16$."),
        ("Minimum Frame Size Condition", "Sender must transmit for at least $2 \\times T_{prop}$ to detect collisions before transmission finishes: $T_{trans} \\ge 2 \\times T_{prop} \\implies L_{min} = 2 \\times T_{prop} \\times \\text{Bandwidth}$ (64 Bytes in 10 Mbps Ethernet).")
    ], "CSMA/CD Key Formulas", [
        "Backoff Range: k in [0, 2^n - 1]",
        "Slot Time: 51.2 microseconds",
        "Min Frame Length = 2 * d_prop * Rate",
        "Standard Ethernet Min Frame = 64 Bytes",
        "Jam Signal: 32 to 48 bits"
    ])
    
    create_content_slide(prs, "3.3.3 Channelization & CDMA (Code Division Multiple Access)", "M3.3 CHANNELIZATION", [
        ("Channelization Principles", "Shared bandwidth divided among stations: FDMA (Frequency bands), TDMA (Time slots), and CDMA (Orthogonal Codes)."),
        ("CDMA Fundamentals", "All stations transmit simultaneously across the entire frequency band. Signals are separated using orthogonal chip sequences."),
        ("Orthogonal Chip Sequences (Walsh Codes)", "Each station is assigned an $N$-bit orthogonal chip code $C_i$ where $C_i \\cdot C_j = 0$ (if $i \\neq j$) and $C_i \\cdot C_i = 1$."),
        ("CDMA Encoding", "To send bit 1: transmit code $C_i$. To send bit 0: transmit inverse $-C_i$. If silent: transmit 0."),
        ("CDMA Decoding", "Receiver multiplies composite incoming signal $S$ by desired station's code $C_i$: $S \\cdot C_i = (d_1 C_1 + d_2 C_2 + \\dots) \\cdot C_i = d_i (C_i \\cdot C_i) = d_i$. All other signals cancel to 0!")
    ], "CDMA Properties", [
        "Inner Product: Ci * Cj = 0 (i != j)",
        "Self Product: Ci * Ci = 1",
        "Immune to interference & jamming",
        "Used in 3G mobile networks & GPS"
    ])
    
    return prs

def build_m3_4(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.4", "Link Layer Addressing & Address Resolution Protocol (ARP)",
        "48-Bit IEEE MAC Addresses, OUI Vendor Allocation, ARP Query & Reply Protocol Mechanism",
        "Module 3"
    )
    
    create_content_slide(prs, "3.4.1 MAC Addressing Architecture", "M3.4 MAC ADDRESSES", [
        ("48-Bit Physical Address (6 Bytes)", "Burned into the Network Interface Card (NIC) ROM. Represented as 12 hexadecimal digits: `00:1A:2B:3C:4D:5E`."),
        ("Organizationally Unique Identifier (OUI - First 24 bits)", "Assigned by IEEE to the hardware manufacturer (e.g. Intel, Cisco, Apple)."),
        ("NIC Serial Number (Last 24 bits)", "Assigned uniquely by manufacturer to individual network interfaces."),
        ("Broadcast MAC Address", "`FF:FF:FF:FF:FF:FF` (all 48 bits are 1s). Processed by every adapter on the local LAN broadcast domain."),
        ("Multicast MAC Address", "Least Significant Bit of first byte is 1 (e.g. `01:00:5E:xx:xx:xx` for IPv4 multicast).")
    ], "MAC Address Structure", [
        "First 3 Bytes (24b): OUI Vendor ID",
        "Last 3 Bytes (24b): Device Serial",
        "Unicast: 00:1A:2B:3C:4D:5E",
        "Broadcast: FF:FF:FF:FF:FF:FF",
        "Flat physical addressing"
    ])
    
    create_content_slide(prs, "3.4.2 Address Resolution Protocol (ARP)", "M3.4 ARP OPERATION", [
        ("ARP Purpose", "Dynamically translates a known 32-bit IP address into its corresponding 48-bit MAC address on the same local subnet."),
        ("ARP Request (Broadcast)", "Sender broadcasts an Ethernet frame (`Dst MAC = FF:FF:FF:FF:FF:FF`) asking: 'Who has IP `192.168.1.5`? Tell `192.168.1.1`'."),
        ("ARP Reply (Unicast)", "The host with target IP `192.168.1.5` responds with a unicast frame directly to sender's MAC containing its physical address."),
        ("ARP Cache Table", "Sender caches the `(IP, MAC, TTL)` mapping (typically for 20 minutes) to eliminate redundant broadcasts for future packets."),
        ("Gratuitous ARP & Proxy ARP", "Gratuitous ARP: Host announces its own IP/MAC on boot to detect IP address conflicts. Proxy ARP: Router responds on behalf of remote hosts.")
    ], "ARP Protocol Flow", [
        "1. ARP Request -> Broadcast (FF:..:FF)",
        "2. Target Host -> Unicast ARP Reply",
        "3. Host stores in ARP Cache Table",
        "4. Cache expires after TTL (20 min)",
        "Gratuitous ARP: Detects IP conflicts"
    ])
    
    return prs

def build_m3_5(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.5", "Ethernet Protocols (IEEE 802.3)",
        "Standard Ethernet (10BASE-T), Fast Ethernet, Gigabit Ethernet, 10GbE, Frame Format & MTU",
        "Module 3"
    )
    
    create_content_slide(prs, "3.5.1 IEEE 802.3 Ethernet Frame Format", "M3.5 ETHERNET FRAME", [
        ("Preamble (7 Bytes)", "Alternating `10101010` pattern for receiver clock synchronization."),
        ("Start of Frame Delimiter (SFD - 1 Byte)", "`10101011` pattern signaling start of valid frame data."),
        ("Destination MAC (6 Bytes) & Source MAC (6 Bytes)", "48-bit physical hardware addresses of receiver and sender."),
        ("Type / Length Field (2 Bytes)", "If $\\ge 1536$ (`0x0600`), specifies upper layer protocol (`0x0800` for IPv4, `0x0806` for ARP). If $\\le 1500$, specifies payload byte length."),
        ("Data Payload (46 to 1500 Bytes)", "Minimum 46 bytes (padded with zeros if smaller to meet 64B frame minimum) and Maximum 1500 bytes (MTU)."),
        ("CRC-32 FCS Trailer (4 Bytes)", "Cyclic Redundancy Check trailer verifying frame integrity.")
    ], "Frame Size Limits", [
        "Min Frame Size: 64 Bytes",
        "Max Frame Size: 1518 Bytes",
        "Min Payload: 46 Bytes",
        "Max Payload (MTU): 1500 Bytes",
        "Preamble + SFD = 8 Bytes"
    ])
    
    create_comparison_slide(prs, "3.5.2 High-Speed Ethernet Standards Evolution", "M3.5 ETHERNET EVOLUTION",
        "Standard & Fast Ethernet", [
            ("Standard Ethernet (10BASE-T)", "10 Mbps, Cat 3/5 UTP, Manchester encoding, Hub topology, CSMA/CD half-duplex"),
            ("Fast Ethernet (100BASE-TX)", "100 Mbps, Cat 5 UTP (2 pairs), 4B/5B + MLT-3 line encoding, Switch full-duplex"),
            ("100BASE-FX", "100 Mbps over Multi-mode Optical Fiber (2 km reach)")
        ],
        "Gigabit & 10G Ethernet", [
            ("Gigabit Ethernet (1000BASE-T)", "1000 Mbps (1 Gbps), Cat 5e/6 UTP (all 4 pairs simultaneous bidirectional), 4D-PAM5 encoding"),
            ("1000BASE-SX / LX", "1 Gbps over Short-wavelength / Long-wavelength Optical Fiber"),
            ("10-Gigabit Ethernet (802.3ae)", "10 Gbps, Optical Fiber & Cat 6A UTP; Full-duplex only (CSMA/CD disabled!)")
        ]
    )
    
    return prs

def build_m3_5v(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.5V", "Virtual LANs (VLAN - IEEE 802.1Q)",
        "Broadcast Domain Segmentation, IEEE 802.1Q Frame Tagging, Trunk Ports vs Access Ports & Inter-VLAN Routing",
        "Module 3"
    )
    
    create_content_slide(prs, "3.5V.1 VLAN Motivation & IEEE 802.1Q Tagging", "M3.5V VLAN ARCHITECTURE", [
        ("VLAN Concept", "Logically segments a single physical switch infrastructure into multiple isolated broadcast domains, improving security, traffic management, and bandwidth efficiency."),
        ("Access Ports vs Trunk Ports", "Access Ports: Connect to end devices (PCs, printers); belong to a single VLAN and carry standard untagged Ethernet frames. Trunk Ports: Connect switch-to-switch or switch-to-router; carry multiplexed traffic for multiple VLANs using 802.1Q tags."),
        ("IEEE 802.1Q Tag (4 Bytes)", "Inserted between Source MAC and Type/Length fields of standard Ethernet frame."),
        ("Tag Fields", "TPID (Tag Protocol ID: 16b = `0x8100`), Priority Code Point (PCP: 3b QoS), DEI (Drop Eligible: 1b), and VLAN ID (VID: 12 bits = 4094 possible VLANs).")
    ], "802.1Q Tag Format", [
        "Tag Size: 4 Bytes (32 bits)",
        "TPID: 0x8100 (16 bits)",
        "Priority (PCP): 3 bits (802.1p)",
        "VLAN ID: 12 bits (1 to 4094)",
        "Trunking: Carries tagged traffic"
    ])
    
    create_content_slide(prs, "3.5V.2 Inter-VLAN Routing Architectures", "M3.5V INTER-VLAN ROUTING", [
        ("Need for Layer 3 Routing", "Hosts in different VLANs cannot communicate at Layer 2 even if connected to the same physical switch. Communication requires a Layer 3 routing device."),
        ("Router-on-a-Stick (ROAS)", "Single physical router interface connected to switch trunk port. Divided into logical sub-interfaces (e.g. `eth0.10`, `eth0.20`), each configured with the default gateway IP for its respective VLAN."),
        ("Layer 3 Switches (Multilayer Switching)", "High-performance switch with built-in hardware ASIC IP routing. Switch Virtual Interfaces (SVIs: `interface vlan 10`) provide wirespeed line-rate Inter-VLAN forwarding without external router bottlenecks.")
    ], "Inter-VLAN Methods", [
        "Legacy: Dedicated router port per VLAN",
        "Router-on-a-Stick: 802.1Q sub-interfaces",
        "Layer 3 Switch: SVI hardware routing",
        "Separates broadcast, secures subnets"
    ])
    
    return prs

def build_m3_6(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.6", "Connecting Devices & Domain Segmentation",
        "Repeaters, Hubs, Bridges, Layer 2 Learning Switches, Routers & Collision vs Broadcast Domain Analysis",
        "Module 3"
    )
    
    create_content_slide(prs, "3.6.1 Connecting Devices Classification", "M3.6 CONNECTING DEVICES", [
        ("Physical Layer (L1): Repeaters & Hubs", "Regenerate/amplify electrical signals and broadcast bits to all ports. Single Collision Domain & Single Broadcast Domain."),
        ("Data Link Layer (L2): Bridges & Switches", "Forward frames based on 48-bit MAC address tables. Break network into separate Collision Domains per port while maintaining a Single Broadcast Domain."),
        ("Learning Switch Algorithm", "Switch inspects Source MAC of incoming frame to update `(MAC, Port, TTL)` table. If Destination MAC is in table $\\implies$ selective forward to specific port; if destination unknown/broadcast $\\implies$ flood to all ports except incoming."),
        ("Network Layer (L3): Routers", "Forward packets based on 32-bit/128-bit IP addresses. Break network into separate Collision Domains AND separate Broadcast Domains.")
    ], "Device Hierarchy", [
        "L1 Hub: Bit repeater (dumb)",
        "L2 Switch: Frame filter (MAC)",
        "L3 Router: Packet forwarder (IP)",
        "L7 Gateway: Protocol translation"
    ])
    
    create_comparison_slide(prs, "3.6.2 Collision Domains vs Broadcast Domains Matrix", "M3.6 DOMAIN ANALYSIS",
        "Collision Domain", [
            ("Definition", "Network segment where simultaneous transmissions cause physical signal collision"),
            ("Hub / Repeater", "Entire hub is 1 single collision domain"),
            ("Layer 2 Switch", "Each individual switch port is an isolated collision domain ($N$ ports = $N$ domains)"),
            ("Router", "Each router interface is an isolated collision domain"),
            ("Full-Duplex Switch", "Zero collisions occur in full-duplex switch links!")
        ],
        "Broadcast Domain", [
            ("Definition", "Network segment reached by an L2 broadcast frame (`FF:FF:FF:FF:FF:FF`)"),
            ("Hub / Switch", "All connected ports belong to 1 single broadcast domain"),
            ("Switch with VLANs", "Each configured VLAN forms an isolated broadcast domain ($M$ VLANs = $M$ domains)"),
            ("Router", "Routers block L2 broadcasts by default; each router interface is a separate broadcast domain")
        ]
    )
    
    return prs

def build_m3_7(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.7", "Wireless LANs (IEEE 802.11 Wi-Fi)",
        "Architecture (BSS, ESS, AP), CSMA/CA Protocol, NAV, IFS, Hidden/Exposed Terminals, RTS/CTS & Wi-Fi Standards",
        "Module 3"
    )
    
    create_content_slide(prs, "3.7.1 IEEE 802.11 Wi-Fi Architecture", "M3.7 802.11 ARCHITECTURE", [
        ("Basic Service Set (BSS)", "Building block of 802.11. Consists of wireless stations. Infrastructure BSS includes a central Access Point (AP); Ad-hoc / IBSS has peer-to-peer communication without an AP."),
        ("Extended Service Set (ESS)", "Two or more BSSs interconnected by a wired Distribution System (DS / Ethernet switch backbone) sharing a common SSID, enabling seamless mobile client roaming."),
        ("Service Set Identifier (SSID)", "Human-readable name of the wireless network (up to 32 characters) advertised in Periodic Beacon frames by APs."),
        ("BSSID", "The 48-bit MAC address of the Access Point's wireless radio interface.")
    ], "Wi-Fi Topologies", [
        "Infrastructure Mode: With AP",
        "Ad-hoc Mode: Peer-to-peer (IBSS)",
        "ESS: Multiple APs on wired DS",
        "SSID: Network broadcast name",
        "BSSID: 48-bit AP MAC address"
    ])
    
    create_content_slide(prs, "3.7.2 CSMA/CA & Inter-Frame Spaces (IFS)", "M3.7 CSMA/CA & IFS", [
        ("Why CSMA/CD Fails in Wireless", "1. Wireless radios cannot transmit and receive simultaneously on same channel (half-duplex). 2. Signal attenuation makes collision detection impossible at sender $\\implies$ Wi-Fi uses Collision AVOIDANCE (CSMA/CA)."),
        ("CSMA/CA Protocol Flow", "Station senses medium. If idle for DIFS, it selects random backoff slot count. Decrements counter while medium idle. Transmits when counter reaches 0. Receiver sends ACK after SIFS."),
        ("Inter-Frame Spaces (IFS Hierarchy)", "SIFS (Short IFS - highest priority for ACKs/CTS) < PIFS (PCF IFS) < DIFS (DCF IFS - standard data frames)."),
        ("Network Allocation Vector (NAV)", "Virtual carrier sensing. Frames carry a `Duration` field. Stations hearing duration set their internal NAV timer and refrain from transmitting until NAV expires.")
    ], "IFS Priority Hierarchy", [
        "1. SIFS: Lowest delay (ACK / CTS)",
        "2. PIFS: Medium delay (Polling)",
        "3. DIFS: Highest delay (Data frames)",
        "NAV: Virtual countdown timer",
        "Exponential Contention Window"
    ])
    
    create_comparison_slide(prs, "3.7.3 Hidden vs Exposed Terminals & RTS/CTS Handshake", "M3.7 RTS/CTS MECHANISM",
        "Hidden Terminal Problem (Solved by RTS/CTS)", [
            ("Scenario", "Station A and C both communicate with AP B, but A and C cannot hear each other"),
            ("Problem", "Simultaneous transmissions from A and C collide at B"),
            ("Solution", "A sends RTS $\\to$ B replies with CTS (heard by C) $\\to$ C sets NAV and stays silent"),
            ("Handshake", "RTS (20B) $\\to$ CTS (14B) $\\to$ DATA $\\to$ ACK")
        ],
        "Exposed Terminal Problem", [
            ("Scenario", "B transmits to A; C wants to transmit to D (outside B's range)"),
            ("Problem", "C senses carrier from B and unnecessarily delays transmitting to D even though no collision would occur at A"),
            ("Resolution", "Directional antennas or spatial reuse techniques in modern Wi-Fi 6 (BSS Coloring)")
        ]
    )
    
    return prs

def build_m3_8(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.8", "Mobile IP Architecture",
        "Entities (MN, HA, FA), Home Address vs Care-of Address, Agent Discovery, Triangle Routing & Route Optimization",
        "Module 3"
    )
    
    create_content_slide(prs, "3.8.1 Mobile IP Entities & Addressing", "M3.8 MOBILE IP ENTITIES", [
        ("Mobile IP (RFC 5944)", "Allows mobile devices (Mobile Nodes) to change their point of attachment to the Internet without changing their static IP address, preserving active TCP connections."),
        ("Mobile Node (MN)", "End system that moves across subnets (e.g. smartphone moving between Wi-Fi and 5G)."),
        ("Home Agent (HA)", "Router on the Mobile Node's home network that tunnels packets to the MN when it is away from home."),
        ("Foreign Agent (FA)", "Router on the visited foreign network that assists the MN in receiving packets and provides a Care-of Address (COA)."),
        ("Two IP Addresses", "Permanent Home Address (static IP identifying MN) and Temporary Care-of Address (COA identifying current location).")
    ], "Mobile IP Terminology", [
        "MN: Mobile Node",
        "HA: Home Agent router",
        "FA: Foreign Agent router",
        "Home Address: Permanent static IP",
        "COA: Temporary location address"
    ])
    
    create_content_slide(prs, "3.8.2 Triangle Routing & Encapsulation Tunneling", "M3.8 TRIANGLE ROUTING", [
        ("Agent Discovery & Registration", "Foreign Agents broadcast periodic Agent Advertisements. MN registers its new COA with Home Agent via Registration Request."),
        ("Triangle Routing Mechanism", "1. Correspondent Node (CN) sends packet to MN's Home Address. 2. Home Agent intercepts packet. 3. HA encapsulates packet inside a new IP header (`Dst = COA`) [IP-in-IP Tunneling]. 4. FA decapsulates packet and delivers to MN. 5. MN replies directly to CN."),
        ("Inefficiency of Triangle Routing", "Packets travel an indirect triangular path through the Home Agent even if CN and MN are on adjacent networks, adding propagation delay."),
        ("Route Optimization Solution", "HA sends a Binding Update to CN containing MN's current COA, allowing CN to tunnel future packets directly to MN's COA.")
    ], "Key Takeaways", [
        "IP-in-IP Encapsulation Tunneling",
        "Triangle Path: CN -> HA -> FA -> MN",
        "Direct Reply: MN -> CN",
        "Binding Update: Eliminates triangle"
    ])
    
    return prs

def build_m3_9(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M3.9", "Linux Raw Socket Link Layer Programming",
        "Datalink Provider Interface, SOCK_PACKET vs PF_PACKET, struct sockaddr_ll & Custom Frame Sniffing",
        "Module 3"
    )
    
    create_content_slide(prs, "3.9.1 Linux Raw Sockets & PF_PACKET Interface", "M3.9 LINUX RAW SOCKETS", [
        ("Link-Layer Direct Access", "Standard sockets operate at L4/L3. Link-layer raw sockets allow application programs to send and receive raw L2 Ethernet frames directly bypassing kernel IP stack."),
        ("Legacy `SOCK_PACKET` vs Modern `PF_PACKET`", "`SOCK_PACKET` (Linux 2.0) passed device name in `sockaddr`. Replaced in modern Linux by `socket(PF_PACKET, SOCK_RAW, htons(ETH_P_ALL))` which provides cleaner device binding and hardware header access."),
        ("`struct sockaddr_ll` Structure", "Socket address struct for link layer: `sll_family = AF_PACKET`, `sll_protocol = htons(ETH_P_ALL)`, `sll_ifindex` (interface index), `sll_hatype` (ARP hardware type), `sll_addr` (MAC address bytes)."),
        ("Promiscuous Mode Sniffing", "NIC configured with `IFF_PROMISC` flag captures ALL frames traversing the physical wire regardless of Destination MAC (used by Wireshark/tcpdump).")
    ], "Hands-on Code Snip", [
        "s = socket(PF_PACKET, SOCK_RAW, htons(ETH_P_ALL));",
        "recvfrom(s, buffer, 2048, 0, NULL, NULL);",
        "struct ethhdr *eth = (struct ethhdr*)buffer;",
        "All KTU CO4 Topics Covered"
    ])
    
    return prs

def build_module_3_master(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "MODULE 3", "Data Link Layer, MAC Protocols & Wireless LANs",
        "Complete Lecture & Revision Master Deck (M3.1 to M3.9)",
        "Module 3 Complete"
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
