"""
ppts_module1.py
Topic-wise slide deck builders for Module 1: Application Layer & Peer-to-Peer Paradigms
Author: Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
"""

from generate_comprehensive_ppts import (
    init_prs, create_title_slide, create_content_slide, create_comparison_slide
)

def build_m1_1(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.1", "Overview of the Internet Architecture",
        "Network Edge, Network Core, Packet Switching vs Circuit Switching, Delay Models, Loss & Throughput",
        "Module 1"
    )
    
    create_content_slide(prs, "1.1.1 Internet Structure: Edge & Core", "M1.1 INTERNET OVERVIEW", [
        ("The Internet: Network of Networks", "A global interconnection of billions of computing devices (hosts/end systems) running distributed network applications."),
        ("Network Edge", "End systems (clients, servers, mobile, IoT) running application-layer software. Access networks (DSL, FTTH, 4G/5G, Wi-Fi) connect edge devices to the core."),
        ("Network Core", "Interconnected mesh of packet switches (routers, link-layer switches) responsible for forwarding data packets across the global mesh."),
        ("Protocols & Standards", "Protocols define format, order of messages sent/received, and actions taken upon message transmission/receipt. Governed by IETF RFCs.")
    ], "Structural Hierarchy", [
        "Tier-1 ISPs: Global transit backbone",
        "IXPs: Internet Exchange Points",
        "Regional ISPs: Connect local access nets",
        "End Hosts: Produce & consume traffic"
    ])
    
    create_comparison_slide(prs, "1.1.2 Switching Paradigms: Packet vs Circuit", "M1.1 SWITCHING COMPARISON",
        "Packet Switching (Internet)", [
            ("Data Unit", "Data chunked into discrete packets"),
            ("Resource Allocation", "Statistical Multiplexing on-demand"),
            ("Bandwidth Efficiency", "High link utilization; handles bursty data"),
            ("Queueing & Loss", "Buffers packets; causes queuing delay & loss"),
            ("State", "Stateless core; flexible routing")
        ],
        "Circuit Switching (Legacy PSTN)", [
            ("Data Unit", "Continuous stream over dedicated circuit"),
            ("Resource Allocation", "Pre-allocated dedicated bandwidth (FDM/TDM)"),
            ("Bandwidth Efficiency", "Inefficient during idle / silent periods"),
            ("Queueing & Loss", "Zero queuing delay; calls blocked if busy"),
            ("State", "Call setup / teardown state in switches")
        ]
    )
    
    create_content_slide(prs, "1.1.3 Delay, Loss & Throughput in Packet Networks", "M1.1 METRICS & DELAYS", [
        ("Total Nodal Delay", "Sum of 4 fundamental delay components: $d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$."),
        ("Nodal Processing Delay ($d_{proc}$)", "Time required to inspect packet header, verify bit-level checksums, and determine output link (typically microseconds)."),
        ("Queuing Delay ($d_{queue}$)", "Time packet waits in output buffer for link transmission. Depends on traffic intensity $I = La / R$ ($I \\to 1 \\Rightarrow$ queue grows exponentially)."),
        ("Transmission Delay ($d_{trans}$)", "Time to push all packet bits onto link: $d_{trans} = L / R$ ($L$ = Packet bits, $R$ = Link bandwidth in bps)."),
        ("Propagation Delay ($d_{prop}$)", "Time for a bit to travel physically across link: $d_{prop} = d / s$ ($d$ = distance in meters, $s$ = propagation speed $\\approx 2 \\times 10^8$ m/s)."),
        ("Packet Loss & Throughput", "When buffer queues overflow, arriving packets are dropped. End-to-end throughput is bottlenecked by the slowest link on the path.")
    ], "Exam Formulas", [
        "d_trans = L / R (sec)",
        "d_prop = d / s (sec)",
        "Traffic Intensity: I = (L * a) / R",
        "If I > 1: Queue grows infinitely",
        "Throughput = min(R1, R2, ..., Rn)"
    ])
    
    return prs

def build_m1_2(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.2", "Protocol Layering & Network Models",
        "Layering Principles, OSI 7-Layer Architecture, TCP/IP 5-Layer Stack, Encapsulation & PDUs",
        "Module 1"
    )
    
    create_content_slide(prs, "1.2.1 Protocol Layering Principles", "M1.2 PROTOCOL LAYERING", [
        ("Modular Architecture", "Complex networking tasks are divided into distinct functional layers. Each layer relies on services from the layer below and provides services to the layer above."),
        ("Layer Independence", "Changes in the internal implementation of one layer do not affect other layers, provided the inter-layer interface remains unchanged."),
        ("Encapsulation & Decapsulation", "As data travels down the stack at the sender, each layer prepends a header (and sometimes a trailer). At receiver, headers are stripped sequentially."),
        ("Protocol Data Units (PDU)", "L5: Message (App) $\\to$ L4: Segment (TCP) / Datagram (UDP) $\\to$ L3: Packet/Datagram (IP) $\\to$ L2: Frame (Ethernet) $\\to$ L1: Bits (Physical).")
    ], "Key Advantages", [
        "Modularity simplifies design",
        "Standardized interfaces",
        "Interoperability across vendors",
        "Easy maintenance and upgrades"
    ])
    
    create_comparison_slide(prs, "1.2.2 Model Comparison: OSI 7-Layer vs TCP/IP Stack", "M1.2 OSI VS TCP/IP",
        "OSI Reference Model (ISO)", [
            ("7. Application", "User network interfaces (HTTP, FTP)"),
            ("6. Presentation", "Data translation, compression, encryption"),
            ("5. Session", "Dialog control & synchronization checkpoints"),
            ("4. Transport", "End-to-end process delivery & flow/error control"),
            ("3. Network", "Routing & logical addressing across networks"),
            ("2. Data Link", "Node-to-node framing & MAC error control"),
            ("1. Physical", "Bit stream transmission over raw media")
        ],
        "TCP/IP Internet Stack (Practical)", [
            ("5. Application", "Combines OSI L7, L6, and L5 functions"),
            ("4. Transport", "Process-to-process delivery (TCP, UDP)"),
            ("3. Network (Internet)", "Host-to-host routing (IPv4, IPv6, ICMP)"),
            ("2. Data Link", "Hardware frame delivery (Ethernet, Wi-Fi)"),
            ("1. Physical", "Cable signals, optical pulses, radio waves")
        ]
    )
    
    create_content_slide(prs, "1.2.3 PDU Encapsulation & Addressing Hierarchy", "M1.2 ADDRESSING & PDUs", [
        ("Application Layer (L5)", "PDU: Message. Uses Port Numbers (16-bit) and URLs/Hostnames to address application endpoints."),
        ("Transport Layer (L4)", "PDU: Segment / Datagram. Adds Source & Destination Port Numbers (e.g., Port 80, 443, 53) for process-to-process multiplexing."),
        ("Network Layer (L3)", "PDU: Datagram / Packet. Adds Source & Destination IP Addresses (32-bit IPv4 / 128-bit IPv6) for global host-to-host routing."),
        ("Data Link Layer (L2)", "PDU: Frame. Adds Source & Destination MAC Addresses (48-bit physical) and CRC-32 Frame Check Sequence (FCS) trailer."),
        ("Physical Layer (L1)", "PDU: Bits. Encodes raw bit stream into voltages, light pulses, or RF carrier modulations.")
    ], "Addressing Summary", [
        "L5/L4: 16-bit Port (0-65535)",
        "L3: 32-bit IPv4 / 128-bit IPv6",
        "L2: 48-bit MAC (Hex notation)",
        "L1: Physical voltage/frequencies"
    ])
    
    return prs

def build_m1_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.3", "Application Layer Paradigms & Services",
        "Client-Server vs Peer-to-Peer (P2P), Transport Service Requirements for Applications",
        "Module 1"
    )
    
    create_comparison_slide(prs, "1.3.1 Application Architecture Paradigms", "M1.3 APP PARADIGMS",
        "Client-Server Architecture", [
            ("Server Host", "Always-on host with permanent, well-known IP address"),
            ("Client Hosts", "Communicate with server; intermittent connections; dynamic IPs"),
            ("Scalability", "Server can become bottleneck; requires data centers / load balancers"),
            ("Control", "Centralized control, security, and authentication"),
            ("Examples", "Web (HTTP), Email (SMTP/IMAP), File Transfer (FTP)")
        ],
        "Peer-to-Peer (P2P) Architecture", [
            ("Peers", "Arbitrary end systems communicate directly without dedicated server"),
            ("Self-Scalability", "New peers bring service capacity as well as demand"),
            ("Decentralization", "No single point of failure; resilient against server outages"),
            ("Management", "Complex churn handling (peers join and leave arbitrarily)"),
            ("Examples", "BitTorrent, Gnutella, Blockchain networks")
        ]
    )
    
    create_content_slide(prs, "1.3.2 Transport Services Required by Applications", "M1.3 TRANSPORT REQUIREMENTS", [
        ("Reliable Data Transfer", "Financial, web, and email apps require 100% loss-free transfer (TCP). Loss-tolerant audio/video can accept minor loss (UDP)."),
        ("Throughput / Bandwidth Guarantees", "Bandwidth-sensitive apps (VoIP, 4K video) need minimum throughput guarantees. Elastic apps adapt to available bandwidth."),
        ("Timing & Latency Constraints", "Interactive games and video conferencing require tight bounds on end-to-end delay (e.g. < 150ms)."),
        ("Security & Encryption", "Confidentiality, data integrity, and endpoint authentication provided by Transport Layer Security (TLS/HTTPS)."),
        ("Socket Abstraction", "The software interface through which application processes send and receive data over the network stack.")
    ], "Protocol Matching", [
        "Web (HTTP): TCP (Port 80/443)",
        "Email (SMTP): TCP (Port 25/587)",
        "DNS: UDP (Port 53) [Low latency]",
        "Streaming: UDP / RTP (or DASH/TCP)",
        "FTP: TCP (Ports 20 & 21)"
    ])
    
    return prs

def build_m1_4(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.4", "World Wide Web & HTTP Architecture",
        "HTTP/1.0, HTTP/1.1 Persistent Pipelining, HTTP/2 Binary Multiplexing, HTTP/3, Methods, Status Codes & Caching",
        "Module 1"
    )
    
    create_content_slide(prs, "1.4.1 HTTP Protocol Fundamentals", "M1.4 HTTP OVERVIEW", [
        ("HyperText Transfer Protocol (HTTP)", "Application-layer request-response protocol running over TCP (Port 80 HTTP, Port 443 HTTPS)."),
        ("Stateless Nature", "Server maintains no information about past client requests. Cookies and sessions add state on top of HTTP."),
        ("HTTP Request Message", "Consists of Request Line (`METHOD URL VERSION`), Header Lines (`Host:`, `User-Agent:`, `Accept:`), Blank Line (`\\r\\n`), and Entity Body (in POST)."),
        ("HTTP Response Message", "Consists of Status Line (`VERSION STATUS_CODE PHRASE`), Header Lines (`Content-Type:`, `Content-Length:`, `Set-Cookie:`), Blank Line, and Entity Body."),
        ("HTTP Methods", "GET (retrieve data), POST (submit form/JSON), HEAD (fetch headers only), PUT (upload/replace resource), DELETE (remove resource).")
    ], "Key Status Codes", [
        "200 OK: Request succeeded",
        "301 Moved Permanently: Redirect",
        "304 Not Modified: Cache valid",
        "400 Bad Request: Malformed",
        "404 Not Found: Missing URL",
        "500 Internal Server Error"
    ])
    
    create_comparison_slide(prs, "1.4.2 HTTP Connections: Non-Persistent vs Persistent", "M1.4 HTTP CONNECTIONS",
        "Non-Persistent HTTP (HTTP/1.0)", [
            ("Connection Rule", "At most one object sent over a single TCP connection"),
            ("Overhead", "New TCP 3-way handshake for EVERY referenced object"),
            ("Response Time", "2 RTTs + Transmission Time per referenced object"),
            ("Server Load", "High OS overhead managing multiple short-lived sockets"),
            ("Parallel Connections", "Browsers open ~6 parallel connections to compensate")
        ],
        "Persistent HTTP (HTTP/1.1)", [
            ("Connection Rule", "Multiple objects sent over a SINGLE open TCP connection"),
            ("Pipelining", "Client sends subsequent requests without waiting for replies"),
            ("Response Time", "1 RTT for initial connection + 1 RTT per batch of objects"),
            ("Keep-Alive", "Header `Connection: keep-alive` prevents socket teardown"),
            ("Head-of-Line Blocking", "Slow first response blocks subsequent queued objects")
        ]
    )
    
    create_content_slide(prs, "1.4.3 HTTP Evolution: HTTP/2 & HTTP/3 & Web Caching", "M1.4 HTTP/2 & CACHING", [
        ("HTTP/2 Innovations (RFC 7540)", "Replaces plain text with Binary Framing Layer. Introduces Stream Multiplexing: multiple requests/responses interleaved over one TCP connection without Head-of-Line (HoL) blocking."),
        ("Header Compression & Server Push", "HPACK algorithm compresses redundant headers across requests. Server Push proactively sends required assets (CSS/JS) before client requests them."),
        ("HTTP/3 over QUIC (RFC 9000)", "Runs over UDP instead of TCP. Eliminates TCP-level Head-of-Line blocking and achieves zero-RTT connection resumption with integrated TLS 1.3."),
        ("Web Caching & Proxy Servers", "Proxy servers satisfy client requests from local storage without contacting origin server. Reduces response time and access link traffic."),
        ("Conditional GET (`If-Modified-Since`)", "Cache verifies freshness with origin server. If object unchanged, server returns `304 Not Modified` with zero entity body.")
    ], "HTTP Evolution Summary", [
        "HTTP/1.0: 1 Object per TCP",
        "HTTP/1.1: Persistent + Keep-Alive",
        "HTTP/2: Binary Multiplexing + Push",
        "HTTP/3: UDP (QUIC) + 0-RTT TLS",
        "Web Caching: Reduces ISP load"
    ])
    
    return prs

def build_m1_5(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.5", "File Transfer Protocol (FTP)",
        "Dual Connection Architecture, Out-of-Band Control, Active vs Passive Mode, Commands & Status Codes",
        "Module 1"
    )
    
    create_content_slide(prs, "1.5.1 FTP Dual-Channel Architecture", "M1.5 FTP ARCHITECTURE", [
        ("Two Parallel TCP Connections", "FTP separates control signalling from actual data transfer by utilizing two distinct TCP connections."),
        ("Control Connection (Port 21)", "Client connects to server port 21. Used for sending ASCII commands (`USER`, `PASS`, `LIST`, `RETR`, `STOR`) and receiving 3-digit status codes. Remains open throughout session."),
        ("Data Connection (Port 20 / Ephemeral)", "Created dynamically whenever a file transfer or directory listing is requested. Closed immediately upon file transfer completion."),
        ("Out-of-Band Control", "Because control information is sent on a completely separate connection from data, FTP is termed an 'Out-of-Band' control protocol (unlike HTTP which is in-band)."),
        ("Stateful Server", "FTP server maintains state about client (current directory, authentication state, transfer parameters).")
    ], "Key FTP Commands", [
        "USER <username>: Login ID",
        "PASS <password>: Auth",
        "LIST: Request directory listing",
        "RETR <filename>: Download file",
        "STOR <filename>: Upload file",
        "QUIT: Close session"
    ])
    
    create_comparison_slide(prs, "1.5.2 FTP Modes: Active vs Passive (PASV)", "M1.5 ACTIVE VS PASSIVE",
        "Active Mode FTP (Standard)", [
            ("Step 1", "Client connects from port N to Server Port 21 (Control)"),
            ("Step 2", "Client sends `PORT` command telling server its IP and port M"),
            ("Step 3", "Server initiates data connection from Port 20 to Client Port M"),
            ("Firewall Issue", "Client-side firewall blocks incoming connection from server port 20"),
            ("Best For", "Clients with direct public IP addresses")
        ],
        "Passive Mode FTP (PASV - Modern)", [
            ("Step 1", "Client connects from port N to Server Port 21 (Control)"),
            ("Step 2", "Client sends `PASV` command to server"),
            ("Step 3", "Server opens random unprivileged port P and tells client"),
            ("Step 4", "Client initiates data connection from port N+1 to Server port P"),
            ("Firewall Friendly", "All connections initiated outbound by client")
        ]
    )
    
    return prs

def build_m1_6(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.6", "Electronic Mail (SMTP, POP3, IMAP, MIME)",
        "Email Architecture, Push vs Pull Models, Simple Mail Transfer Protocol, POP3 vs IMAP4 & MIME Encoding",
        "Module 1"
    )
    
    create_content_slide(prs, "1.6.1 Electronic Mail Architecture & SMTP", "M1.6 EMAIL ARCHITECTURE", [
        ("Three Core Components", "User Agents (UA: Mail readers like Outlook, Thunderbird), Mail Servers (contain mailboxes & outgoing message spools), and Transfer Protocols."),
        ("SMTP (Simple Mail Transfer Protocol)", "Standard push protocol for transferring email messages reliably between mail servers over TCP (Port 25 standard, 587 submission)."),
        ("SMTP Push Mechanism", "Sender User Agent pushes email to Sender Mail Server via SMTP $\\to$ Sender Mail Server pushes email directly to Recipient Mail Server via SMTP."),
        ("Connection Phases", "Three phases: Handshake (`HELO` / `EHLO`), Message Transfer (`MAIL FROM:`, `RCPT TO:`, `DATA`), and Closure (`QUIT`)."),
        ("7-Bit ASCII Limitation", "Original SMTP body restricted to plain 7-bit ASCII characters. Multimedia require MIME extensions.")
    ], "SMTP Commands", [
        "HELO / EHLO: Client greeting",
        "MAIL FROM: Identifies sender",
        "RCPT TO: Identifies recipient",
        "DATA: Begins email body text",
        ". (Single dot on line): Ends body",
        "QUIT: Terminates connection"
    ])
    
    create_comparison_slide(prs, "1.6.2 Mail Access Protocols: POP3 vs IMAP4", "M1.6 POP3 VS IMAP4",
        "POP3 (Post Office Protocol v3 - Port 110)", [
            ("Paradigm", "Download-and-delete / Download-and-keep mode"),
            ("Folder Management", "Messages downloaded locally; cannot create server folders"),
            ("Multi-Device Sync", "Poor; state changes on one device not reflected on others"),
            ("Server Storage", "Minimal server storage required; client maintains local archive"),
            ("Statelessness", "Stateless across client sessions")
        ],
        "IMAP4 (Internet Message Access Protocol - Port 143)", [
            ("Paradigm", "Remote message management on server"),
            ("Folder Management", "Allows creating, renaming, and nesting folders on server"),
            ("Multi-Device Sync", "Perfect synchronization across phone, laptop, webmail"),
            ("Partial Download", "Allows fetching message headers before downloading body"),
            ("Stateful", "Server tracks read, flagged, and deleted states")
        ]
    )
    
    create_content_slide(prs, "1.6.3 MIME (Multipurpose Internet Mail Extensions)", "M1.6 MIME EXTENSIONS", [
        ("Motivation", "Enables sending non-ASCII data (images, audio, video, attachments, non-English character sets) across standard 7-bit ASCII SMTP infrastructure."),
        ("MIME Header Extensions", "`MIME-Version: 1.0`, `Content-Type:` (e.g. `text/html`, `image/jpeg`, `multipart/mixed`), `Content-Transfer-Encoding:`."),
        ("Base64 Encoding", "Converts arbitrary binary data into 6-bit chunks mapped to 64 printable ASCII characters (`A-Z`, `a-z`, `0-9`, `+`, `/`). Every 3 binary bytes produce 4 ASCII chars (33% overhead)."),
        ("Quoted-Printable Encoding", "Used for text with few non-ASCII characters; non-ASCII byte represented as `=XX` (hex)."),
        ("Multipart MIME", "Allows single email message to contain plain text, HTML version, and multiple attached binary files separated by a boundary string.")
    ], "Push vs Pull Summary", [
        "Sender UA -> Sender Server: SMTP (Push)",
        "Sender Server -> Recv Server: SMTP (Push)",
        "Recv Server -> Recv UA: POP3/IMAP (Pull)",
        "Webmail: HTTP between UA and Server"
    ])
    
    return prs

def build_m1_7(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.7", "Domain Name System (DNS)",
        "Hierarchical Namespace, Root & TLD Servers, Recursive vs Iterative Resolution, Resource Records & Caching",
        "Module 1"
    )
    
    create_content_slide(prs, "1.7.1 DNS Hierarchy & Architecture", "M1.7 DNS HIERARCHY", [
        ("DNS Role", "Distributed, hierarchical database that translates human-friendly hostnames (e.g. `www.vjcet.ac.in`) into 32-bit IPv4 or 128-bit IPv6 machine addresses. Operates over UDP/TCP Port 53."),
        ("Root DNS Servers", "Top of DNS tree. 13 logical root server addresses (replicated globally via Anycast routing). Returns TLD server referrals."),
        ("Top-Level Domain (TLD) Servers", "Manage top-level domains: Generic TLDs (`.com`, `.org`, `.edu`) and Country-code TLDs (`.in`, `.uk`, `.us`). Returns authoritative server referrals."),
        ("Authoritative DNS Servers", "Maintained by organizations/service providers. Stores actual mappings for organization's publicly accessible hosts."),
        ("Local DNS Resolvers", "Operated by ISPs / enterprise networks. Intercepts host queries and performs DNS tree resolution on behalf of the client.")
    ], "DNS Server Hierarchy", [
        "1. Root DNS Servers (13)",
        "2. TLD Servers (.com, .in, .edu)",
        "3. Authoritative Servers (vjcet.ac.in)",
        "4. Local Resolvers (ISP / 8.8.8.8)"
    ])
    
    create_comparison_slide(prs, "1.7.2 DNS Query Resolution: Recursive vs Iterative", "M1.7 RESOLUTION METHODS",
        "Recursive DNS Resolution", [
            ("Client Burden", "Client/resolver offloads full lookup work to queried server"),
            ("Process", "Server contacts other servers sequentially until answer found"),
            ("Root Server Impact", "Places heavy processing & memory burden on higher servers"),
            ("Usage", "Standard between Client Host and Local DNS Resolver")
        ],
        "Iterative DNS Resolution", [
            ("Referral Model", "Queried server responds immediately with 'I do not know, ask this server next'"),
            ("Process", "Local resolver contacts Root -> TLD -> Authoritative itself"),
            ("Root Server Impact", "Lightweight; preserves root/TLD server capacity"),
            ("Usage", "Standard among Local Resolver, Root, and TLD servers")
        ]
    )
    
    create_content_slide(prs, "1.7.3 DNS Resource Records (RR) & Caching", "M1.7 DNS RECORDS & CACHE", [
        ("Resource Record Format", "Stored as 4-tuple: `(Name, Value, Type, TTL)`."),
        ("Type A", "`Name` is hostname, `Value` is IPv4 address (e.g. `vjcet.ac.in -> 103.112.212.10`)."),
        ("Type AAAA", "`Name` is hostname, `Value` is IPv6 address."),
        ("Type CNAME", "`Name` is alias hostname, `Value` is canonical real hostname (e.g. `www.vjcet.ac.in -> vjcet.ac.in`)."),
        ("Type MX", "`Name` is domain name, `Value` is mail server hostname handling email for domain."),
        ("Type NS", "`Name` is domain name, `Value` is authoritative name server hostname."),
        ("DNS Caching", "Resolvers cache learned RRs for duration specified by TTL (Time-to-Live). Drastically reduces internet latency and root server load.")
    ], "Key Record Types", [
        "A: Hostname -> IPv4",
        "AAAA: Hostname -> IPv6",
        "CNAME: Alias -> Canonical Name",
        "MX: Domain -> Mail Server",
        "NS: Domain -> Authoritative Server",
        "TTL: Cache validity time (sec)"
    ])
    
    return prs

def build_m1_8(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.8", "Peer-to-Peer Paradigm & BitTorrent Case Study",
        "P2P Scalability Analysis, BitTorrent Swarming, Trackers, Rarest-First Chunk Selection & Tit-for-Tat Choking",
        "Module 1"
    )
    
    create_content_slide(prs, "1.8.1 P2P vs Client-Server File Distribution Scalability", "M1.8 P2P SCALABILITY", [
        ("File Distribution Problem", "Distribute a large file of size $F$ bits from a single server to $N$ independent peers/clients."),
        ("Client-Server Distribution Time", "$D_{C-S} \\ge \\max \\left( \\frac{NF}{u_s}, \\frac{F}{d_{min}} \\right)$. Time increases LINEARLY with $N$. As $N \\to \\infty$, server upload link becomes the fatal bottleneck."),
        ("P2P Distribution Time", "$D_{P2P} \\ge \\max \\left( \\frac{F}{u_s}, \\frac{F}{d_{min}}, \\frac{NF}{u_s + \\sum_{i=1}^N u_i} \\right)$."),
        ("Self-Scalability Principle", "Each new peer downloading the file ALSO contributes its upload capacity $u_i$ to assist other peers, keeping distribution time bounded.")
    ], "Scalability Comparison", [
        "Client-Server: O(N) linear growth",
        "P2P: Sub-linear, asymptotically bounded",
        "u_s: Server upload capacity",
        "d_min: Minimum client download speed",
        "sum(u_i): Aggregate peer upload rate"
    ])
    
    create_content_slide(prs, "1.8.2 BitTorrent Architecture & Swarm Coordination", "M1.8 BITTORRENT ARCHITECTURE", [
        ("BitTorrent Fundamentals", "A popular P2P protocol for distributing large files efficiently across thousands of cooperating peers."),
        ("Torrent & Chunks", "Target file is split into fixed-size chunks (typically 256 KB). A `.torrent` metadata file contains chunk cryptographic hashes and tracker URL."),
        ("Tracker & Swarm", "A centralized server (or distributed DHT) that tracks all peers currently downloading/uploading the torrent. The collection of participating peers is the 'Swarm'."),
        ("Leechers vs Seeders", "Leechers: Peers still downloading missing chunks while uploading acquired ones. Seeders: Peers possessing 100% of file chunks who remain online solely to upload.")
    ], "BitTorrent Components", [
        "Torrent File: Metadata descriptor",
        "Tracker: Coordinates active peer list",
        "Swarm: Entire pool of active peers",
        "Chunks: 256 KB file fragments",
        "SHA-1 Hashes: Verify chunk integrity"
    ])
    
    create_content_slide(prs, "1.8.3 BitTorrent Algorithms: Rarest-First & Tit-for-Tat", "M1.8 BITTORRENT ALGORITHMS", [
        ("Rarest-First Chunk Selection", "Peers determine which chunks are least common among their connected neighbors and request those first. Prevents rarest chunks from disappearing and maximizes chunk diversity."),
        ("Tit-for-Tat (TFT) Choking Algorithm", "Incentivizes uploading. Peer measures upload rates from all neighbors and 'unchokes' the top 4 fastest uploaders. Other neighbors are 'choked' (no data sent). Re-evaluated every 10s."),
        ("Optimistic Unchoking", "Every 30 seconds, a peer randomly unchokes one additional choked neighbor. Allows discovering new peers with potentially faster upload speeds and lets newly joined leechers acquire their first chunk."),
        ("Free-Rider Mitigation", "Tit-for-Tat discourages free-riders (peers that download without uploading) by starving them of high-speed data feeds.")
    ], "Key Takeaways", [
        "Rarest-First: Balances chunk supply",
        "Top 4 Unchoked: Rewards fast peers",
        "Optimistic Unchoke: Discovers new links",
        "TFT cycle: 10s; Opt unchoke: 30s"
    ])
    
    return prs

def build_m1_9(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.9", "Application Layer Case Study & Socket Mapping",
        "Comprehensive Protocol Comparison, Port Addressing Summary, and Socket API Interface Mapping",
        "Module 1"
    )
    
    create_comparison_slide(prs, "1.9.1 Master Protocol Comparison Matrix", "M1.9 PROTOCOL MATRIX",
        "Web & File Transfer Protocols", [
            ("HTTP/1.1", "TCP Port 80, In-band, Stateless, Persistent"),
            ("HTTP/2 & HTTP/3", "TCP/443 & UDP/443, Multiplexed, Binary"),
            ("FTP Control", "TCP Port 21, Out-of-band, Stateful"),
            ("FTP Data", "TCP Port 20 (or Ephemeral), Closed per file"),
            ("DNS", "UDP Port 53 (TCP for zone transfers), Hierarchical")
        ],
        "Email & P2P Protocols", [
            ("SMTP", "TCP Port 25/587, Push model, 7-bit ASCII"),
            ("POP3", "TCP Port 110, Pull model, Download & Delete"),
            ("IMAP4", "TCP Port 143, Pull model, Remote folder sync"),
            ("BitTorrent", "P2P over TCP/UDP, Swarm-based, Tit-for-Tat"),
            ("MIME", "Encapsulation header & Base64 binary encoding")
        ]
    )
    
    create_content_slide(prs, "1.9.2 Socket Interface & Application Layer Integration", "M1.9 SOCKET INTEGRATION", [
        ("Socket as Application Doorway", "Application processes interact with the operating system networking stack via the Berkeley Socket API."),
        ("Transport Choice Binding", "App chooses `SOCK_STREAM` (TCP for reliability, order, flow control) or `SOCK_DGRAM` (UDP for speed, low overhead, multicasting)."),
        ("Port Number Binding", "Servers bind to well-known ports (< 1024, root privilege) while clients are assigned ephemeral ports (49152 - 65535)."),
        ("Application Layer Framing", "Because TCP is a continuous byte-stream without message boundaries, application protocols must implement their own framing (e.g. `\\r\\n\\r\\n` delimiter in HTTP, `Content-Length:` header, or ASN.1 TLV).")
    ], "Module 1 Review", [
        "Edge vs Core & Delays",
        "OSI 7 vs TCP/IP 5 Layers",
        "Client-Server vs P2P Models",
        "HTTP, FTP, SMTP, DNS, P2P",
        "All KTU CO1 Topics Covered"
    ])
    
    return prs

def build_module_1_master(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "MODULE 1", "Application Layer & Peer-to-Peer Paradigms",
        "Complete Lecture & Revision Master Deck (M1.1 to M1.9)",
        "Module 1 Complete"
    )
    build_m1_1(prs)
    build_m1_2(prs)
    build_m1_3(prs)
    build_m1_4(prs)
    build_m1_5(prs)
    build_m1_6(prs)
    build_m1_7(prs)
    build_m1_8(prs)
    build_m1_9(prs)
    return prs
