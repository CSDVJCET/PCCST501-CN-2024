"""
ppts_module2.py
Topic-wise slide deck builders for Module 2: Transport & Network Layers with Linux Kernel Architecture
Author: Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
"""

from generate_comprehensive_ppts import (
    init_prs, create_title_slide, create_content_slide, create_comparison_slide
)

def build_m2_1_1(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.1.1", "Transport Layer Services & Principles",
        "Process-to-Process Logical Communication, Port Addressing Hierarchy, Multiplexing & Demultiplexing",
        "Module 2"
    )
    
    create_content_slide(prs, "2.1.1.1 Transport Layer Role & Port Addressing", "M2.1.1 TL SERVICES", [
        ("Process-to-Process Delivery", "While the Network Layer provides host-to-host delivery between IP addresses, the Transport Layer provides logical communication between application processes running on those hosts."),
        ("16-Bit Port Numbers (0 to 65535)", "Used to identify specific application processes running on an operating system."),
        ("Well-Known Ports (0 - 1023)", "Assigned by IANA for standard server services (e.g., HTTP: 80, HTTPS: 443, FTP: 21, SSH: 22, DNS: 53, SMTP: 25). Requires root/admin privilege to bind."),
        ("Registered Ports (1024 - 49151)", "Used by vendor applications (e.g. MySQL: 3306, PostgreSQL: 5432, Redis: 6379)."),
        ("Dynamic / Ephemeral Ports (49152 - 65535)", "Assigned automatically by the client operating system kernel for short-lived client-side connection endpoints.")
    ], "Port Ranges", [
        "Well-Known: 0 to 1023",
        "Registered: 1024 to 49151",
        "Dynamic/Private: 49152 to 65535",
        "Socket = IP Address + Port Number"
    ])
    
    create_comparison_slide(prs, "2.1.1.2 Multiplexing & Demultiplexing Mechanisms", "M2.1.1 MUX & DEMUX",
        "Connectionless Demux (UDP)", [
            ("Identifier", "2-Tuple: `(Destination IP, Destination Port)`"),
            ("Behavior", "Packets from different source IPs/Ports targeting the same Dest IP/Port go to the SAME socket"),
            ("Overhead", "Lightweight, zero connection state maintained by kernel"),
            ("Use Case", "DNS queries, SNMP traps, video broadcasting")
        ],
        "Connection-Oriented Demux (TCP)", [
            ("Identifier", "4-Tuple: `(Src IP, Src Port, Dst IP, Dst Port)`"),
            ("Behavior", "Each concurrent client connection gets a UNIQUE dedicated socket returned by `accept()`"),
            ("Overhead", "Kernel maintains dedicated buffers & state variables per connection"),
            ("Use Case", "Web browsing, secure shell, file transfers")
        ]
    )
    
    return prs

def build_m2_1_2(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.1.2", "User Datagram Protocol (UDP)",
        "Connectionless Transport, 8-Byte Minimal Header, 1's Complement Checksum Calculation with Pseudo-Header",
        "Module 2"
    )
    
    create_content_slide(prs, "2.1.2.1 UDP Characteristics & 8-Byte Header Structure", "M2.1.2 UDP PROTOCOL", [
        ("Core Characteristics", "Connectionless, unreliable, best-effort message-oriented service. No handshaking delay, no congestion control throttling, minimal header overhead."),
        ("Source Port (16 bits)", "Identifies sending process (optional; set to 0 if no reply expected)."),
        ("Destination Port (16 bits)", "Identifies receiving application process on target host."),
        ("Length (16 bits)", "Total length of UDP datagram in bytes (Header [8 bytes] + Payload). Minimum value is 8 bytes."),
        ("Checksum (16 bits)", "Used for error detection across pseudo-header, UDP header, and payload. Optional in IPv4 (0 if unused), mandatory in IPv6.")
    ], "UDP Header (8 Bytes)", [
        "0-15: Source Port (16b)",
        "16-31: Destination Port (16b)",
        "32-47: Total Length (16b)",
        "48-63: Checksum (16b)",
        "Followed immediately by Payload"
    ])
    
    create_content_slide(prs, "2.1.2.2 UDP Checksum Calculation with Pseudo-Header", "M2.1.2 UDP CHECKSUM", [
        ("The Pseudo-Header Concept", "To detect misrouted packets, UDP computes checksum over a 12-byte temporary IP Pseudo-Header + 8-byte UDP header + payload."),
        ("Pseudo-Header Fields", "Source IP (32b), Destination IP (32b), All Zeros (8b), Protocol Number (8b: `17` for UDP), UDP Length (16b)."),
        ("1's Complement Addition Algorithm", "Data divided into 16-bit words. All 16-bit words are added together using 1's complement arithmetic (any carry-out bit is wrapped around and added back to LSB)."),
        ("Checksum Inversion", "The bitwise NOT (1's complement inverse) of the final sum is placed into the Checksum field."),
        ("Receiver Verification", "Receiver sums all 16-bit words (including the checksum). If no errors occurred, the resulting 16-bit sum MUST be all 1s (`0xFFFF`).")
    ], "Checksum Algorithm", [
        "1. Pad odd payload with 0x00",
        "2. Add 16-bit words with carry wrap",
        "3. Checksum = ~Sum (bitwise NOT)",
        "4. Receiver Sum + Checksum = 0xFFFF",
        "5. If not 0xFFFF -> Packet Corrupted!"
    ])
    
    return prs

def build_m2_1_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.1.3", "Transmission Control Protocol (TCP) Architecture",
        "Stream-Oriented Full-Duplex Model, TCP Segment Header, 3-Way Handshake Connection Setup & 4-Way Teardown",
        "Module 2"
    )
    
    create_content_slide(prs, "2.1.3.1 TCP Characteristics & Segment Header Format", "M2.1.3 TCP HEADER", [
        ("TCP Characteristics", "Connection-oriented, reliable byte-stream, full-duplex, point-to-point, flow-controlled, congestion-controlled."),
        ("Sequence Number (32 bits)", "Byte-stream number of the first data byte in this segment (relative to Initial Sequence Number ISN)."),
        ("Acknowledgment Number (32 bits)", "Cumulative ACK: The next byte number the sender expects to receive. Acknowledges all prior bytes."),
        ("Header Length / Data Offset (4 bits)", "Specifies header length in 32-bit (4-byte) words (Range: 5 to 15 words = 20 to 60 bytes)."),
        ("Control Flags (6 bits)", "URG (Urgent pointer valid), ACK (Ack number valid), PSH (Push data immediately), RST (Reset connection), SYN (Synchronize sequence numbers during handshake), FIN (Terminate connection)."),
        ("Receive Window `rwnd` (16 bits)", "Number of bytes receiver is willing to accept (Flow Control).")
    ], "Header Breakdown", [
        "Base Header: 20 Bytes",
        "Max Options: 40 Bytes",
        "Total Header: 20 to 60 Bytes",
        "Seq No: Byte-level tracking",
        "Ack No: Cumulative next-expected"
    ])
    
    create_comparison_slide(prs, "2.1.3.2 Connection Lifecycle: 3-Way Handshake & 4-Way Teardown", "M2.1.3 HANDSHAKES",
        "3-Way Handshake (Establishment)", [
            ("Step 1 (Client -> Server)", "SYN=1, ACK=0, Seq = client_isn (Requests connection)"),
            ("Step 2 (Server -> Client)", "SYN=1, ACK=1, Seq = server_isn, Ack = client_isn + 1"),
            ("Step 3 (Client -> Server)", "SYN=0, ACK=1, Seq = client_isn + 1, Ack = server_isn + 1 (May piggyback payload)"),
            ("SYN Flood Defense", "SYN Cookies avoid pre-allocating TCB state before ACK")
        ],
        "4-Way Handshake (Termination)", [
            ("Step 1 (Client -> Server)", "FIN=1, Seq = u (Client enters FIN_WAIT_1)"),
            ("Step 2 (Server -> Client)", "ACK=1, Ack = u + 1 (Server enters CLOSE_WAIT; Client enters FIN_WAIT_2)"),
            ("Step 3 (Server -> Client)", "FIN=1, Seq = w (Server enters LAST_ACK)"),
            ("Step 4 (Client -> Server)", "ACK=1, Ack = w + 1 (Client enters TIME_WAIT for 2MSL = 2 minutes)")
        ]
    )
    
    return prs

def build_m2_1_4(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.1.4", "TCP Flow & Congestion Control",
        "Sliding Window Flow Control, rwnd vs cwnd, Slow Start, AIMD, Fast Retransmit, Fast Recovery & Tahoe vs Reno",
        "Module 2"
    )
    
    create_content_slide(prs, "2.1.4.1 Flow Control & Sliding Window", "M2.1.4 FLOW CONTROL", [
        ("Flow Control Goal", "Prevents a fast sender from overflowing the receive buffer of a slow receiver."),
        ("Sliding Window Mechanism", "Receiver advertises its available buffer space in the `Receive Window (rwnd)` header field: $rwnd = RcvBuffer - (LastByteRcvd - LastByteRead)$."),
        ("Sender Constraint", "Sender ensures unacknowledged inflight bytes never exceed $rwnd$: $LastByteSent - LastByteAcked \\le rwnd$."),
        ("Zero-Window Probing", "When $rwnd = 0$, sender pauses data but periodically sends 1-byte probe segments to trigger receiver window update advertisements."),
        ("Silly Window Syndrome", "Sender sends tiny packets (1 byte payload + 40B header) or receiver advertises tiny buffer. Solved by Nagle's Algorithm (sender buffering) and Clark's Solution (receiver delays advertising until MSS space free).")
    ], "Flow Control Terms", [
        "rwnd: Receiver advertised window",
        "Effective Win = min(cwnd, rwnd)",
        "Nagle's: Buffers small packets",
        "Clark's: Avoids advertising tiny rwnd"
    ])
    
    create_content_slide(prs, "2.1.4.2 Congestion Control: Slow Start & AIMD", "M2.1.4 CONGESTION PHASES", [
        ("Congestion Window (`cwnd`)", "Dynamic limit on unacknowledged bytes maintained by sender based on perceived network congestion. Max unacked data $= \\min(cwnd, rwnd)$."),
        ("Slow Start Phase", "Begins with $cwnd = 1 \\text{ MSS}$. cwnd increases by 1 MSS for every ACK received $\\implies$ cwnd DOUBLES every Round Trip Time (RTT) [Exponential Growth]. Continues until $cwnd \\ge ssthresh$ (slow start threshold)."),
        ("Congestion Avoidance (AIMD)", "Additive Increase: $cwnd$ increases by 1 MSS per RTT (linear growth) to probe for bandwidth safely."),
        ("Multiplicative Decrease", "On congestion detection, sender throttles transmission rate aggressively by halving the threshold: $ssthresh = cwnd / 2$.")
    ], "Congestion Formulas", [
        "Slow Start: cwnd *= 2 per RTT",
        "Congestion Avoidance: cwnd += 1 MSS/RTT",
        "Threshold on Loss: ssthresh = cwnd / 2"
    ])
    
    create_comparison_slide(prs, "2.1.4.3 Loss Recovery: TCP Tahoe vs TCP Reno", "M2.1.4 TAHOE VS RENO",
        "TCP Tahoe (Legacy)", [
            ("Timeout Loss", "ssthresh = cwnd / 2; cwnd = 1 MSS; Enters Slow Start"),
            ("3 Duplicate ACKs", "ssthresh = cwnd / 2; cwnd = 1 MSS; Enters Slow Start"),
            ("Fast Retransmit", "Retransmits lost packet immediately upon 3rd duplicate ACK"),
            ("Fast Recovery", "NOT supported (always drops cwnd to 1 MSS)")
        ],
        "TCP Reno (Modern Standard)", [
            ("Timeout Loss", "ssthresh = cwnd / 2; cwnd = 1 MSS; Enters Slow Start"),
            ("3 Duplicate ACKs", "ssthresh = cwnd / 2; cwnd = ssthresh + 3 MSS; Enters Fast Recovery"),
            ("Fast Retransmit", "Retransmits lost segment without waiting for retransmission timer expiry"),
            ("Fast Recovery", "Avoids dropping to 1 MSS; increments cwnd on dup ACKs and returns to Congestion Avoidance upon new ACK")
        ]
    )
    
    return prs

def build_m2_1_5(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.1.5", "Berkeley Socket API & I/O Multiplexing",
        "Socket System Call Lifecycle, TCP/UDP Client-Server Code Architecture, I/O Multiplexing with select() and poll()",
        "Module 2"
    )
    
    create_comparison_slide(prs, "2.1.5.1 TCP vs UDP Socket API Lifecycle", "M2.1.5 SOCKET API",
        "TCP Socket Flow (Stream)", [
            ("Server Sequence", "`socket()` $\\to$ `bind()` $\\to$ `listen()` $\\to$ `accept()` $\\to$ `read()`/`write()` $\\to$ `close()`"),
            ("Client Sequence", "`socket()` $\\to$ `connect()` $\\to$ `write()`/`read()` $\\to$ `close()`"),
            ("`listen(sockfd, backlog)`", "Prepares socket for incoming connections with connection backlog queue limit"),
            ("`accept()`", "Blocks until connection arrives; returns NEW connected socket descriptor for client")
        ],
        "UDP Socket Flow (Datagram)", [
            ("Server Sequence", "`socket()` $\\to$ `bind()` $\\to$ `recvfrom()` $\\to$ `sendto()` $\\to$ `close()`"),
            ("Client Sequence", "`socket()` $\\to$ `sendto()` $\\to$ `recvfrom()` $\\to$ `close()`"),
            ("Connectionless", "No `listen()`, `connect()`, or `accept()` required"),
            ("`recvfrom()` / `sendto()`", "Takes explicit destination `sockaddr_in` struct on every call")
        ]
    )
    
    create_content_slide(prs, "2.1.5.2 I/O Multiplexing: select() & poll() Functions", "M2.1.5 IO MULTIPLEXING", [
        ("Motivation for I/O Multiplexing", "Allows a single-threaded server process to monitor multiple active file/socket descriptors simultaneously without blocking on any single socket or spawning thousands of threads."),
        ("`select()` System Call", "`int select(int maxfdp1, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, struct timeval *timeout)`."),
        ("`fd_set` Bitmask Operations", "`FD_ZERO(&set)`, `FD_SET(fd, &set)`, `FD_CLR(fd, &set)`, `FD_ISSET(fd, &set)`. Limited by `FD_SETSIZE` (typically 1024 descriptors)."),
        ("`poll()` System Call", "`int poll(struct pollfd fds[], nfds_t nfds, int timeout)`. Uses array of structures with event bitmasks (`POLLIN`, `POLLOUT`, `POLLERR`). Eliminates `FD_SETSIZE` descriptor limits."),
        ("Event Notification", "Both calls block until one or more monitored descriptors become ready for I/O reading/writing, waking the main event loop.")
    ], "Key Takeaways", [
        "select(): Bitmasks, 1024 limit",
        "poll(): Array of structs, unlimited",
        "Non-blocking server architecture",
        "Foundation of modern event loops (epoll/nginx/node)"
    ])
    
    return prs

def build_m2_2_1(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.1", "Network Layer Architecture & Delivery",
        "Host-to-Host Packet Delivery, Data Plane vs Control Plane, Forwarding vs Routing, Service Models",
        "Module 2"
    )
    
    create_comparison_slide(prs, "2.2.1.1 Network Layer Core Concepts", "M2.2.1 FORWARDING VS ROUTING",
        "Data Plane: Forwarding (Local)", [
            ("Definition", "Router's local action of transferring arriving packet from input port to correct output port"),
            ("Timescale", "Hardware nanoseconds / microseconds"),
            ("Mechanism", "Forwarding Table lookup using packet destination IP prefix matching (Longest Prefix Match)"),
            ("Implementation", "ASIC hardware / TCAM (Ternary Content Addressable Memory)")
        ],
        "Control Plane: Routing (Network-Wide)", [
            ("Definition", "Network-wide logic determining end-to-end path taken by packets from source to destination"),
            ("Timescale", "Software milliseconds / seconds"),
            ("Mechanism", "Routing algorithms (OSPF, RIP, BGP) computing forwarding table entries"),
            ("Approaches", "Traditional distributed per-router control vs Software Defined Networking (SDN)")
        ]
    )
    
    create_content_slide(prs, "2.2.1.2 Network Layer Service Models", "M2.2.1 SERVICE MODELS", [
        ("Internet Service Model: Best-Effort", "The IP network layer makes no guarantees on packet delivery, no throughput guarantees, no delay bounds, and no in-order delivery assurance."),
        ("Why Best-Effort?", "Simple, highly robust core network design. Intelligence and complexity (reliability, congestion control) pushed to the network edge (hosts/transport layer)."),
        ("Datagram Networks (Internet)", "Connectionless packet forwarding. Each packet carries destination IP address and is routed independently. Stateless routers."),
        ("Virtual Circuit Networks (ATM/X.25)", "Connection-oriented network layer. Requires call setup, per-connection virtual circuit identifiers (VCIs), and stateful switches.")
    ], "Core Summary", [
        "Forwarding: Hardware packet switching",
        "Routing: Path computation algorithms",
        "IP Model: Best-effort datagrams",
        "End-to-End Principle: Smart edge, simple core"
    ])
    
    return prs

def build_m2_2_2(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.2", "Network Layer Protocols: IPv4 & Subnetting",
        "IPv4 Header Format, Subnetting, CIDR Notation, VLSM, ARP, ICMP, DHCP & NAT",
        "Module 2"
    )
    
    create_content_slide(prs, "2.2.2.1 IPv4 Datagram Header Structure", "M2.2.2 IPV4 HEADER", [
        ("Base Header Length", "20 to 60 bytes (minimum 20 bytes when options are absent)."),
        ("Version (4b) & IHL (4b)", "Version 4; Internet Header Length (IHL) in 32-bit words (e.g. 5 = 20 bytes)."),
        ("Type of Service / DiffServ (8b)", "QoS classification and Explicit Congestion Notification (ECN)."),
        ("Total Length (16b)", "Total length of datagram in bytes (Header + Payload). Max 65,535 bytes."),
        ("Fragmentation Fields (32b)", "Identification (16b: groups fragments), Flags (3b: Reserved, DF = Don't Fragment, MF = More Fragments), Fragment Offset (13b: measured in 8-byte units)."),
        ("Time to Live (TTL - 8b)", "Decremented by 1 at each router hop to prevent infinite routing loops. Dropped when TTL = 0 (triggers ICMP Time Exceeded)."),
        ("Protocol (8b) & Checksum (16b)", "Protocol number: `6` for TCP, `17` for UDP, `1` for ICMP. Checksum verified over header only.")
    ], "IPv4 Key Fields", [
        "Base Header: 20 Bytes",
        "TTL: Loop prevention",
        "Protocol 6: TCP | 17: UDP",
        "Offset: Measured in 8-byte blocks",
        "DF=1: Drop if MTU exceeded"
    ])
    
    create_content_slide(prs, "2.2.2.2 Subnetting, CIDR & VLSM Formulas", "M2.2.2 SUBNETTING & CIDR", [
        ("Classless Inter-Domain Routing (CIDR)", "Replaced Class A, B, C addressing. Format: `a.b.c.d/x`, where `/x` is the prefix length (network bits) and `32 - x` are host bits."),
        ("Subnet Mask", "32-bit value with `/x` contiguous 1s followed by `32 - x` zeros (e.g. `/24` = `255.255.255.0`)."),
        ("Number of Usable Hosts Formula", "Total hosts in subnet $= 2^{(32 - x)} - 2$ (Subtract 2 because all host bits 0 = Network Address, all host bits 1 = Directed Broadcast Address)."),
        ("Subnet Splitting Formula", "Borrowing $k$ bits from host portion creates $2^k$ new subnets, each with prefix length $x + k$."),
        ("Variable Length Subnet Masking (VLSM)", "Allows dividing an IP block into subnets of different sizes matching exact department host requirements, eliminating address wastage.")
    ], "Subnet Formulas", [
        "Host Bits: h = 32 - prefix",
        "Usable Hosts = 2^h - 2",
        "New Subnets = 2^(borrowed bits)",
        "Network Addr: Host bits = 0",
        "Broadcast Addr: Host bits = 1"
    ])
    
    create_comparison_slide(prs, "2.2.2.3 Auxiliary Network Layer Protocols", "M2.2.2 AUXILIARY PROTOCOLS",
        "Control & Management Protocols", [
            ("ARP (Address Resolution Protocol)", "Dynamically resolves 32-bit IP address to 48-bit MAC address using broadcast requests and unicast replies"),
            ("ICMP (Internet Control Message Protocol)", "Used for error reporting (Destination Unreachable, TTL Expired) and network diagnostics (`ping` Echo, `traceroute`)"),
            ("DHCP (Dynamic Host Configuration)", "DORA process (Discover, Offer, Request, ACK) dynamically leases IP, mask, default gateway, and DNS servers to booting hosts")
        ],
        "Address Extension Protocols", [
            ("NAT (Network Address Translation)", "Maps multiple private RFC 1918 IPs (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to a single public IP using port multiplexing (NAPT/PAT)"),
            ("NAT Translation Table", "Maintains `(Private IP, Private Port) <-> (Public IP, NAT Assigned Port)` mappings")
        ]
    )
    
    return prs

def build_m2_2_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.3", "Unicast Routing Protocols",
        "Distance Vector (Bellman-Ford, RIP, Count-to-Infinity), Link State (Dijkstra, OSPF) & Path Vector (BGP)",
        "Module 2"
    )
    
    create_comparison_slide(prs, "2.2.3.1 Distance Vector vs Link State Routing", "M2.2.3 ROUTING PARADIGMS",
        "Distance Vector (Bellman-Ford / RIP)", [
            ("Information Shared", "Vector of least-cost distances to all destinations"),
            ("Shared With", "Only directly connected physical neighbors"),
            ("Exchange Timing", "Periodically (e.g. RIP every 30s) and on trigger"),
            ("Convergence", "Slow convergence; susceptible to routing loops"),
            ("Algorithm", "Bellman-Ford Equation: $D_x(y) = \\min_v \\{ c(x,v) + D_v(y) \\}$")
        ],
        "Link State (Dijkstra / OSPF)", [
            ("Information Shared", "Status and cost of directly connected links (LSAs)"),
            ("Shared With", "Flooded to ALL routers in entire network / area"),
            ("Exchange Timing", "Only when link state changes (event-driven)"),
            ("Convergence", "Rapid convergence; loop-free topology knowledge"),
            ("Algorithm", "Dijkstra's Shortest Path Tree computation")
        ]
    )
    
    create_content_slide(prs, "2.2.3.2 Count-to-Infinity & Distance Vector Remedies", "M2.2.3 DV REMEDIES", [
        ("The Count-to-Infinity Problem", "When a link fails, two routers can create a routing loop by continually updating each other with incrementing hop counts (e.g., $A \\to B \\to A \\to \\dots$)."),
        ("Remedy 1: Define Infinity as 16 (RIP)", "Routing Information Protocol sets maximum hop metric to 15. A hop count of 16 means 'Unreachable', stopping infinite looping."),
        ("Remedy 2: Split Horizon Rule", "A router does NOT advertise a route back out the same interface through which it learned that route."),
        ("Remedy 3: Poison Reverse", "If router A routes traffic to destination X through neighbor B, router A advertises route to X back to B with metric = $\\infty$ (16), preventing B from ever routing back to A."),
        ("Remedy 4: Triggered Updates", "Routers send update messages immediately upon detecting a link failure rather than waiting for regular 30s timer.")
    ], "RIP Protocol Summary", [
        "Algorithm: Distance Vector",
        "Metric: Hop count (Max 15)",
        "Port: UDP 520",
        "Periodic Timer: 30 seconds",
        "Split Horizon + Poison Reverse"
    ])
    
    create_content_slide(prs, "2.2.3.3 OSPF & BGP Internet Routing Hierarchy", "M2.2.3 OSPF & BGP", [
        ("Open Shortest Path First (OSPF)", "Interior Gateway Protocol (IGP) based on Link State. Directly encapsulates in IP (Protocol 89). Supports authentication, equal-cost multi-path (ECMP), and Hierarchical Areas."),
        ("OSPF Area Hierarchy", "Backbone Area (Area 0) connects non-backbone areas. Area Border Routers (ABRs) summarize routing between areas, limiting LSA flooding scale."),
        ("Border Gateway Protocol (BGP-4)", "The de-facto standard Inter-Autonomous System (Inter-AS / EGP) routing protocol connecting global ISPs over TCP (Port 179)."),
        ("Path Vector Routing in BGP", "BGP advertisements include full `AS-PATH` attribute (list of Autonomous System numbers traversed). Prevents loops by discarding routes containing router's own AS number.")
    ], "Routing Matrix", [
        "RIP: Distance Vector (Hops < 16)",
        "OSPF: Link State (Cost/Bandwidth)",
        "BGP: Path Vector (AS-PATH, Policy)",
        "Intra-AS: OSPF, RIP",
        "Inter-AS: BGP-4"
    ])
    
    return prs

def build_m2_2_4(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.4", "Multicast Routing Protocols",
        "Multicasting Fundamentals, IGMP Group Management, Source-Based Trees, Shared Trees, DVMRP, MOSPF & PIM",
        "Module 2"
    )
    
    create_content_slide(prs, "2.2.4.1 Multicast Fundamentals & IGMP", "M2.2.4 MULTICAST BASICS", [
        ("Multicast Concept", "One source sends data packets to multiple designated receivers belonging to a multicast group using a single Class D multicast address (`224.0.0.0/4`)."),
        ("Internet Group Management Protocol (IGMP)", "Operates between local hosts and their directly attached first-hop router. Enables hosts to join or leave multicast groups dynamically."),
        ("IGMP Message Types", "Membership Query (router queries group members), Membership Report (host announces group join), Leave Group (host departs)."),
        ("Source-Based Trees vs Group-Shared Trees", "Source-Based: Builds a distinct shortest path tree rooted at each sender (e.g. DVMRP, MOSPF, PIM-DM). Shared Tree: All senders route traffic through a single central Rendezvous Point (RP) shared tree (e.g. PIM-SM).")
    ], "Multicast Trees", [
        "Class D IPs: 224.0.0.0 - 239.255.255.255",
        "IGMP: Host-to-Router signaling",
        "Source Tree: Optimal delay per sender",
        "Shared Tree: Less router memory state"
    ])
    
    create_comparison_slide(prs, "2.2.4.2 Multicast Routing Protocols Comparison", "M2.2.4 MULTICAST PROTOCOLS",
        "Dense-Mode Protocols (Flood & Prune)", [
            ("PIM-DM / DVMRP", "Assumes multicast group members are densely distributed across almost every subnet"),
            ("Reverse Path Forwarding (RPF)", "Accepts packet only if it arrives on interface used to reach the source IP; drops duplicates"),
            ("Flood & Prune", "Floods initial traffic everywhere; routers with no active downstream members send 'Prune' messages"),
            ("Grafting", "Allows pruned branch to rejoin tree immediately when a new host joins")
        ],
        "Sparse-Mode Protocols (Explicit Join)", [
            ("PIM-SM", "Assumes members are sparsely distributed across wide-area network"),
            ("Rendezvous Point (RP)", "Core router where all sender sources register and receiver branches join"),
            ("Explicit Join", "Traffic only forwarded to subnets that explicitly sent IGMP/PIM Join messages"),
            ("Scalability", "Highly scalable for Internet-scale video broadcasting")
        ]
    )
    
    return prs

def build_m2_2_5(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.5", "Next Generation Internet Protocol (IPv6)",
        "128-Bit Addressing, Fixed 40-Byte Base Header, Extension Headers Chain, SLAAC Autoconfiguration & Migration",
        "Module 2"
    )
    
    create_content_slide(prs, "2.2.5.1 IPv6 Header Architecture", "M2.2.5 IPV6 HEADER", [
        ("128-Bit Address Space", "$2^{128} \\approx 3.4 \\times 10^{38}$ unique addresses (represented as 8 groups of 4 hex digits: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`)."),
        ("Fixed 40-Byte Base Header", "Fixed length streamlines router processing in hardware ASICs (compared to variable 20-60B IPv4 header)."),
        ("Key Header Fields", "Version (4b: 6), Traffic Class (8b: QoS DiffServ), Flow Label (20b: maintains flow context), Payload Length (16b), Next Header (8b: identifies upper layer protocol or next extension header), Hop Limit (8b: replaces TTL), Source Address (128b), Destination Address (128b)."),
        ("Eliminated Fields", "Header Checksum (eliminated to boost speed; left to L2/L4), IHL (fixed at 40B), and Fragmentation fields (moved to optional Extension Headers).")
    ], "IPv6 vs IPv4 Header", [
        "Address: 128-bit vs 32-bit",
        "Base Header: 40B fixed vs 20-60B",
        "Checksum: None vs 16-bit Header",
        "Fragmentation: Source only vs Routers",
        "TTL -> Hop Limit (8 bits)"
    ])
    
    create_content_slide(prs, "2.2.5.2 Extension Headers, SLAAC & IPv6 Migration", "M2.2.5 SLAAC & TRANSITION", [
        ("Extension Headers Chain", "Daisy-chained via `Next Header` field: Hop-by-Hop Options $\\to$ Routing $\\to$ Fragment $\\to$ Encapsulating Security Payload (ESP) $\\to$ Authentication Header (AH) $\\to$ TCP/UDP."),
        ("Stateless Address Autoconfiguration (SLAAC)", "Host generates unique IPv6 address automatically using local link prefix advertised by router + modified EUI-64 MAC address (or randomized interface ID). No DHCP server required."),
        ("Dual-Stack Transition", "Nodes implement both full IPv4 and IPv6 protocol stacks simultaneously, allowing seamless communication across both networks."),
        ("Tunneling (6in4 / 6to4 / Teredo)", "IPv6 packets encapsulated as payload inside IPv4 packets to traverse legacy IPv4 routing backbones."),
        ("NAT64 / DNS64", "Translates IPv6-only client requests to communicate directly with legacy IPv4-only web servers.")
    ], "Transition Strategies", [
        "Dual-Stack: Run IPv4 & IPv6 together",
        "Tunneling: Encapsulate IPv6 in IPv4",
        "Translation: NAT64/DNS64 gateway",
        "SLAAC: Zero-configuration networking"
    ])
    
    return prs

def build_m2_2_6(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.6", "Quality of Service (QoS) & Traffic Shaping",
        "QoS Principles, Traffic Shaping Algorithms: Leaky Bucket vs Token Bucket, Integrated Services & Differentiated Services",
        "Module 2"
    )
    
    create_comparison_slide(prs, "2.2.6.1 Traffic Shaping: Leaky Bucket vs Token Bucket", "M2.2.6 LEAKY VS TOKEN BUCKET",
        "Leaky Bucket Algorithm", [
            ("Mechanism", "Packets enter bucket of capacity $C$; leak out bottom at constant fixed rate $r$"),
            ("Output Rate", "Strictly constant / smooth transmission rate; zero bursts allowed"),
            ("Overflow", "If arriving packet overflows bucket capacity, it is discarded"),
            ("Best For", "Strict traffic policing and real-time constant-bitrate audio (CBR)")
        ],
        "Token Bucket Algorithm", [
            ("Mechanism", "Tokens generated at constant rate $r$ into bucket of capacity $b$. Packet sent only if enough tokens present"),
            ("Output Rate", "Allows controlled burst transmission up to bucket capacity $b$, with average rate $r$"),
            ("Burst Duration", "Max burst size $= b + r \\times t$"),
            ("Best For", "Bursty Internet data traffic (Web, video streaming, database queries)")
        ]
    )
    
    create_content_slide(prs, "2.2.6.2 Architectural QoS Models: IntServ vs DiffServ", "M2.2.6 INTSERV VS DIFFSERV", [
        ("Integrated Services (IntServ / RFC 1633)", "Per-flow hard QoS guarantees. End hosts use RSVP (Resource Reservation Protocol) to reserve bandwidth and buffer space along entire path prior to data transmission."),
        ("IntServ Scalability Problem", "Requires every core router to maintain state for millions of individual flows $\\implies$ unscalable for the global Internet backbone."),
        ("Differentiated Services (DiffServ / RFC 2475)", "Class-based soft QoS. Edge routers classify and mark packets by writing a 6-bit DSCP (Differentiated Services Code Point) value in IP header."),
        ("Per-Hop Behaviors (PHB)", "Core routers inspect DSCP and schedule packets according to class without maintaining per-flow state (Expedited Forwarding EF for VoIP, Assured Forwarding AF for video).")
    ], "QoS Model Summary", [
        "IntServ: Per-flow, RSVP, stateful, unscalable",
        "DiffServ: Class-based, DSCP, stateless core",
        "Leaky Bucket: Constant output rate",
        "Token Bucket: Allows controlled bursts"
    ])
    
    return prs

def build_m2_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.3", "Linux Kernel TCP/IP Architecture & Routing",
        "Linux Network Stack Internals, sk_buff Structure, Routing Table fib_table, Route Cache & ip route Commands",
        "Module 2"
    )
    
    create_content_slide(prs, "2.3.1 Linux Kernel Network Stack & sk_buff", "M2.3 LINUX KERNEL STACK", [
        ("Linux Packet Journey", "NIC RX Ring Buffer $\\to$ DMA to RAM $\\to$ Hard IRQ $\\to$ NAPI SoftIRQ $\\to$ `netif_receive_skb()` $\\to$ IP Layer $\\to$ Transport Layer $\\to$ Socket Receive Queue."),
        ("Socket Buffer (`struct sk_buff`)", "The central data structure in Linux kernel networking representing a network packet as it moves through layers."),
        ("Zero-Copy Pointer Manipulation", "`sk_buff` contains `head`, `data`, `tail`, `end` pointers. Adding headers (encapsulation) simply shifts `data` pointer via `skb_push()`, avoiding expensive data copying in memory!"),
        ("Netfilter Hook Framework", "Kernel hooks (`NF_INET_PRE_ROUTING`, `NF_INET_LOCAL_IN`, `NF_INET_FORWARD`, `NF_INET_LOCAL_OUT`, `NF_INET_POST_ROUTING`) powering `iptables` / `nftables` firewalls and NAT.")
    ], "sk_buff Functions", [
        "skb_push(): Prepend header space",
        "skb_pull(): Strip header at receiver",
        "skb_put(): Append payload data",
        "skb_reserve(): Allocate head room",
        "Zero memory copy overhead!"
    ])
    
    create_content_slide(prs, "2.3.2 Linux Routing Table (fib_table) & ip route CLI", "M2.3 LINUX ROUTING COMMANDS", [
        ("Forwarding Information Base (`fib_table`)", "Linux kernel routing table storing network prefixes, metrics, scopes, and next-hop gateways organized in a LC-trie (Level-Compressed Trie) for sub-microsecond Longest Prefix Matching."),
        ("Viewing Routing Table", "`ip route show` or `ip route list` displays main routing table entries."),
        ("Adding Static Route", "`ip route add 192.168.10.0/24 via 10.0.0.1 dev eth0`."),
        ("Adding Default Gateway", "`ip route add default via 192.168.1.1 dev eth0`."),
        ("Deleting Route", "`ip route del 192.168.10.0/24`."),
        ("Policy Routing (`ip rule`)", "Multiple routing tables selected by source IP, TOS, or firewall mark (e.g. `ip rule add from 192.168.2.0/24 table 100`).")
    ], "Hands-on Commands", [
        "ip route show: View routes",
        "ip route add <net> via <gw> dev <if>",
        "ip route del <net>",
        "ip rule list: Policy routing rules",
        "All KTU CO2 & CO3 Topics Covered"
    ])
    
    return prs

def build_module_2_master(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "MODULE 2", "Transport & Network Layers with Linux Kernel Architecture",
        "Complete Lecture & Revision Master Deck (M2.1.1 to M2.3)",
        "Module 2 Complete"
    )
    build_m2_1_1(prs)
    build_m2_1_2(prs)
    build_m2_1_3(prs)
    build_m2_1_4(prs)
    build_m2_1_5(prs)
    build_m2_2_1(prs)
    build_m2_2_2(prs)
    build_m2_2_3(prs)
    build_m2_2_4(prs)
    build_m2_2_5(prs)
    build_m2_2_6(prs)
    build_m2_3(prs)
    return prs
