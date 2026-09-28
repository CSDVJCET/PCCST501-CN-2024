import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# --- Color Palette ---
COLOR_PRIMARY = RGBColor(30, 58, 138)      # Deep Navy/Blue
COLOR_SECONDARY = RGBColor(14, 116, 144)   # Deep Cyan / Teal
COLOR_ACCENT = RGBColor(245, 158, 11)      # Amber / Gold
COLOR_BG_DARK = RGBColor(15, 23, 42)       # Slate 900
COLOR_TEXT_LIGHT = RGBColor(248, 250, 252) # Slate 50
COLOR_TEXT_DARK = RGBColor(30, 41, 59)     # Slate 800
COLOR_TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
COLOR_CARD_BG = RGBColor(241, 245, 249)    # Slate 100

def create_title_slide(prs, title, subtitle, module_num=None):
    slide_layout = prs.slide_layouts[6] # blank layout
    slide = prs.slides.add_slide(slide_layout)
    
    # Background shape
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_BG_DARK
    bg.line.fill.background()
    
    # Accent bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1), Inches(1.5), Inches(0.2), Inches(4.5))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_ACCENT
    bar.line.fill.background()
    
    # Text Box
    tx_box = slide.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.5), Inches(4.5))
    tf = tx_box.text_frame
    tf.word_wrap = True
    
    if module_num:
        p0 = tf.paragraphs[0]
        p0.text = f"PCCST501 COMPUTER NETWORKS | MODULE {module_num}"
        p0.font.bold = True
        p0.font.size = Pt(16)
        p0.font.color.rgb = COLOR_ACCENT
        p0.space_after = Pt(14)
        p1 = tf.add_paragraph()
    else:
        p1 = tf.paragraphs[0]
        
    p1.text = title
    p1.font.bold = True
    p1.font.size = Pt(38)
    p1.font.color.rgb = COLOR_TEXT_LIGHT
    p1.space_after = Pt(20)
    
    p2 = tf.add_paragraph()
    p2.text = subtitle
    p2.font.size = Pt(20)
    p2.font.color.rgb = RGBColor(148, 163, 184)
    p2.space_after = Pt(24)
    
    p3 = tf.add_paragraph()
    p3.text = "Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET"
    p3.font.size = Pt(14)
    p3.font.color.rgb = RGBColor(203, 213, 225)
    
    return slide

def create_content_slide(prs, title, module_tag, points, card_header=None, card_content=None):
    slide_layout = prs.slide_layouts[6] # blank
    slide = prs.slides.add_slide(slide_layout)
    
    # Top banner bar
    banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
    banner.fill.solid()
    banner.fill.fore_color.rgb = COLOR_PRIMARY
    banner.line.fill.background()
    
    # Title Text
    tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.15), Inches(9.5), Inches(0.8))
    tf_t = tx_title.text_frame
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.bold = True
    p_t.font.size = Pt(24)
    p_t.font.color.rgb = COLOR_TEXT_LIGHT
    
    # Tag Text (Top right)
    tx_tag = slide.shapes.add_textbox(Inches(9.5), Inches(0.15), Inches(3.2), Inches(0.8))
    tf_tag = tx_tag.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = module_tag
    p_tag.alignment = PP_ALIGN.RIGHT
    p_tag.font.bold = True
    p_tag.font.size = Pt(13)
    p_tag.font.color.rgb = COLOR_ACCENT
    
    # Left Content Box (Points)
    left_w = Inches(7.5) if card_header else Inches(11.8)
    tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.4), left_w, Inches(5.5))
    tf = tx_box.text_frame
    tf.word_wrap = True
    
    for i, pt in enumerate(points):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if isinstance(pt, tuple): # (Header, details)
            p.text = f"• {pt[0]}: "
            p.font.bold = True
            p.font.size = Pt(16)
            p.font.color.rgb = COLOR_PRIMARY
            p.space_after = Pt(4)
            
            # Add detail
            p_sub = tf.add_paragraph()
            p_sub.text = f"   {pt[1]}"
            p_sub.font.size = Pt(14)
            p_sub.font.color.rgb = COLOR_TEXT_DARK
            p_sub.space_after = Pt(10)
        else:
            p.text = f"• {pt}"
            p.font.size = Pt(15)
            p.font.color.rgb = COLOR_TEXT_DARK
            p.space_after = Pt(10)
            
    # Right Highlight Card (if present)
    if card_header and card_content:
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.7), Inches(1.5), Inches(3.9), Inches(5.3))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_SECONDARY
        card.line.width = Pt(1.5)
        
        tx_card = slide.shapes.add_textbox(Inches(8.9), Inches(1.7), Inches(3.5), Inches(4.9))
        tf_c = tx_card.text_frame
        tf_c.word_wrap = True
        
        p_ch = tf_c.paragraphs[0]
        p_ch.text = card_header
        p_ch.font.bold = True
        p_ch.font.size = Pt(16)
        p_ch.font.color.rgb = COLOR_SECONDARY
        p_ch.space_after = Pt(12)
        
        for c_pt in card_content:
            p_c = tf_c.add_paragraph()
            p_c.text = f"→ {c_pt}"
            p_c.font.size = Pt(13)
            p_c.font.color.rgb = COLOR_TEXT_DARK
            p_c.space_after = Pt(8)
            
    # Footer
    footer = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.8), Inches(0.4))
    tf_f = footer.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "PCCST501 Computer Networks | VJCET Dept of CSE | Prepared by Prof. Anju Markose"
    p_f.font.size = Pt(10)
    p_f.font.color.rgb = COLOR_TEXT_MUTED
    
    return slide

# ==================== MODULE 1 DECK BUILDER ====================
def build_module_1(prs):
    create_title_slide(prs, "Overview of Internet & Application Layer", "Architecture, Protocol Layering, HTTP, FTP, Email, DNS & BitTorrent P2P", 1)
    
    create_content_slide(prs, "1.1 Overview of the Internet", "MODULE 1", [
        ("Network Edge", "End systems, hosts (clients & servers) running distributed applications."),
        ("Network Core", "Interconnected mesh of routers and packet switches forwarding data packets."),
        ("Packet Switching vs Circuit Switching", "Statistical multiplexing on-demand vs dedicated physical circuit reservation."),
        ("Transmission Delay & Propagation Delay", "Transmission = L / R (packet length / link rate); Propagation = d / s (distance / wave speed)."),
        ("Packet Loss & Throughput", "Queue overflow in router buffers causes loss; bottleneck link determines end-to-end throughput.")
    ], "Key Takeaway", [
        "Internet is a 'Network of Networks'",
        "Statistical multiplexing optimizes link utilization",
        "Total Delay = Proc + Queue + Trans + Prop"
    ])
    
    create_content_slide(prs, "1.2 Protocol Layering & OSI / TCP-IP Models", "MODULE 1", [
        ("Layering Principle", "Modular design where each layer provides a well-defined service to the layer above."),
        ("OSI 7-Layer Reference Model", "Application, Presentation, Session, Transport, Network, Data Link, Physical."),
        ("TCP/IP 5-Layer Internet Model", "Application, Transport, Network, Data Link, Physical."),
        ("Encapsulation & Decapsulation", "Headers and trailers added as data moves down (Data -> Segment -> Packet -> Frame -> Bits)."),
        ("Protocol Data Units (PDU)", "Message (L5), Segment (L4), Datagram/Packet (L3), Frame (L2), Bit stream (L1).")
    ], "Comparison Summary", [
        "OSI: Strict conceptual model with Session & Presentation",
        "TCP/IP: Practical implementation architecture of the Internet",
        "Encapsulation preserves abstraction"
    ])

    create_content_slide(prs, "1.3 Application Layer Paradigms", "MODULE 1", [
        ("Client-Server Architecture", "Always-on host (server) serves requests from many intermittent hosts (clients). E.g. Web, FTP."),
        ("Peer-to-Peer (P2P) Architecture", "Direct communication between arbitrary end systems (peers) with self-scalability. E.g. BitTorrent."),
        ("Application Layer Protocols", "Define message types (request/response), syntax, semantics, and rules for sending/handling."),
        ("Transport Services Needed", "Data integrity (reliable transfer), throughput (bandwidth guarantees), timing (low latency), security.")
    ], "Paradigm Contrast", [
        "Client-Server: Centralized control, server bottleneck potential",
        "P2P: Highly scalable, decentralized, complex churn management"
    ])

    create_content_slide(prs, "1.4 World Wide Web & HTTP", "MODULE 1", [
        ("HTTP Basics", "HyperText Transfer Protocol running over TCP (Port 80 default, 443 HTTPS). Stateless protocol."),
        ("Non-Persistent vs Persistent HTTP", "Non-persistent: 1 TCP connection per object (2 RTT per object). Persistent (HTTP 1.1): multiple objects over single connection."),
        ("HTTP Methods", "GET (retrieve), POST (submit form data), HEAD (headers only), PUT (upload/replace), DELETE (remove)."),
        ("Status Codes", "200 OK, 301 Moved Permanently, 304 Not Modified, 400 Bad Request, 404 Not Found, 500 Internal Server Error."),
        ("Cookies & Web Caching", "Cookies maintain session state on top of stateless HTTP; Proxy servers cache content to reduce latency.")
    ], "HTTP Evolution", [
        "HTTP/1.0: Non-persistent",
        "HTTP/1.1: Persistent + Pipelining",
        "HTTP/2: Binary framing, Multiplexing",
        "HTTP/3: UDP (QUIC based)"
    ])

    create_content_slide(prs, "1.5 File Transfer Protocol (FTP)", "MODULE 1", [
        ("Dual Connection Model", "Uses two separate parallel TCP connections: Control connection (Port 21) & Data connection (Port 20)."),
        ("Out-of-Band Control", "Control information (commands/replies) sent over a separate connection, not interleaved with data."),
        ("Stateful Protocol", "FTP server maintains client state (current working directory, auth session)."),
        ("Active vs Passive Mode", "Active: Client listens on port, server connects. Passive (PASV): Server opens port, client connects (firewall friendly).")
    ], "FTP Commands", [
        "USER, PASS: Authentication",
        "LIST: Directory listing",
        "RETR: Retrieve / download file",
        "STOR: Store / upload file"
    ])

    create_content_slide(prs, "1.6 Electronic Mail (SMTP, POP3, IMAP, MIME)", "MODULE 1", [
        ("Email Architecture", "User Agents (Mail Readers), Mail Servers (Spools & Mailboxes), Simple Mail Transfer Protocol (SMTP)."),
        ("SMTP (Port 25/587)", "Push protocol between mail servers. Uses direct TCP connection, ASCII command/response format."),
        ("Mail Access Protocols (Pull)", "POP3 (Port 110, download & delete/keep, stateless), IMAP4 (Port 143, maintains folders/state across devices)."),
        ("MIME Extension", "Multipurpose Internet Mail Extensions: allows non-ASCII multimedia content via base64/quoted-printable encoding.")
    ], "Push vs Pull", [
        "Sender UA -> Sender Server: SMTP (Push)",
        "Sender Server -> Recipient Server: SMTP (Push)",
        "Recipient Server -> Recipient UA: POP3/IMAP (Pull)"
    ])

    create_content_slide(prs, "1.7 Domain Name System (DNS)", "MODULE 1", [
        ("Role of DNS", "Distributed database mapping human-readable hostnames to 32-bit/128-bit IP addresses (Port 53 UDP/TCP)."),
        ("Hierarchical Namespace", "Root DNS Servers -> Top-Level Domain (TLD: .com, .edu, .in) -> Authoritative DNS Servers."),
        ("Resolution Mechanisms", "Recursive Resolution (Local DNS resolver does entire query tree) vs Iterative Resolution (referrals returned)."),
        ("DNS Resource Records (RR)", "Format: (Name, Value, Type, TTL). Type A (IPv4), AAAA (IPv6), NS (Name Server), CNAME (Alias), MX (Mail Exchange)."),
        ("DNS Caching", "Resolvers cache RR mappings to drastically reduce latency and root server load.")
    ], "Key DNS Records", [
        "Type A: hostname -> IPv4",
        "Type AAAA: hostname -> IPv6",
        "Type CNAME: alias -> canonical name",
        "Type MX: domain -> mail server",
        "Type NS: domain -> authoritative server"
    ])

    create_content_slide(prs, "1.8 Peer-to-Peer Paradigm & BitTorrent Case Study", "MODULE 1", [
        ("Self-Scalability in P2P", "Each peer adds download demand AND upload capacity, allowing distribution time to remain bounded."),
        ("BitTorrent Architecture", "File split into equal chunks (256 KB). Peers join a 'swarm' coordinated by a 'tracker' (or DHT)."),
        ("Rarest First Selection", "Peers request rarest chunks among neighbors first to maximize chunk diversity across the swarm."),
        ("Tit-for-Tat Choking Algorithm", "Peers unchoke top 4 uploaders contributing at highest rates; Optimistic Unchoking explores new peers every 30s.")
    ], "BitTorrent Highlights", [
        "Tracker: Coordinates peer list",
        "Torrent: Metadata descriptor file",
        "Rarest First: Prevents bottleneck",
        "Tit-for-Tat: Incentivizes upload"
    ])

# ==================== MODULE 2 DECK BUILDER ====================
def build_module_2(prs):
    create_title_slide(prs, "Transport & Network Layers with Linux Kernel", "UDP, TCP, Socket Programming, IPv4/IPv6, Routing Protocols & QoS", 2)
    
    create_content_slide(prs, "2.1 Transport Layer Services & UDP", "MODULE 2", [
        ("Transport Layer Role", "Provides process-to-process logical communication using 16-bit Port Numbers."),
        ("Multiplexing & Demultiplexing", "Gathering data chunks from multiple sockets (multiplexing) and delivering to correct socket via headers (demux)."),
        ("User Datagram Protocol (UDP)", "Connectionless, unreliable, lightweight, minimal overhead (8-byte header: Src Port, Dst Port, Length, Checksum)."),
        ("UDP Checksum Calculation", "Calculated over 16-bit words of Pseudo-header (IP info) + UDP header + payload using 1's complement addition.")
    ], "When to use UDP?", [
        "Real-time streaming (VoIP, Video)",
        "DNS queries & SNMP traps",
        "Where low latency is vital and retransmissions cause unacceptable delay"
    ])

    create_content_slide(prs, "2.2 Transmission Control Protocol (TCP)", "MODULE 2", [
        ("TCP Characteristics", "Connection-oriented, full-duplex, reliable byte-stream service with flow & congestion control."),
        ("Connection Establishment", "Three-Way Handshake: SYN -> SYN-ACK -> ACK. Connection Release: 4-Way FIN/ACK exchange."),
        ("TCP Header Structure", "20 to 60 bytes (Src/Dst Port, Sequence No, Ack No, Data Offset, Flags: URG, ACK, PSH, RST, SYN, FIN, Window Size, Checksum)."),
        ("Flow Control", "Sliding Window Mechanism: Receiver advertises `rwnd` to prevent buffer overflow. Silly Window Syndrome mitigated by Nagle's & Clark's algorithm.")
    ], "TCP Handshake", [
        "1. Client -> Server: SYN (seq=x)",
        "2. Server -> Client: SYN-ACK (seq=y, ack=x+1)",
        "3. Client -> Server: ACK (seq=x+1, ack=y+1)"
    ])

    create_content_slide(prs, "2.3 TCP Congestion Control Mechanisms", "MODULE 2", [
        ("Congestion Window (cwnd)", "Dynamic limit on unacknowledged inflight bytes maintained by sender. Effective Window = min(cwnd, rwnd)."),
        ("Slow Start Phase", "cwnd starts at 1 MSS, doubles every RTT (exponential growth) until reaching `ssthresh` threshold."),
        ("Congestion Avoidance", "Linear growth (AIMD: Additive Increase Multiplicative Decrease). cwnd increases by 1 MSS per RTT."),
        ("Fast Retransmit & Fast Recovery", "3 duplicate ACKs trigger immediate retransmission before timeout; cwnd halved rather than reset to 1 (TCP Reno).")
    ], "Tahoe vs Reno", [
        "Timeout: cwnd=1, ssthresh=cwnd/2 (Both)",
        "3 Dup ACKs (Tahoe): cwnd=1",
        "3 Dup ACKs (Reno): cwnd=ssthresh, enters Fast Recovery (Avoids Slow Start)"
    ])

    create_content_slide(prs, "2.4 Socket Programming & I/O Multiplexing", "MODULE 2", [
        ("Socket API Lifecycle (TCP)", "Server: `socket()` -> `bind()` -> `listen()` -> `accept()` -> `recv()`/`send()` -> `close()`. Client: `socket()` -> `connect()` -> `send()`/`recv()` -> `close()`."),
        ("UDP Sockets", "No connection setup; uses `sendto()` and `recvfrom()` directly with destination socket addresses."),
        ("I/O Multiplexing with select()", "`select(maxfd+1, &readfds, &writefds, &exceptfds, &timeout)` monitors multiple file descriptors simultaneously without threads."),
        ("poll() Function", "Uses an array of `struct pollfd` structures with event masks (`POLLIN`, `POLLOUT`), eliminating `FD_SETSIZE` limitations.")
    ], "Socket Syscalls", [
        "socket(AF_INET, SOCK_STREAM, 0)",
        "bind(): assigns IP & Port",
        "listen(): backlog queue",
        "accept(): creates new active socket",
        "select() / poll(): Non-blocking multiplexing"
    ])

    create_content_slide(prs, "2.5 Network Layer: IPv4, Subnetting & CIDR", "MODULE 2", [
        ("Network Layer Responsibilities", "Host-to-host routing, logical addressing, datagram forwarding, fragmentation/reassembly."),
        ("IPv4 Datagram Header", "20-60 bytes (Version, IHL, TOS/DiffServ, Total Length, Identification, Flags [DF, MF], Fragment Offset, TTL, Protocol, Checksum)."),
        ("Classful vs Classless Addressing (CIDR)", "Class A/B/C deprecated in favor of Classless Inter-Domain Routing (e.g. `192.168.1.0/24` prefix)."),
        ("Subnetting & VLSM", "Borrowing host bits for subnetting; Variable Length Subnet Masking optimizes address space allocation."),
        ("Auxiliary Protocols", "ARP (IP to MAC resolution), ICMP (error reporting/diagnostics: ping, traceroute), NAT, DHCP.")
    ], "IPv4 Key Formulas", [
        "No. of subnets = 2^(borrowed bits)",
        "Hosts per subnet = 2^(host bits) - 2",
        "Broadcast Addr: All host bits = 1",
        "Network Addr: All host bits = 0"
    ])

    create_content_slide(prs, "2.6 Unicast Routing Protocols", "MODULE 2", [
        ("Distance Vector Routing (Bellman-Ford)", "Routers share vector of distances to all nodes with neighbors. Used in RIP (Hop count limit = 15)."),
        ("Count-to-Infinity Problem", "Slow convergence on link failure; solved by Split Horizon and Poison Reverse techniques."),
        ("Link State Routing (Dijkstra's Algorithm)", "Routers flood Link State Advertisements (LSAs) to build full network topology graph. Used in OSPF."),
        ("Path Vector Routing (BGP)", "Border Gateway Protocol for Inter-Autonomous System (Inter-AS) routing; prevents routing loops by tracking full AS paths.")
    ], "Routing Protocol Matrix", [
        "RIP: Distance Vector, Metric: Hops (<16)",
        "OSPF: Link State, Metric: Cost/Bandwidth, Area hierarchy",
        "BGP: Path Vector, Policy-based, Inter-AS"
    ])

    create_content_slide(prs, "2.7 Multicast Routing, Next-Gen IP & QoS", "MODULE 2", [
        ("Multicast Basics & IGMP", "One-to-many communication; IGMP handles host group join/leave; Source-based trees vs Group-shared trees."),
        ("Multicast Protocols", "Intra-domain: DVMRP (Reverse Path Forwarding), MOSPF, PIM-DM (Flood & Prune), PIM-SM (Rendezvous Point)."),
        ("Next Generation IP (IPv6)", "128-bit addresses (hex notation), simplified 40-byte base header, no checksum, flow labeling, extension headers."),
        ("Quality of Service (QoS) & Traffic Shaping", "Leaky Bucket (constant output rate) vs Token Bucket (allows controlled bursts); IntServ (RSVP) vs DiffServ (DSCP)."),
        ("Linux Routing Hands-on", "`ip route add`, `ip route del`, kernel Forwarding Information Base (`fib_table`) and route cache.")
    ], "IPv6 vs IPv4", [
        "Address: 128-bit vs 32-bit",
        "Base Header: 40-byte fixed vs 20-60B",
        "Fragmentation: Source host vs Routers",
        "Auto-configuration: SLAAC built-in"
    ])

# ==================== MODULE 3 DECK BUILDER ====================
def build_module_3(prs):
    create_title_slide(prs, "Data Link Layer, Ethernet & Wireless LANs", "Framing, Error/Flow Control, MAC Protocols, 802.11 & Mobile IP", 3)
    
    create_content_slide(prs, "3.1 Data Link Control: Framing, Error & Flow Control", "MODULE 3", [
        ("Data Link Layer Responsibilities", "Node-to-node frame delivery across physical link, framing, link-layer addressing, error/flow control."),
        ("Framing Techniques", "Character Count (vulnerable to bit flips), Byte Stuffing (ESC character), Bit Stuffing (0 inserted after five consecutive 1s)."),
        ("Error Detection Codes", "Parity check, Checksum, Cyclic Redundancy Check (CRC using generator polynomial division)."),
        ("Error Correction Codes", "Hamming Code: detects 2-bit errors, corrects single-bit errors using parity check bits at positions 2^k."),
        ("Flow Control Protocols", "Stop-and-Wait, Sliding Window: Go-Back-N (window N, discards out of order), Selective Repeat (individual ACKs).")
    ], "Framing & CRC", [
        "Bit Stuffing Flag: 01111110",
        "CRC Divisor: (n+1) bit polynomial produces n-bit FCS remainder",
        "Hamming Distance: d_min determines detection/correction power"
    ])

    create_content_slide(prs, "3.2 Multiple Access Protocols (MAC)", "MODULE 3", [
        ("Random Access Protocols", "Pure ALOHA (Max throughput 18.4%), Slotted ALOHA (Max throughput 36.8%)."),
        ("CSMA (Carrier Sense Multiple Access)", "1-persistent, Non-persistent, p-persistent carrier sensing strategies."),
        ("CSMA/CD (Collision Detection)", "Listen while transmitting; if collision detected, abort, transmit jam signal, apply Binary Exponential Backoff (Used in Ethernet)."),
        ("CSMA/CA (Collision Avoidance)", "Used in Wireless LANs; uses Inter-Frame Spacing (IFS), Contention Window, and optional RTS/CTS handshake."),
        ("Controlled Access & Channelization", "Reservation, Polling, Token Ring; FDMA, TDMA, CDMA (Orthogonal Walsh-Hadamard codes).")
    ], "CSMA/CD Minimum Frame Size", [
        "Condition: Trans_Time >= 2 * Prop_Time",
        "Min Frame Length = 2 * Propagation Delay * Bandwidth",
        "Guarantees sender detects collision before transmission finishes"
    ])

    create_content_slide(prs, "3.3 Link Layer Addressing & Ethernet Protocols", "MODULE 3", [
        ("MAC / Link Layer Addressing", "48-bit physical address (6 octets in hex: `00:1A:2B:3C:4D:5E`). First 24 bits: OUI vendor ID, last 24: device serial."),
        ("Address Resolution Protocol (ARP)", "Dynamically maps 32-bit IPv4 address to 48-bit MAC address using broadcast request & unicast reply."),
        ("Standard Ethernet (IEEE 802.3)", "10 Mbps baseband, Manchester encoding, 10BASE5 / 10BASE2 / 10BASE-T."),
        ("High-Speed Ethernet Evolution", "Fast Ethernet (100 Mbps, 802.3u), Gigabit Ethernet (1 Gbps, 802.3ab), 10-Gigabit Ethernet (802.3ae)."),
        ("Ethernet Frame Format", "Preamble (7B), SFD (1B), Dst MAC (6B), Src MAC (6B), Type/Length (2B), Payload (46-1500B), CRC FCS (4B).")
    ], "ARP Cache & Frames", [
        "ARP Request: Broadcast (FF:FF:FF:FF:FF:FF)",
        "ARP Reply: Unicast to requester",
        "Min Ethernet Frame: 64 Bytes",
        "Max Ethernet Frame (MTU): 1518 Bytes"
    ])

    create_content_slide(prs, "3.4 Connecting Devices & VLANs", "MODULE 3", [
        ("Physical Layer Devices", "Repeaters & Hubs: regenerate/broadcast electrical signals; single collision & broadcast domain."),
        ("Data Link Layer Devices", "Bridges & Layer 2 Switches: filter frames based on MAC address tables; separate collision domains, single broadcast domain."),
        ("Learning Switch Algorithm", "Inspects Source MAC of incoming frames to learn port mappings; floods frames if Destination MAC unknown."),
        ("Virtual LANs (VLAN - IEEE 802.1Q)", "Logically segments a physical switch into multiple isolated broadcast domains; uses 4-byte 802.1Q tag with 12-bit VLAN ID."),
        ("Network Layer Devices", "Routers: forward packets based on IP addresses; separate both collision AND broadcast domains.")
    ], "Collision vs Broadcast Domains", [
        "Hub: 1 Collision, 1 Broadcast",
        "Switch: N Collision (per port), 1 Broadcast",
        "Switch + VLANs: N Collision, M Broadcast (per VLAN)",
        "Router: Separates all Collision & Broadcast"
    ])

    create_content_slide(prs, "3.5 Wireless LANs (IEEE 802.11) & Mobile IP", "MODULE 3", [
        ("IEEE 802.11 Architecture", "Basic Service Set (BSS) with Access Point (AP) or Ad-hoc; Extended Service Set (ESS) connected via Distribution System (DS)."),
        ("MAC Sublayer in 802.11", "CSMA/CA with Network Allocation Vector (NAV) virtual carrier sensing; Inter-frame Spaces (SIFS < PIFS < DIFS)."),
        ("Hidden & Exposed Terminal Problems", "Hidden Node: Solved by RTS (Request to Send) / CTS (Clear to Send) exchange; Exposed Node: prevented from transmitting unnecessarily."),
        ("Mobile IP Architecture", "Mobile Node (MN), Home Agent (HA), Foreign Agent (FA), Home Address (static) & Care-of Address (COA temporary)."),
        ("Triangle Routing & Optimization", "Correspondent Node -> Home Agent -> Foreign Agent -> Mobile Node encapsulation tunneling; Direct binding route optimization.")
    ], "802.11 Standards", [
        "802.11b: 2.4 GHz, 11 Mbps (DSSS)",
        "802.11g: 2.4 GHz, 54 Mbps (OFDM)",
        "802.11n: 2.4/5 GHz, 600 Mbps (MIMO)",
        "802.11ac: 5 GHz, 6.9 Gbps (MU-MIMO)",
        "802.11ax (WiFi 6): OFDMA"
    ])

# ==================== MODULE 4 DECK BUILDER ====================
def build_module_4(prs):
    create_title_slide(prs, "Network Management & Physical Layer", "SNMP, ASN.1, Signals, Digital/Analog Transmission & Media", 4)
    
    create_content_slide(prs, "4.1 Network Management: SNMP Architecture", "MODULE 4", [
        ("Network Management Framework", "Managing Entity (Manager / NMS), Managed Device (Agent), Management Information Base (MIB), Protocol (SNMP)."),
        ("SNMP Operations (UDP Port 161/162)", "`GetRequest`, `GetNextRequest`, `GetBulkRequest` (fetch MIB data), `SetRequest` (configure device), `Response`, `Trap` (unsolicited alert), `InformRequest`."),
        ("SNMP Versions", "SNMPv1 (Community strings in plaintext), SNMPv2c (GetBulkRequest, 64-bit counters), SNMPv3 (USM Security: Auth with MD5/SHA, Encryption with DES/AES, VACM Access Control)."),
        ("Structure of Management Information (SMI)", "Defines rules for naming objects, data types, and constructing MIB tables.")
    ], "SNMP Ports", [
        "Port 161 UDP: Manager to Agent (Get/Set)",
        "Port 162 UDP: Agent to Manager (Trap/Inform)",
        "SNMPv3 provides Confidentiality, Integrity, Authentication"
    ])

    create_content_slide(prs, "4.2 Abstract Syntax Notation One (ASN.1) & MIB", "MODULE 4", [
        ("Role of ASN.1", "Standard formal language to define data types and structures independently of hardware architecture."),
        ("Basic ASN.1 Data Types", "Primitive: `INTEGER`, `OCTET STRING`, `OBJECT IDENTIFIER`, `BOOLEAN`, `NULL`. Constructed: `SEQUENCE`, `SEQUENCE OF`, `CHOICE`."),
        ("Basic Encoding Rules (BER)", "TLV (Type-Length-Value) format for serializing ASN.1 data onto network wire."),
        ("Management Information Base (MIB-2)", "Hierarchical tree structure of manageable objects. Standard root: `iso.org.dod.internet.mgmt.mib-2` (`1.3.6.1.2.1`)."),
        ("Object Identifier (OID)", "Dotted numerical path locating node in MIB tree. E.g., `sysDescr` = `1.3.6.1.2.1.1.1`.")
    ], "BER TLV Structure", [
        "Tag (Type): 1 byte identifier",
        "Length: 1 or more bytes (value length)",
        "Value: Actual payload data bytes",
        "Example: INTEGER 5 -> 02 01 05"
    ])

    create_content_slide(prs, "4.3 Physical Layer: Data, Signals & Capacity Limits", "MODULE 4", [
        ("Analog vs Digital Signals", "Continuous amplitude values over time vs discrete finite levels (binary 0 and 1)."),
        ("Time Domain vs Frequency Domain", "Fourier Analysis: any composite periodic signal can be decomposed into an infinite sum of sine waves."),
        ("Transmission Impairments", "Attenuation (loss of energy, dB formula $10 \log_{10}(P_2/P_1)$), Distortion (phase shifting of harmonics), Noise (Thermal, Induced, Crosstalk, Impulse)."),
        ("Nyquist Bit Rate (Noiseless Channel)", "$C = 2 \times B \times \log_2(L)$ bps, where $B$ = Bandwidth in Hz, $L$ = number of signal levels."),
        ("Shannon Capacity Formula (Noisy Channel)", "$C = B \times \log_2(1 + \text{SNR})$ bps, where SNR is signal-to-noise power ratio in linear scale.")
    ], "Capacity Formulas", [
        "Nyquist: Max rate for noiseless channel",
        "Shannon: Theoretical upper bound with noise",
        "SNR(dB) = 10 * log10(SNR_linear)",
        "If SNR(dB)=30dB, SNR_linear=1000"
    ])

    create_content_slide(prs, "4.4 Digital Transmission: Line Coding Techniques", "MODULE 4", [
        ("Line Coding Concept", "Converting sequence of binary digits into discrete digital voltage signals."),
        ("Unipolar & Polar NRZ", "NRZ-L (Level): Positive for 0, Negative for 1. NRZ-I (Invert): Transition at beginning of bit for 1, no transition for 0 (DC component & sync issues)."),
        ("Biphase Coding (Self-Synchronizing)", "Manchester (0 = High-to-Low transition, 1 = Low-to-High transition, used in 802.3 Ethernet); Differential Manchester (transition at start for 0)."),
        ("Bipolar & Block Coding", "AMI (Alternate Mark Inversion: 0=0V, 1=alternating +V/-V); 4B/5B block coding eliminates long runs of consecutive zeros.")
    ], "Line Coding Summary", [
        "NRZ: Simple, poor sync, DC bias",
        "Manchester: Perfect sync, double bandwidth",
        "AMI: Zero DC bias, loss of sync on 0s",
        "B8ZS / HDB3: Scrambling solves long 0s"
    ])

    create_content_slide(prs, "4.5 Analog Transmission & Bandwidth Utilization", "MODULE 4", [
        ("Digital-to-Analog Modulation", "Amplitude Shift Keying (ASK), Frequency Shift Keying (FSK), Phase Shift Keying (BPSK, QPSK)."),
        ("Quadrature Amplitude Modulation (QAM)", "Combines ASK and PSK to transmit multiple bits per baud (e.g., 16-QAM sends 4 bits/baud, 64-QAM sends 6 bits/baud)."),
        ("Frequency Division Multiplexing (FDM)", "Analog technique; divides total bandwidth into non-overlapping frequency bands separated by guard bands."),
        ("Wavelength Division Multiplexing (WDM)", "Optical multiplexing of multiple light wavelengths over a single optical fiber strand."),
        ("Time Division Multiplexing (TDM)", "Digital technique; Synchronous TDM assigns fixed time slots per channel; Statistical TDM assigns slots dynamically on-demand.")
    ], "Multiplexing Methods", [
        "FDM: Analog, frequency bands (Radio/TV)",
        "WDM: Optical spectrum in glass fiber",
        "TDM: Digital time slots (T1/E1 lines)",
        "Statistical TDM: Eliminates idle slots"
    ])

    create_content_slide(prs, "4.6 Transmission Media (Guided & Unguided)", "MODULE 4", [
        ("Guided Media (Physical Conductors)", "Twisted Pair (UTP Cat 5e/6, STP - twists cancel electromagnetic interference), Coaxial Cable (copper core with braided shield), Optical Fiber (light propagation by Total Internal Reflection; Single-mode vs Multi-mode)."),
        ("Unguided Media (Wireless Propagation)", "Radio Waves (3 kHz - 1 GHz, omnidirectional, penetrate walls), Microwaves (1 GHz - 300 GHz, line-of-sight, parabolic dish), Infrared (300 GHz - 400 THz, short range, cannot penetrate walls)."),
        ("Satellite Communication", "Geostationary Earth Orbit (GEO ~36,000 km), Medium Earth Orbit (MEO: GPS), Low Earth Orbit (LEO: Starlink, low propagation delay).")
    ], "Media Comparison", [
        "UTP: Inexpensive, easy install, 100m limit",
        "Fiber: Immense bandwidth, immune to EMI, long distance",
        "Radio/Microwave: High mobility, path loss / fading"
    ])

# ==================== MAIN EXECUTION ====================
def main():
    os.makedirs("assets/ppts", exist_ok=True)
    
    # 1. Module 1
    prs1 = Presentation()
    prs1.slide_width = Inches(13.333)
    prs1.slide_height = Inches(7.5)
    build_module_1(prs1)
    prs1.save("assets/ppts/Module_1_Application_Layer.pptx")
    print("Generated Module_1_Application_Layer.pptx")
    
    # 2. Module 2
    prs2 = Presentation()
    prs2.slide_width = Inches(13.333)
    prs2.slide_height = Inches(7.5)
    build_module_2(prs2)
    prs2.save("assets/ppts/Module_2_Transport_and_Network_Layer.pptx")
    print("Generated Module_2_Transport_and_Network_Layer.pptx")
    
    # 3. Module 3
    prs3 = Presentation()
    prs3.slide_width = Inches(13.333)
    prs3.slide_height = Inches(7.5)
    build_module_3(prs3)
    prs3.save("assets/ppts/Module_3_DataLink_Layer_and_WLAN.pptx")
    print("Generated Module_3_DataLink_Layer_and_WLAN.pptx")
    
    # 4. Module 4
    prs4 = Presentation()
    prs4.slide_width = Inches(13.333)
    prs4.slide_height = Inches(7.5)
    build_module_4(prs4)
    prs4.save("assets/ppts/Module_4_Network_Management_and_Physical_Layer.pptx")
    print("Generated Module_4_Network_Management_and_Physical_Layer.pptx")
    
    # 5. Master Course Deck
    prs_all = Presentation()
    prs_all.slide_width = Inches(13.333)
    prs_all.slide_height = Inches(7.5)
    create_title_slide(prs_all, "PCCST501 Computer Networks", "Complete Master Course Lecture Deck (Modules 1 - 4)", None)
    build_module_1(prs_all)
    build_module_2(prs_all)
    build_module_3(prs_all)
    build_module_4(prs_all)
    prs_all.save("assets/ppts/PCCST501_Complete_Course_Deck.pptx")
    print("Generated PCCST501_Complete_Course_Deck.pptx")

if __name__ == "__main__":
    main()
