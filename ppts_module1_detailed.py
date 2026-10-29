"""
ppts_module1_detailed.py
Comprehensive, classroom-ready presentation decks for Module 1: Application Layer & Internet Fundamentals.
Prepared exclusively for:
Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
PCCST501 Computer Networks (KTU 2024 Scheme)
"""

from build_master_ppts_framework import (
    init_prs, create_title_slide, create_content_slide, 
    create_comparison_slide, create_numerical_slide, create_code_slide, create_exam_booster_slide
)

def build_m1_1(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.1", "Overview of the Internet Architecture & Performance Metrics",
        "Network Edge, Network Core, Packet vs Circuit Switching, Delay Models, Queuing Loss & Throughput Bottlenecks",
        "Module 1"
    )
    
    create_content_slide(prs, "1.1.1 The Internet: Structural Hierarchy", "M1.1 INTERNET OVERVIEW", [
        ("The Internet: Network of Networks", "A vast, distributed interconnection of billions of heterogeneous computing devices (end systems / hosts) running networked software."),
        ("Network Edge", "End systems (clients, servers, mobile, IoT devices) that generate and consume application data. Connected via Access Networks (DSL, FTTH, 4G/5G, Wi-Fi 6)."),
        ("Network Core", "The mesh of interconnected packet switches (routers and link-layer switches) responsible for routing and forwarding data across global ISP tiers."),
        ("ISP Tier Hierarchy", "Tier-1 ISPs (global transit providers like Lumen, AT&T), connected via IXPs (Internet Exchange Points), supplying regional and local access ISPs."),
        ("Protocols & Standards", "Network protocols define message format, ordering, transmission rules, and error handling. Governed by IETF RFCs and IEEE standards.")
    ], "Key Structural Layers", [
        "Tier-1 ISPs: Global backbone",
        "IXPs: Free/peered routing exchange",
        "Regional ISPs: Connect local access",
        "Access Nets: DSL, PON/Fiber, Wireless",
        "End Systems: Run user applications"
    ])
    
    create_comparison_slide(prs, "1.1.2 Switching Paradigms: Packet vs Circuit Switching", "M1.1 SWITCHING COMPARISON",
        "Packet Switching (Internet)", [
            ("Data Unit", "Discrete chunks called packets (Header + Payload)"),
            ("Multiplexing", "Statistical Multiplexing — resources allocated on demand"),
            ("Link Utilization", "High efficiency; handles bursty internet traffic seamlessly"),
            ("Delays & Loss", "Queuing delay occurs; buffers drop packets on congestion"),
            ("State Maintenance", "Stateless core routers; adaptive per-packet dynamic routing")
        ],
        "Circuit Switching (Legacy PSTN)", [
            ("Data Unit", "Continuous bit stream over reserved physical channel"),
            ("Multiplexing", "Fixed allocation via FDM (Frequency) or TDM (Time) slots"),
            ("Link Utilization", "Low; reserved bandwidth wasted during idle/silent periods"),
            ("Delays & Loss", "Zero queuing delay; calls blocked if no circuit available"),
            ("State Maintenance", "Dedicated call setup and teardown state in every switch")
        ]
    )
    
    create_content_slide(prs, "1.1.3 Mathematical Delay Models in Packet Networks", "M1.1 NODAL DELAY", [
        ("Total Nodal Delay ($d_{nodal}$)", "Sum of 4 fundamental delay components at each intermediate router hop: $d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$."),
        ("Nodal Processing Delay ($d_{proc}$)", "Time taken by router CPU to inspect packet header, compute bit checksums, and determine output interface (microseconds)."),
        ("Queuing Delay ($d_{queue}$)", "Time packet waits inside output buffer queue before transmission. Governed by Traffic Intensity $I = (L \\cdot a) / R$ ($L$ = bits, $a$ = arrival rate, $R$ = bandwidth)."),
        ("Transmission Delay ($d_{trans}$)", "Time required to push all $L$ bits of the packet onto the link at rate $R$: $d_{trans} = L / R$ seconds."),
        ("Propagation Delay ($d_{prop}$)", "Time for a physical bit to travel through the physical medium over distance $d$ at speed $s \\approx 2 \\times 10^8$ m/s in copper/fiber: $d_{prop} = d / s$ seconds."),
        ("Packet Loss & Throughput", "When arriving traffic exceeds buffer capacity, packet drop occurs. End-to-end throughput is bottlenecked by the minimum link capacity along the transmission path.")
    ], "Delay Formulas", [
        "d_nodal = d_proc + d_queue + d_trans + d_prop",
        "d_trans = L / R (sec)",
        "d_prop = d / s (sec)",
        "Traffic Intensity: I = (L * a) / R",
        "If I -> 1: Queuing delay -> infinity",
        "Bottleneck Throughput = min(R1, R2, ...)"
    ])
    
    create_numerical_slide(
        prs, "1.1.4 Worked KTU Numerical: Delay & Throughput", "M1.1 WORKED PROBLEM",
        "A 1500-byte packet is transmitted over a 100 km fiber link with transmission rate R = 10 Mbps. Propagation speed in fiber is s = 2 * 10^8 m/s. Nodal processing delay is 5 microseconds and the router queue currently holds 2 packets of 1500 bytes each. Calculate: (a) Transmission delay, (b) Propagation delay, (c) Queuing delay, (d) Total nodal delay.",
        [
            "L = 1500 bytes = 1500 * 8 = 12,000 bits",
            "R = 10 Mbps = 10 * 10^6 bps",
            "d = 100 km = 10^5 m, s = 2 * 10^8 m/s",
            "d_trans = L / R, d_prop = d / s, d_queue = 2 * (L / R)"
        ],
        [
            (1, "d_trans = 12,000 / 10^7 = 1.2 * 10^-3 s = 1.2 ms"),
            (2, "d_prop = 10^5 / (2 * 10^8) = 0.5 * 10^-3 s = 0.5 ms"),
            (3, "d_queue = 2 * 1.2 ms = 2.4 ms (2 packets ahead in queue)"),
            (4, "d_proc = 5 microseconds = 0.005 ms"),
            (5, "d_nodal = 0.005 + 2.4 + 1.2 + 0.5 = 4.105 ms")
        ],
        "Total Nodal Delay = 4.105 ms (Queuing delay is dominant)",
        "In university exams, always convert bytes to bits (multiply by 8) before dividing by transmission rate R (bps)."
    )
    
    create_exam_booster_slide(
        prs, "M1.1", "Internet Architecture & Delay Models", "K2 / K3 Apply",
        [
            "Differentiate between packet switching and circuit switching with respect to bandwidth utilization, delays, and state maintenance. (7 Marks)",
            "Derive the four components of nodal delay in packet-switched networks with mathematical equations and units. (7 Marks)",
            "Explain statistical multiplexing and explain why traffic intensity I > 1 causes buffer overflow and packet loss. (5 Marks)"
        ],
        [
            "Packet switching enables statistical multiplexing without dedicated circuits.",
            "Transmission delay (L/R) depends on bandwidth; Propagation delay (d/s) depends on distance.",
            "Queuing delay grows non-linearly as traffic intensity I = (L*a)/R approaches 1.",
            "End-to-end throughput is always throttled by the bottleneck link on the path."
        ]
    )
    return prs

def build_m1_2(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.2", "Protocol Layering & Network Models",
        "Layering Principles, OSI 7-Layer Reference Model, TCP/IP 5-Layer Stack, PDU Encapsulation & Addressing Hierarchy",
        "Module 1"
    )
    
    create_content_slide(prs, "1.2.1 Principles of Layered Network Architecture", "M1.2 PROTOCOL LAYERING", [
        ("Modularity & Abstraction", "Dividing the massive complexity of network communication into decoupled functional layers. Each layer provides well-defined services to the layer above."),
        ("Layer Independence", "The internal implementation of a layer protocol can be completely modified or replaced without affecting adjacent layers as long as the layer interface remains unchanged."),
        ("Encapsulation at Sender", "Data moves top-down; each layer adds its own Protocol Header (and L2 adds a trailer) containing control metadata (addresses, sequence numbers, checksums)."),
        ("Decapsulation at Receiver", "Data moves bottom-up; each layer processes and strips its corresponding header, passing the demultiplexed payload to the upper layer."),
        ("Protocol Data Unit (PDU) Terminology", "L5: Message (App) -> L4: Segment (TCP) / Datagram (UDP) -> L3: Packet / Datagram (IP) -> L2: Frame (Ethernet/Wi-Fi) -> L1: Raw Bit Stream.")
    ], "Benefits of Layering", [
        "Simplifies system design",
        "Standardizes interfaces",
        "Enables multi-vendor hardware",
        "Isolates layer troubleshooting",
        "Facilitates protocol evolution"
    ])
    
    create_comparison_slide(prs, "1.2.2 Comprehensive Architecture: OSI 7-Layer vs TCP/IP Stack", "M1.2 OSI VS TCP/IP",
        "OSI 7-Layer Model (ISO Conceptual)", [
            ("7. Application", "User applications & network services (HTTP, DNS)"),
            ("6. Presentation", "Data formatting, compression, encryption/decryption"),
            ("5. Session", "Dialog management, token coordination, checkpoints"),
            ("4. Transport", "End-to-end reliability, flow control, port addressing"),
            ("3. Network", "Logical host addressing (IP) & packet routing"),
            ("2. Data Link", "Node-to-node frame transfer & MAC error control"),
            ("1. Physical", "Unstructured bit transmission over raw copper/fiber/air")
        ],
        "TCP/IP 5-Layer Internet Stack (Practical)", [
            ("5. Application", "Integrates OSI L7, L6, L5; protocols: HTTP, SMTP, DNS"),
            ("4. Transport", "Process-to-process multiplexing: TCP (reliable) & UDP"),
            ("3. Network (Internet)", "Host-to-host delivery across networks: IPv4, IPv6, ICMP"),
            ("2. Data Link", "Hardware framing, MAC addressing: Ethernet, 802.11"),
            ("1. Physical", "Signals, voltages, optical pulses, RF frequencies")
        ]
    )
    
    create_content_slide(prs, "1.2.3 Addressing Hierarchy & PDU Encapsulation", "M1.2 ADDRESSING HIERARCHY", [
        ("Application Layer Addressing", "Uniform Resource Identifiers (URIs), Domain Names (FQDNs), and standardized Port Numbers."),
        ("Transport Layer Addressing (Port Numbers)", "16-bit Port Number (0 - 65,535). Well-known ports (0-1023: HTTP 80, HTTPS 443, SSH 22), Registered (1024-49151), Dynamic/Private (49152-65535)."),
        ("Network Layer Addressing (IP Addresses)", "Logical 32-bit IPv4 or 128-bit IPv6 address used for global routing across subnets and autonomous systems."),
        ("Data Link Layer Addressing (MAC Addresses)", "Physical 48-bit (6-byte) EUI-48 hardware address burned into the NIC (e.g., `00:1A:2B:3C:4D:5E`). Used strictly on the local link."),
        ("Cross-Layer Demultiplexing", "L2 Frame Type field identifies L3 (IPv4 0x0800, ARP 0x0806) -> L3 Protocol field identifies L4 (TCP 6, UDP 17) -> L4 Port identifies L5 application.")
    ], "Addressing Summary", [
        "Process ID: 16-bit Port Number",
        "Host ID: 32-bit / 128-bit IP",
        "NIC ID: 48-bit MAC Address",
        "L2 Type 0x0800 -> IPv4",
        "L3 Protocol 6 -> TCP",
        "L3 Protocol 17 -> UDP"
    ])
    
    create_exam_booster_slide(
        prs, "M1.2", "Protocol Layering & Network Models", "K2 Understand",
        [
            "Compare the OSI 7-Layer model with the TCP/IP 5-Layer stack. Explain why the Presentation and Session layers are merged in TCP/IP. (8 Marks)",
            "Illustrate the step-by-step PDU encapsulation and decapsulation process across all layers with a neat labeled diagram. (7 Marks)",
            "Explain the three-level addressing hierarchy (Port, IP, MAC) and describe how demultiplexing occurs at each layer. (6 Marks)"
        ],
        [
            "OSI is a conceptual model; TCP/IP is the practical architecture implemented across the Internet.",
            "Headers prepend metadata: Port at L4, IP at L3, MAC and CRC FCS trailer at L2.",
            "L2 MAC changes at every router hop; L3 Source and Destination IP remain unchanged end-to-end (without NAT)."
        ]
    )
    return prs

def build_m1_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.3", "Application Layer Paradigms & Requirements",
        "Client-Server vs P2P Architectures, Transport Service Needs (Integrity, Throughput, Timing, Security), Socket Interface",
        "Module 1"
    )
    
    create_comparison_slide(prs, "1.3.1 Application Paradigms: Client-Server vs P2P", "M1.3 APPLICATION PARADIGMS",
        "Client-Server Architecture", [
            ("Centralized Server", "Always-on host with fixed, well-known IP address"),
            ("Client Behavior", "Initiate requests on demand; clients do not speak to each other"),
            ("Scalability Limit", "Server upload capacity bottlenecks under massive simultaneous loads ($D_{CS} = \\max\\{N \\cdot F / u_s, F / d_i\\}$)"),
            ("Infrastructure Cost", "Requires massive data centers, load balancers, and CDN caching"),
            ("Examples", "Web (HTTP), Email (SMTP/IMAP), Remote Login (SSH)")
        ],
        "Peer-to-Peer (P2P) Architecture", [
            ("Decentralized Peers", "Arbitrary end systems communicate directly without dedicated central servers"),
            ("Self-Scalability", "Peers are both consumers (downloaders) and producers (uploaders) of data"),
            ("Scalability Formula", "Distribution time grows logarithmically: $D_{P2P} = \\max\\{F / u_s, F / d_{min}, N \\cdot F / (u_s + \\sum u_i)\\}$"),
            ("Challenges", "Churn (peers join/leave dynamically), security, ISP asymmetric bandwidth"),
            ("Examples", "BitTorrent, IPFS, Blockchain, Skype (original)")
        ]
    )
    
    create_content_slide(prs, "1.3.2 Transport Layer Service Requirements for Applications", "M1.3 TRANSPORT REQUIREMENTS", [
        ("Data Integrity / Reliability", "Loss-intolerant applications (Web documents, file transfer, email, banking) require 100% reliable transport (TCP). Loss-tolerant applications (audio/video streaming, VoIP) can tolerate slight packet loss (UDP)."),
        ("Throughput Guarantees", "Bandwidth-sensitive applications (HD video streaming, real-time conferencing) need minimum throughput guarantees. Elastic applications (Email, Web, FTP) make use of whatever bandwidth is available."),
        ("Timing / Latency Guarantees", "Interactive gaming and VoIP require tight upper bounds on end-to-end delay (e.g., < 150 ms) to prevent human-perceptible lag."),
        ("Security & Encryption", "Application data privacy, server authentication, and message integrity provided via TLS (Transport Layer Security) running on top of TCP (e.g., HTTPS, SMTPS)."),
        ("Transport Choice Mapping", "TCP: HTTP/1.1 (80), HTTPS (443), FTP (20/21), SMTP (25), SSH (22). UDP: DNS (53), SNMP (161), RTP/RTSP, DHCP (67/68), QUIC/HTTP3 (443).")
    ], "Service Classification", [
        "Reliability: TCP (Strict) vs UDP (Loss-tolerant)",
        "Timing: Sensitive (VoIP) vs Elastic (Email/Web)",
        "Security: TLS/SSL cryptographic wrapper",
        "Multiplexing: 16-bit Port numbers"
    ])
    
    create_exam_booster_slide(
        prs, "M1.3", "Application Paradigms & Requirements", "K2 Understand",
        [
            "Differentiate between Client-Server and Peer-to-Peer network paradigms with real-world examples. (6 Marks)",
            "Identify the transport service requirements (loss, throughput, timing, security) for HTTP, VoIP, DNS, and FTP. (6 Marks)",
            "Explain how the socket interface acts as an API bridge between application-layer user processes and kernel transport protocols. (5 Marks)"
        ],
        [
            "Client-Server has centralized control and fixed IP; P2P possesses self-scalability as each leecher becomes a seeder.",
            "TCP provides 100% reliable byte-stream delivery with flow and congestion control.",
            "UDP provides low-latency, lightweight datagram delivery without handshake or congestion throttling."
        ]
    )
    return prs

def build_m1_4(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.4", "World Wide Web & HTTP Protocol Suite",
        "HTTP/1.0, HTTP/1.1 (Persistent vs Non-Persistent, Pipelining), HTTP/2 (Binary Framing, Streams, Push), HTTP/3 (QUIC), Caching & Cookies",
        "Module 1"
    )
    
    create_content_slide(prs, "1.4.1 HTTP Protocol Fundamentals & Message Structure", "M1.4 HTTP OVERVIEW", [
        ("HTTP (HyperText Transfer Protocol)", "Stateless, application-layer request-response protocol operating over TCP (standard port 80, TLS encrypted HTTPS port 443)."),
        ("HTTP Request Structure", "Method (GET, POST, HEAD, PUT, DELETE) + Request-URI + HTTP-Version \\r\\n Header Lines (Host, User-Agent, Accept, Cookie) \\r\\n\\r\\n [Optional Entity Body]."),
        ("HTTP Response Structure", "HTTP-Version + Status Code (200 OK, 301 Moved, 304 Not Modified, 404 Not Found, 500 Server Error) + Status Phrase \\r\\n Headers (Content-Type, Content-Length, Set-Cookie, Cache-Control) \\r\\n\\r\\n [Data Body]."),
        ("Statelessness & State Management", "HTTP servers maintain no state across successive requests from the same client. State is tracked using Cookies (via `Set-Cookie` and `Cookie` headers) and Session Tokens."),
        ("Conditional GET & Web Caching", "Clients and Proxy Caches avoid re-transmitting unmodified objects using the `If-Modified-Since` request header. If object unchanged, server responds `304 Not Modified` with zero body bits.")
    ], "Key Status Codes", [
        "200 OK: Request succeeded",
        "301 Moved Permanently: Redirect",
        "304 Not Modified: Cache hit",
        "400 Bad Request: Syntax error",
        "404 Not Found: Resource absent",
        "503 Service Unavailable: Busy"
    ])
    
    create_comparison_slide(prs, "1.4.2 HTTP/1.0 vs HTTP/1.1 vs HTTP/2 vs HTTP/3", "M1.4 HTTP EVOLUTION",
        "HTTP/1.0 & HTTP/1.1", [
            ("1.0 Non-Persistent", "Opens fresh TCP connection per object ($2 \\cdot RTT$ per object); high latency"),
            ("1.1 Persistent", "Reuses single TCP connection for multiple objects; default `Keep-Alive`"),
            ("Pipelining", "Sends multiple requests without waiting for replies (suffers Head-of-Line blocking)")
        ],
        "HTTP/2 (RFC 7540)", [
            ("Binary Framing", "Replaces plain text with binary frame parser (Headers & Data frames)"),
            ("Multiplexing", "Interleaves streams over single TCP; eliminates HTTP Head-of-Line blocking"),
            ("Server Push", "Proactively pushes critical resources (CSS, JS) before client requests them"),
            ("HPACK", "Compresses redundant header fields")
        ],
        "HTTP/3 (QUIC / RFC 9000)", [
            ("QUIC over UDP", "Replaces TCP with QUIC transport layer over UDP"),
            ("Zero HoL Blocking", "Packet loss in one stream never stalls unrelated streams"),
            ("0-RTT Handshake", "Combines connection setup and TLS 1.3 cryptographic handshake in 1 round-trip")
        ]
    )
    
    create_numerical_slide(
        prs, "1.4.3 Worked KTU Numerical: Web Page Retrieval Time", "M1.4 WORKED PROBLEM",
        "A base HTML page references 8 small embedded JPEG images located on the same server. Round-Trip Time between client and server is RTT = 40 ms. Base HTML transmission time is negligible. Calculate total retrieval time for: (a) HTTP/1.0 Non-Persistent with sequential TCP connections, (b) HTTP/1.1 Persistent without pipelining, (c) HTTP/1.1 Persistent with pipelining.",
        [
            "Non-Persistent: 1 TCP Handshake (1 RTT) + 1 Request/Response (1 RTT) = 2 RTT per object",
            "Persistent without Pipelining: 1 TCP Handshake (1 RTT) + 1 RTT for Base + N * 1 RTT for images",
            "Persistent with Pipelining: 1 TCP Handshake (1 RTT) + 1 RTT for Base + 1 RTT for all images"
        ],
        [
            (1, "Total objects = 1 Base HTML + 8 Images = 9 objects."),
            (2, "(a) Non-Persistent: 9 objects * 2 RTT = 18 RTT = 18 * 40 ms = 720 ms."),
            (3, "(b) Persistent without Pipelining: 1 RTT (TCP setup) + 1 RTT (Base HTML) + (8 * 1 RTT) = 10 RTT = 10 * 40 ms = 400 ms."),
            (4, "(c) Persistent with Pipelining: 1 RTT (TCP setup) + 1 RTT (Base HTML) + 1 RTT (pipelined batch) = 3 RTT = 3 * 40 ms = 120 ms.")
        ],
        "Non-Persistent: 720 ms | Persistent: 400 ms | Pipelined: 120 ms",
        "Always remember: TCP 3-way handshake consumes 1 full RTT before any HTTP request can be transmitted."
    )
    
    create_exam_booster_slide(
        prs, "M1.4", "World Wide Web & HTTP", "K3 Apply",
        [
            "Explain the difference between non-persistent and persistent HTTP connections with timing diagrams. (7 Marks)",
            "What is Head-of-Line (HoL) blocking? How do HTTP/2 binary framing and HTTP/3 QUIC solve it? (8 Marks)",
            "Describe the mechanism of Web Caching using the Conditional GET request (`If-Modified-Since`). (5 Marks)"
        ],
        [
            "HTTP/1.0 incurs 2 RTT per object; HTTP/1.1 persistent reuses TCP connections to save handshakes.",
            "HTTP/2 multiplexes streams over 1 TCP connection using binary framing, but TCP packet loss stalls all streams.",
            "HTTP/3 runs over UDP with QUIC to provide independent stream streams and 0-RTT connection re-establishment.",
            "Web caches reduce traffic intensity on access links and drastically cut down end-user latency."
        ]
    )
    return prs

def build_m1_5(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.5", "FTP (File Transfer Protocol) Architecture",
        "Out-of-Band Control vs In-Band Data, Control Port 21 vs Data Port 20, Active Mode (PORT) vs Passive Mode (PASV), Stateful Operation",
        "Module 1"
    )
    
    create_content_slide(prs, "1.5.1 Dual-Channel Architecture of FTP (RFC 959)", "M1.5 FTP ARCHITECTURE", [
        ("Out-of-Band Control Connection (Port 21)", "FTP establishes a dedicated TCP connection on port 21 solely for control commands (USER, PASS, LIST, RETR, STOR, QUIT) and server status replies (e.g., 220, 331, 230). Remains open throughout session."),
        ("In-Band Data Connection (Port 20)", "A separate, independent TCP connection created strictly for data transfer (file upload/download, directory listings). Opened per file transfer and closed immediately upon completion."),
        ("Stateful Connection", "Unlike stateless HTTP, FTP servers maintain extensive session state: current working directory, authenticated user credentials, transfer mode (ASCII vs Binary), and client IP/port."),
        ("Security Limitations of Plain FTP", "Credentials and data transmitted in unencrypted cleartext. Modern secure alternatives: FTPS (FTP over TLS/SSL) and SFTP (SSH File Transfer Protocol).")
    ], "FTP Commands", [
        "USER / PASS: Authentication",
        "LIST: Directory listing",
        "RETR: Retrieve / Download file",
        "STOR: Store / Upload file",
        "TYPE A / I: ASCII / Binary mode",
        "QUIT: Close session"
    ])
    
    create_comparison_slide(prs, "1.5.2 Active Mode (`PORT`) vs Passive Mode (`PASV`)", "M1.5 ACTIVE VS PASSIVE",
        "Active Mode FTP (`PORT`)", [
            ("Control Channel", "Client connects from random port $N$ to Server Port 21"),
            ("Data Channel Initiation", "Client sends `PORT IP,p1,p2` command. Server initiates data connection from Server Port 20 to Client Port $P$"),
            ("Firewall Problem", "Client-side firewalls and NATs block inbound connections initiated by external servers"),
            ("Usage", "Legacy environments without client NAT firewalls")
        ],
        "Passive Mode FTP (`PASV`)", [
            ("Control Channel", "Client connects from random port $N$ to Server Port 21"),
            ("Data Channel Initiation", "Client sends `PASV` command. Server opens random port $M$ and replies with `227 Entering Passive Mode`"),
            ("Firewall Friendly", "Client initiates outbound connection to Server Port $M$; traversable through client NATs/firewalls"),
            ("Usage", "Standard default mode across modern Internet")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M1.5", "FTP Architecture & Modes", "K2 Understand",
        [
            "Explain why FTP is called an 'out-of-band' control protocol. How does it differ from HTTP? (6 Marks)",
            "Compare Active Mode and Passive Mode in FTP with step-by-step connection flow diagrams. Explain why Passive mode is preferred behind NAT firewalls. (8 Marks)"
        ],
        [
            "FTP separates control signaling (Port 21) from data bulk transfer (Port 20).",
            "In Active mode, server connects to client (fails behind client firewalls).",
            "In Passive mode, client connects to server's dynamically assigned high port (bypasses client NAT restrictions)."
        ]
    )
    return prs

def build_m1_6(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.6", "Electronic Mail Architecture & Protocols",
        "User Agents (UA), Mail Transfer Agents (MTA), SMTP Push Protocol (Port 25/587), MIME 7-Bit ASCII Encoding, POP3 vs IMAP4 vs Webmail",
        "Module 1"
    )
    
    create_content_slide(prs, "1.6.1 Email System Architecture & Message Flow", "M1.6 EMAIL ARCHITECTURE", [
        ("Core Components", "Three major components: User Agents (mail clients like Thunderbird, Outlook), Mail Servers (run mailboxes and outgoing message queues), and Mail Transfer Protocols."),
        ("SMTP (Simple Mail Transfer Protocol - RFC 5321)", "Push protocol operating over TCP port 25 (inter-server relay) and port 587 (client message submission with STARTTLS)."),
        ("End-to-End Delivery Flow", "Alice (UA) -> Alice's Mail Server (MTA) -> [Internet Relay via SMTP over TCP] -> Bob's Mail Server (MTA mailbox) -> Bob (UA via POP3/IMAP4/HTTPS)."),
        ("SMTP Push vs Pull Architecture", "SMTP pushes email from sender to receiver's server. Receiver cannot use SMTP to pull mail to their local client because client may not be online with fixed IP."),
        ("SMTP Message Format (RFC 5322)", "Header lines (`From:`, `To:`, `Subject:`, `Date:`) separated from Message Body by a blank line `\\r\\n`. Handled as 7-bit ASCII text.")
    ], "SMTP Command Flow", [
        "HELO / EHLO: Client intro",
        "MAIL FROM: Sender envelope",
        "RCPT TO: Recipient address",
        "DATA: Start message payload",
        ". (Single period): End of data",
        "QUIT: Terminate TCP session"
    ])
    
    create_comparison_slide(prs, "1.6.2 MIME Extensions & Mail Access: POP3 vs IMAP4", "M1.6 MIME & ACCESS PROTOCOLS",
        "MIME (Multipurpose Internet Mail Extensions)", [
            ("Purpose", "Allows non-ASCII binary data (images, audio, PDFs, attachments) over 7-bit ASCII SMTP"),
            ("MIME Headers", "`MIME-Version: 1.0`, `Content-Type: multipart/mixed; boundary=...`, `Content-Transfer-Encoding: base64`"),
            ("Base64 Encoding", "Converts 3 binary bytes (24 bits) into 4 printable ASCII characters (6 bits each; 33% overhead)")
        ],
        "Mail Access: POP3 vs IMAP4", [
            ("POP3 (Post Office Protocol v3)", "TCP Port 110. 'Download and Delete' mode — copies email to local device; no server synchronization"),
            ("IMAP4 (Internet Message Access Protocol)", "TCP Port 143. Retains all messages/folders on server; multi-device synchronization; supports partial retrieval (e.g., fetch headers only)"),
            ("Webmail (HTTP/HTTPS)", "User agent runs inside web browser; uses HTTPS to communicate with webmail server")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M1.6", "Electronic Mail Protocols", "K2 Understand",
        [
            "Explain why SMTP cannot be used by an end user to pull emails from the mail server. (5 Marks)",
            "Differentiate between POP3 and IMAP4 access protocols with respect to folder synchronization and multi-device access. (6 Marks)",
            "Explain the role of MIME in electronic mail. How does Base64 encoding convert 8-bit binary data to 7-bit ASCII? (6 Marks)"
        ],
        [
            "SMTP is strictly a push protocol; POP3 and IMAP4 are pull protocols.",
            "POP3 is simple and offline-oriented; IMAP4 maintains centralized state and synchronized folders across devices.",
            "MIME headers allow multimedia attachments; Base64 maps 3 binary bytes into 4 ASCII symbols."
        ]
    )
    return prs

def build_m1_7(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.7", "Domain Name System (DNS) Architecture",
        "Hierarchical Distributed Database, Root/TLD/Authoritative Servers, Iterative vs Recursive Queries, DNS Caching & TTL, Resource Records (RR)",
        "Module 1"
    )
    
    create_content_slide(prs, "1.7.1 DNS: Distributed Hierarchical Database", "M1.7 DNS ARCHITECTURE", [
        ("DNS Core Function", "Application-layer service translating human-readable hostnames (e.g., `www.vjcet.ac.in`) into 32-bit IPv4 / 128-bit IPv6 machine addresses."),
        ("Why Distributed & Hierarchical?", "A single centralized database would suffer single-point failure, massive traffic congestion, geographic distance delay, and impossible maintenance."),
        ("Root DNS Servers", "13 logical root server addresses (A through M, replicated worldwide via Anycast routing). Directs queries to appropriate TLD servers."),
        ("Top-Level Domain (TLD) Servers", "Responsible for generic TLDs (`.com`, `.org`, `.net`, `.edu`) and country-code ccTLDs (`.in`, `.uk`, `.de`, `.jp`)."),
        ("Authoritative DNS Servers", "Maintained by organizations/service providers containing the definitive, official mapping records for an institution's public hosts."),
        ("Local DNS Name Server (Resolver)", "ISP / Campus resolver (e.g., Google 8.8.8.8, Cloudflare 1.1.1.1) acting as proxy intermediary cache for client queries.")
    ], "DNS Hierarchy", [
        "Root Servers: Global root '.'",
        "TLD Servers: .com, .in, .org",
        "Authoritative: vjcet.ac.in",
        "Local Resolver: ISP DNS cache",
        "Runs on UDP Port 53"
    ])
    
    create_comparison_slide(prs, "1.7.2 DNS Resolution Mechanisms: Iterative vs Recursive", "M1.7 RESOLUTION COMPARISON",
        "Iterative DNS Query", [
            ("Client Interaction", "Local DNS server handles resolution"),
            ("Server Response", "Contacted server replies: 'I don't know the exact IP, but you should ask this next DNS server' (returns referral delegation)"),
            ("Query Load", "Local DNS server sequentially queries Root -> TLD -> Authoritative"),
            ("Server Burden", "Puts minimal load on Root and TLD server infrastructure")
        ],
        "Recursive DNS Query", [
            ("Server Action", "Contacted server takes full responsibility to obtain the final IP address on behalf of the requester"),
            ("Chain of Queries", "Client -> Local -> Root -> TLD -> Authoritative (and returns back up the chain)"),
            ("Server Burden", "Heavy connection holding state and CPU burden on high-level servers; generally restricted at Root/TLD"),
            ("Standard Practice", "Client to Local DNS is Recursive; Local DNS to Root/TLD/Authoritative is Iterative")
        ]
    )
    
    create_content_slide(prs, "1.7.3 DNS Resource Records (RR) & Message Caching", "M1.7 RESOURCE RECORDS", [
        ("Resource Record (RR) 4-Tuple Format", "`(Name, Value, Type, TTL)` stored in DNS database."),
        ("Type A Record", "`Name` = Hostname, `Value` = IPv4 Address (e.g., `(vjcet.ac.in, 117.211.89.5, A, 3600)`)."),
        ("Type AAAA Record", "`Name` = Hostname, `Value` = 128-bit IPv6 Address."),
        ("Type CNAME Record", "`Name` = Alias hostname, `Value` = Canonical / True hostname (e.g., `(www.vjcet.org, vjcet.ac.in, CNAME, 86400)`)."),
        ("Type NS Record", "`Name` = Domain, `Value` = Hostname of Authoritative Name Server for domain (e.g., `(vjcet.ac.in, ns1.vjcet.ac.in, NS, 86400)`)."),
        ("Type MX Record", "`Name` = Domain, `Value` = Hostname of Mail Server for domain (e.g., `(vjcet.ac.in, mail.vjcet.ac.in, MX, 3600)`)."),
        ("DNS Caching & TTL", "Resolvers cache mapping records for `TTL` seconds, dramatically reducing query delays and global root traffic.")
    ], "RR Summary Table", [
        "Type A: Hostname -> IPv4",
        "Type AAAA: Hostname -> IPv6",
        "Type CNAME: Alias -> Canonical",
        "Type NS: Domain -> Name Server",
        "Type MX: Domain -> Mail Server",
        "Type PTR: IP -> Hostname (Reverse)"
    ])
    
    create_exam_booster_slide(
        prs, "M1.7", "Domain Name System (DNS)", "K3 Apply",
        [
            "Draw and explain the step-by-step resolution process for `www.vjcet.ac.in` comparing Iterative and Recursive queries. (8 Marks)",
            "Explain the format and role of DNS Resource Records (A, AAAA, CNAME, NS, MX, PTR) with examples. (7 Marks)",
            "Why does DNS use UDP on port 53 for standard queries instead of TCP? When is TCP used in DNS? (5 Marks)"
        ],
        [
            "Standard DNS uses UDP port 53 for fast 1-round-trip resolution without 3-way handshake overhead.",
            "TCP port 53 is used for DNS Zone Transfers between primary/secondary servers and responses exceeding 512 bytes (EDNS0).",
            "DNS caching drastically improves web browsing latency across the globe."
        ]
    )
    return prs

def build_m1_8(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.8", "Peer-to-Peer Paradigm & BitTorrent Case Study",
        "P2P File Distribution Time ($D_{P2P}$ vs $D_{CS}$), Torrents, Trackers & DHT, Chunks & Pieces, Rarest-First, Tit-for-Tat Choking",
        "Module 1"
    )
    
    create_content_slide(prs, "1.8.1 P2P File Distribution vs Client-Server Scalability", "M1.8 P2P SCALABILITY", [
        ("File Distribution Problem", "A server holds a file of size $F$ bits and needs to distribute copies to $N$ independent peer clients. Server upload rate is $u_s$, peer upload rates $u_i$, peer download rates $d_i$."),
        ("Client-Server Distribution Time ($D_{CS}$)", "$D_{CS} \\ge \\max \\{ \\frac{N \\cdot F}{u_s}, \\frac{F}{d_{min}} \\}$. As $N$ grows, $D_{CS}$ increases linearly with $N$. Adding more clients degrades service."),
        ("P2P Distribution Time ($D_{P2P}$)", "$D_{P2P} \\ge \\max \\{ \\frac{F}{u_s}, \\frac{F}{d_{min}}, \\frac{N \\cdot F}{u_s + \\sum_{i=1}^N u_i} \\}$. Each client donates upload capacity ($u_i$) back to the swarm."),
        ("Self-Scalability of P2P", "As $N \\to \\infty$, the total upload capacity $(u_s + \\sum u_i)$ scales proportionally with demand $N \\cdot F$, bounding distribution time to a sub-linear / constant asymptote.")
    ], "Scalability Formulas", [
        "D_CS >= max(N*F/u_s, F/d_min)",
        "D_P2P >= max(F/u_s, F/d_min, N*F / (u_s + sum(u_i)))",
        "Client-Server scales O(N)",
        "P2P scales O(1) / O(log N)",
        "Peers act as uploaders"
    ])
    
    create_content_slide(prs, "1.8.2 BitTorrent Protocol Architecture & Mechanics", "M1.8 BITTORRENT PROTOCOL", [
        ("Torrents & Swarms", "The collection of all peers participating in the distribution of a specific file is called a Swarm. File metadata is encoded in a `.torrent` file containing SHA-1 hashes of chunks."),
        ("Chunks & Pieces", "The file is partitioned into equal chunks (typically 256 KB to 2 MB). As soon as a peer downloads a chunk, it can immediately upload it to other peers."),
        ("Tracker & Trackerless DHT", "A central Tracker node maintains the list of active IP addresses in the swarm. Modern BitTorrent uses Kademlia Distributed Hash Tables (DHT) for trackerless operation."),
        ("Rarest-First Chunk Selection", "A peer determines which chunks are least common among its neighbors and requests those first. Ensures rare chunks are duplicated rapidly across the swarm to prevent missing chunk bottlenecks."),
        ("Tit-for-Tat (TFT) Choking Algorithm", "A peer gives upload priority to the top 4 peers currently supplying data to it at the highest rates (unchoked every 10 s)."),
        ("Optimistic Unchoking", "Every 30 s, a peer randomly picks 1 additional peer to upload to, discovering new faster partners and allowing newcomers to obtain their initial chunk.")
    ], "BitTorrent Mechanics", [
        "Swarm: Group of active peers",
        "Chunk Size: 256 KB - 2 MB",
        "Rarest-First: Balances supply",
        "Tit-for-Tat: Incentivizes uploading",
        "Optimistic Unchoking: Finds peers",
        "Seeders: 100% complete file"
    ])
    
    create_exam_booster_slide(
        prs, "M1.8", "P2P & BitTorrent", "K3 Apply",
        [
            "Derive the theoretical file distribution time for Client-Server ($D_{CS}$) and P2P ($D_{P2P}$) architectures. (8 Marks)",
            "Explain the working of BitTorrent with focus on Rarest-First chunk selection, Tit-for-Tat choking, and Optimistic Unchoking. (8 Marks)",
            "What is peer churn in P2P networks, and how does Distributed Hash Table (DHT) handle it? (5 Marks)"
        ],
        [
            "Client-Server distribution time increases linearly with $N$, whereas P2P distributes the upload burden.",
            "Rarest-First ensures even chunk distribution across the swarm.",
            "Tit-for-Tat solves free-riding by rewarding peers who contribute upload bandwidth."
        ]
    )
    return prs

def build_m1_9(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M1.9", "Application Layer Case Study: CDNs & Video Streaming",
        "Content Distribution Networks (CDNs), DNS Redirection, Edge Server Placement, DASH (Dynamic Adaptive Streaming over HTTP)",
        "Module 1"
    )
    
    create_content_slide(prs, "1.9.1 Content Distribution Networks (CDNs)", "M1.9 CDN ARCHITECTURE", [
        ("The Web Scale Problem", "Serving massive video traffic (YouTube, Netflix) from a single mega data center causes single point of failure, network congestion, long-distance delay, and repeated link traversals."),
        ("CDN Philosophy", "Deploy thousands of geographically distributed server clusters (Points of Presence - PoPs) at edge ISPs across the globe. Store replicated video copies close to end users."),
        ("Server Placement Philosophies", "1. Enter Deep (Akamai): Deploy clusters inside thousands of access ISPs close to users. 2. Bring Home (Limelight): Deploy fewer large clusters at Tier-1 PoPs interconnected by private backbone."),
        ("CDN DNS Redirection", "When user requests `video.netflix.com`, authoritative DNS intercepts the request and returns a CNAME pointing to CDN domain. CDN's DNS resolver uses client IP to return the IP address of the geographically closest edge cache server.")
    ], "CDN Benefits", [
        "Ultra-low latency to users",
        "Reduces ISP transit costs",
        "Absorbs DDoS attacks",
        "High availability & redundancy"
    ])
    
    create_content_slide(prs, "1.9.2 DASH: Dynamic Adaptive Streaming over HTTP", "M1.9 DASH VIDEO", [
        ("Video Encoding & Chunks", "Video is pre-encoded at multiple quality/bitrate versions (e.g., 360p 500 kbps, 720p 2 Mbps, 1080p 5 Mbps, 4K 15 Mbps) and partitioned into small chunks (2 to 10 seconds each)."),
        ("MPD (Media Presentation Description)", "An XML manifest file listing the URLs and bitrates for all chunks across every quality level."),
        ("Client-Side Dynamic Adaptation", "The client player continuously monitors available download bandwidth and buffer occupancy. It dynamically requests high-quality chunks when bandwidth is ample, and gracefully steps down to lower bitrates to avoid playback stalling."),
        ("Transport over HTTP/TCP", "Streams over standard HTTP/HTTPS port 80/443, effortlessly traversing firewalls and NATs without requiring proprietary streaming server protocols.")
    ], "DASH Algorithm", [
        "MPD Manifest: Lists chunks & bitrates",
        "Client measures throughput",
        "If buffer high -> Request 4K/1080p",
        "If bandwidth drops -> Request 720p",
        "Zero playback interruption"
    ])
    
    create_exam_booster_slide(
        prs, "M1.9", "CDN & Streaming Case Study", "K2 Understand",
        [
            "Explain how Content Distribution Networks (CDNs) use DNS redirection to route user requests to the optimal edge server. (8 Marks)",
            "Describe the architecture and working of Dynamic Adaptive Streaming over HTTP (DASH). (7 Marks)"
        ],
        [
            "CDNs bring content close to users, cutting down WAN transit delays and backbone congestion.",
            "DNS CNAME redirection enables real-time dynamic traffic routing based on network conditions.",
            "DASH shifts streaming intelligence to the client, adapting video bitrate in real time."
        ]
    )
    return prs

def build_module_1_master(prs=None):
    """Builds the comprehensive master deck combining all Module 1 topics."""
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "MODULE 1 MASTER DECK", "Application Layer & Internet Fundamentals",
        "Complete Lecture Slides for KTU PCCST501 Computer Networks | Topics M1.1 through M1.9",
        "Module 1 Master"
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
