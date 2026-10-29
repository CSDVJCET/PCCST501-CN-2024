"""
build_all_topic_pdfs_master.py
Generates comprehensive, beautifully formatted PDF Chapter Notes for all 36 topics in PCCST501 Computer Networks.
Prepared exclusively for:
Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
Viswajyothi College of Engineering and Technology (VJCET), Vazhakulam
KTU 2024 Scheme Curriculum
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
from reportlab.pdfgen import canvas

# --- PDF Canvas with Header, Footer, Watermark & Page Numbers ---
class NumberedTopicCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedTopicCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedTopicCanvas, self).showPage()
        super(NumberedTopicCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 755, "PCCST501 COMPUTER NETWORKS — TOPIC LECTURE NOTES")
            self.drawRightString(558, 755, "Prof. Anju Markose | Dept. of CSE, VJCET")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 748, 558, 748)
            
        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawString(54, 35, "Viswajyothi College of Engineering & Technology (VJCET) • KTU 2024 Scheme")
        self.drawRightString(558, 35, page_str)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        
        self.restoreState()

def get_topic_styles():
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#0f1e4a"),
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#475569"),
        spaceAfter=8
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=14.5,
        textColor=colors.HexColor("#0f1e4a"),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=colors.HexColor("#0e7490"),
        spaceBefore=5,
        spaceAfter=2,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=3
    )
    
    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1e293b"),
        leftIndent=10,
        firstLineIndent=-6,
        spaceAfter=2.5
    )
    
    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'h1': h1_style,
        'h2': h2_style,
        'body': body_style,
        'bullet': bullet_style
    }

def create_banner_header(topic_code, title, module_name, scope_text, styles):
    header_data = [
        [Paragraph(f"<b>PCCST501 COMPUTER NETWORKS</b> &bull; {module_name.upper()} &bull; <b>{topic_code}</b>", styles['subtitle'])],
        [Paragraph(f"<b>{title}</b>", styles['title'])],
        [Paragraph(f"<i>Coverage: {scope_text}</i>", styles['subtitle'])],
        [Paragraph("<b>Prepared by: Prof. Anju Markose</b> | Assistant Professor, Dept. of Computer Science & Engineering | VJCET", styles['subtitle'])]
    ]
    t = Table(header_data, colWidths=[504])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor("#0f1e4a")),
        ('LINEBELOW', (0,0), (-1,0), 0.5, colors.HexColor("#d97706")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    return t

def create_callout_box(title, items, border_color="#0e7490", bg_color="#f0fdf4", styles=None):
    content = [Paragraph(f"<b>{title}</b>", styles['h2'])]
    for it in items:
        if isinstance(it, tuple):
            content.append(Paragraph(f"<b>{it[0]}:</b> {it[1]}", styles['bullet']))
        else:
            content.append(Paragraph(f"&bull; {it}", styles['bullet']))
            
    t = Table([[content]], colWidths=[504])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_color)),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor(border_color)),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    return t

# Full 36 Topics Catalog with all legacy mapping aliases
FULL_TOPICS_CATALOG = [
    # --- MODULE 1 ---
    {
        "code": "M1.1",
        "name": "M1.1_Internet_Overview_Notes.pdf",
        "legacy_aliases": ["M1.1 Overview of Internet.pdf"],
        "title": "Overview of the Internet Architecture & Performance Metrics",
        "module": "Module 1",
        "scope": "Network Edge, Network Core, Packet Switching vs Circuit Switching, Delay Models, Loss & Bottleneck Throughput",
        "sections": [
            ("1. Internet Structural Architecture", [
                "Network Edge: End systems/hosts (clients, servers, IoT) running application-layer software. Access networks (DSL, FTTH, 5G, Wi-Fi) connect edge hosts to the core mesh.",
                "Network Core: Interconnected mesh of packet switches (routers and switches) forwarding packets using routing protocols across Tier-1 ISPs, IXPs, and Regional ISPs.",
                "Standards: Governed by IETF RFCs and IEEE 802 LAN/MAN standards."
            ]),
            ("2. Packet Switching vs Circuit Switching", [
                "Packet Switching: Data divided into discrete packets. Uses statistical multiplexing on demand. High efficiency for bursty data, but incurs queuing delays.",
                "Circuit Switching: Dedicated end-to-end physical channel pre-allocated via FDM or TDM. Zero queuing delay, but bandwidth is wasted during idle periods."
            ]),
            ("3. Mathematical Delay Components", [
                "Total Nodal Delay: d_nodal = d_proc + d_queue + d_trans + d_prop",
                "Processing Delay (d_proc): Microseconds to inspect header and verify checksums.",
                "Queuing Delay (d_queue): Waits in output queue. Traffic intensity I = (L * a) / R. As I -> 1, queue delay -> infinity.",
                "Transmission Delay (d_trans): d_trans = L / R seconds (L = packet bits, R = link rate bps).",
                "Propagation Delay (d_prop): d_prop = d / s seconds (d = distance, s = propagation speed ~2*10^8 m/s)."
            ])
        ],
        "worked_example": (
            "Worked Problem: Nodal Delay Calculation",
            [
                "Given: L = 1500 bytes = 12,000 bits. R = 10 Mbps = 10^7 bps. d = 100 km. s = 2 * 10^8 m/s. d_proc = 5 microseconds. 2 packets in queue.",
                "1. d_trans = 12,000 / 10^7 = 1.2 ms | 2. d_prop = 10^5 / (2 * 10^8) = 0.5 ms | 3. d_queue = 2 * 1.2 = 2.4 ms.",
                "4. Total d_nodal = 0.005 + 2.4 + 1.2 + 0.5 = 4.105 ms."
            ]
        ),
        "exam_questions": [
            "Differentiate between packet switching and circuit switching with respect to resource allocation and delay. (7 Marks)",
            "Derive the four components of nodal delay with mathematical formulas. (7 Marks)"
        ]
    },
    {
        "code": "M1.2",
        "name": "M1.2_Protocol_Layering_Notes.pdf",
        "legacy_aliases": ["M1.2 Protocol layering1.pdf", "M1.2 Protocol Layering2.pdf"],
        "title": "Protocol Layering & Network Models (OSI vs TCP/IP)",
        "module": "Module 1",
        "scope": "Layering Principles, OSI 7-Layer Model, TCP/IP 5-Layer Stack, PDU Encapsulation & Addressing Hierarchy",
        "sections": [
            ("1. Protocol Layering Principles", [
                "Modularity & Abstraction: Divides complex networking tasks into decoupled functional layers.",
                "Encapsulation: Top-down header addition at sender; Decapsulation: Bottom-up header stripping at receiver.",
                "PDU Hierarchy: L5 Message -> L4 Segment/Datagram -> L3 Packet/Datagram -> L2 Frame -> L1 Bit stream."
            ]),
            ("2. OSI 7-Layer vs TCP/IP Stack", [
                "OSI Reference Model: 7. Application, 6. Presentation, 5. Session, 4. Transport, 3. Network, 2. Data Link, 1. Physical.",
                "TCP/IP Stack: Application (integrates L7, L6, L5), Transport (TCP/UDP), Network (IPv4/IPv6), Data Link (Ethernet/802.11), Physical."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Compare the OSI 7-layer reference model with the TCP/IP 5-layer internet stack. (8 Marks)",
            "Explain PDU encapsulation and addressing across all 5 layers with a neat diagram. (7 Marks)"
        ]
    },
    {
        "code": "M1.3",
        "name": "M1.3_Application_Layer_Paradigms_Notes.pdf",
        "legacy_aliases": ["M1.3 Application Layer Introduction.pdf"],
        "title": "Application Layer Paradigms & Requirements",
        "module": "Module 1",
        "scope": "Client-Server vs P2P Architectures, Transport Service Needs (Integrity, Throughput, Timing, Security), Socket Interface",
        "sections": [
            ("1. Application Paradigms", [
                "Client-Server: Centralized server with fixed IP; clients initiate requests. Server upload bottlenecks at scale.",
                "Peer-to-Peer (P2P): Decentralized end hosts communicate directly; peers act as both clients and servers (self-scaling)."
            ]),
            ("2. Transport Requirements", [
                "Data Integrity: Loss-intolerant (TCP: Web, FTP, Email) vs Loss-tolerant (UDP: VoIP, Streaming).",
                "Timing & Throughput: Real-time interactive applications require tight delay bounds (<150ms)."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Compare Client-Server and Peer-to-Peer network paradigms with real-world examples. (6 Marks)"
        ]
    },
    {
        "code": "M1.4",
        "name": "M1.4_WWW_and_HTTP_Notes.pdf",
        "legacy_aliases": ["M1.4 WWW and HTTP.pdf"],
        "title": "World Wide Web & HTTP Protocol Suite",
        "module": "Module 1",
        "scope": "HTTP/1.0 vs HTTP/1.1 (Persistent vs Non-Persistent, Pipelining), HTTP/2 (Binary Framing), HTTP/3 (QUIC), Cookies & Web Caching",
        "sections": [
            ("1. HTTP Message Architecture & Methods", [
                "Stateless request-response protocol operating over TCP port 80 (HTTPS port 443).",
                "Methods: GET, POST, HEAD, PUT, DELETE. Status codes: 200 OK, 301 Moved, 304 Not Modified, 404 Not Found, 500 Error.",
                "State Management: Cookies (Set-Cookie / Cookie headers) and Session Tokens."
            ]),
            ("2. HTTP Protocol Evolution", [
                "HTTP/1.0: Non-persistent (1 TCP handshake per object = 2 RTT per object).",
                "HTTP/1.1: Persistent connections by default; Pipelining (suffers Head-of-Line blocking).",
                "HTTP/2: Binary Framing Layer, Stream Multiplexing over single TCP connection, HPACK compression, Server Push.",
                "HTTP/3: Operates over UDP using QUIC transport layer to eliminate TCP Head-of-Line blocking and enable 0-RTT handshakes."
            ])
        ],
        "worked_example": (
            "Worked Problem: Web Page Retrieval Time",
            [
                "Given: 1 Base HTML + 8 JPEG images on same server. RTT = 40 ms.",
                "1. Non-Persistent HTTP: 9 objects * 2 RTT = 18 RTT = 720 ms.",
                "2. Persistent HTTP without pipelining: 1 RTT (TCP) + 1 RTT (Base) + 8 * 1 RTT = 10 RTT = 400 ms.",
                "3. Persistent HTTP with pipelining: 1 RTT (TCP) + 1 RTT (Base) + 1 RTT (Images) = 3 RTT = 120 ms."
            ]
        ),
        "exam_questions": [
            "Compare Non-Persistent and Persistent HTTP connections with timing diagrams. (7 Marks)",
            "Explain how HTTP/2 and HTTP/3 solve Head-of-Line blocking. (8 Marks)"
        ]
    },
    {
        "code": "M1.5",
        "name": "M1.5_FTP_Protocol_Notes.pdf",
        "legacy_aliases": ["M1.5 AL FTP.pdf"],
        "title": "FTP (File Transfer Protocol) Architecture",
        "module": "Module 1",
        "scope": "Out-of-Band Control Port 21 vs In-Band Data Port 20, Active Mode (PORT) vs Passive Mode (PASV), Stateful Operation",
        "sections": [
            ("1. Dual-Channel Architecture", [
                "Control Connection: Dedicated TCP port 21 for commands (USER, PASS, RETR, STOR) and status replies. Remains open.",
                "Data Connection: Dedicated TCP port 20 opened per file transfer and closed upon completion.",
                "Stateful: Server tracks current working directory, authenticated user, and transfer mode."
            ]),
            ("2. Active vs Passive Mode", [
                "Active Mode: Client sends PORT command; Server initiates data connection from Port 20 to Client (blocked by client firewalls).",
                "Passive Mode: Client sends PASV command; Server opens random high port; Client initiates data connection (firewall-friendly)."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain why FTP is called an out-of-band protocol. Compare Active and Passive FTP. (8 Marks)"
        ]
    },
    {
        "code": "M1.6",
        "name": "M1.6_Email_SMTP_MIME_Notes.pdf",
        "legacy_aliases": ["M1.6 AL Email.pdf"],
        "title": "Electronic Mail Architecture & Protocols",
        "module": "Module 1",
        "scope": "User Agents (UA), Mail Transfer Agents (MTA), SMTP Push Protocol (Port 25/587), MIME Base64 Encoding, POP3 vs IMAP4 vs Webmail",
        "sections": [
            ("1. Email Delivery Flow & SMTP", [
                "SMTP (RFC 5321): Push protocol over TCP port 25 (server-to-server) and port 587 (client submission).",
                "Delivery: Sender UA -> Sender MTA (SMTP) -> Receiver MTA (SMTP) -> Receiver UA (POP3/IMAP4/Webmail)."
            ]),
            ("2. MIME & Access Protocols", [
                "MIME: Enables binary attachments over 7-bit ASCII SMTP using Base64 encoding.",
                "POP3 (Port 110): Download-and-delete mode. IMAP4 (Port 143): Synchronized server folders and partial message fetches."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Differentiate between SMTP and POP3/IMAP4. Explain why POP3/IMAP4 are required for email access. (7 Marks)"
        ]
    },
    {
        "code": "M1.7",
        "name": "M1.7_DNS_System_Notes.pdf",
        "legacy_aliases": ["M1.7 AL DNS.pdf"],
        "title": "Domain Name System (DNS) Architecture",
        "module": "Module 1",
        "scope": "Hierarchical Distributed Database, Root/TLD/Authoritative Servers, Iterative vs Recursive Queries, Resource Records (RR)",
        "sections": [
            ("1. DNS Hierarchy & Resolution", [
                "Distributed Database translating human hostnames to IP addresses over UDP port 53.",
                "Hierarchy: Root Servers -> TLD Servers (.com, .in) -> Authoritative Servers (vjcet.ac.in) -> Local Resolvers.",
                "Iterative: Contacted server returns referral. Recursive: Contacted server resolves full IP on client behalf."
            ]),
            ("2. Resource Records (RR)", [
                "Type A (IPv4), Type AAAA (IPv6), Type CNAME (Alias), Type NS (Name server), Type MX (Mail server), Type PTR (Reverse lookup)."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Draw and explain the step-by-step resolution process for a domain using Iterative vs Recursive queries. (8 Marks)"
        ]
    },
    {
        "code": "M1.8",
        "name": "M1.8_P2P_BitTorrent_Notes.pdf",
        "legacy_aliases": ["M1.8 AL P2P.pdf"],
        "title": "Peer-to-Peer Architecture & BitTorrent Case Study",
        "module": "Module 1",
        "scope": "P2P Scalability Time Models, BitTorrent Swarms, Trackers & DHT, Chunks, Rarest-First, Tit-for-Tat Choking",
        "sections": [
            ("1. Scalability Models", [
                "Client-Server Time: D_CS >= max(N*F / u_s, F / d_min). Linear growth with N.",
                "P2P Time: D_P2P >= max(F / u_s, F / d_min, N*F / (u_s + sum(u_i))). Sub-linear / bounded growth."
            ]),
            ("2. BitTorrent Mechanics", [
                "Swarm: Group of active peers. Chunks: 256KB - 2MB pieces. Rarest-First chunk selection.",
                "Tit-for-Tat (TFT): Top 4 contributing uploaders unchoked every 10s; Optimistic unchoking every 30s."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Derive the theoretical file distribution time for Client-Server and P2P architectures. (8 Marks)"
        ]
    },
    {
        "code": "M1.9",
        "name": "M1.9_Application_Layer_Case_Study_Notes.pdf",
        "legacy_aliases": ["M1.9 Case Study.pdf"],
        "title": "Application Layer Case Study: CDNs & Video Streaming",
        "module": "Module 1",
        "scope": "Content Distribution Networks (CDNs), DNS Redirection, Edge Server Placement, DASH (Dynamic Adaptive Streaming over HTTP)",
        "sections": [
            ("1. CDN Architecture", [
                "Replicates video content across thousands of edge server clusters (PoPs) close to end users.",
                "DNS Redirection: CNAME DNS intercept directs client to geographically nearest edge cache."
            ]),
            ("2. DASH Video Streaming", [
                "Video encoded at multiple bitrates and divided into chunks. Client dynamically requests optimal bitrate based on available bandwidth."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain how CDNs use DNS redirection and explain the working of DASH. (8 Marks)"
        ]
    },

    # --- MODULE 2 ---
    {
        "code": "M2.1.1",
        "name": "M2.1.1_Transport_Layer_Services_Notes.pdf",
        "legacy_aliases": ["M2.1.1Transport LayerServices.pdf"],
        "title": "Transport Layer Services & Multiplexing Principles",
        "module": "Module 2",
        "scope": "Process-to-Process Communication, Port Addressing, Connectionless vs Connection-Oriented Demultiplexing (2-Tuple vs 4-Tuple)",
        "sections": [
            ("1. Transport Responsibilities", [
                "Process-to-process delivery using 16-bit Port numbers (0 to 65535).",
                "Multiplexing & Demultiplexing: UDP uses 2-tuple (Dst IP, Dst Port); TCP uses 4-tuple (Src IP, Src Port, Dst IP, Dst Port)."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain how multiplexing and demultiplexing work in UDP and TCP. (8 Marks)"
        ]
    },
    {
        "code": "M2.1.2",
        "name": "M2.1.2_Transport_Protocols_UDP_Notes.pdf",
        "legacy_aliases": ["M2.1.2 TL Protocols.pdf", "M2.1.3 UDP.pdf"],
        "title": "Transport Protocols & User Datagram Protocol (UDP)",
        "module": "Module 2",
        "scope": "UDP 8-Byte Header Structure, 16-Bit 1's Complement Checksum Calculation with Pseudo-Header, UDP Applications",
        "sections": [
            ("1. UDP 8-Byte Header", [
                "Source Port (16b), Destination Port (16b), Length (16b), Checksum (16b). Minimal overhead."
            ]),
            ("2. Checksum Calculation", [
                "16-bit 1's complement sum of header, data, and 12-byte IP Pseudo-Header. Result inverted at sender."
            ])
        ],
        "worked_example": (
            "Worked Problem: UDP Checksum",
            [
                "Given words: 0x66B4, 0x5555, 0x8F0C. Sum = 0x14B15 -> Wrap carry = 0x4B16 -> Invert = 0xB4E9 (Checksum)."
            ]
        ),
        "exam_questions": [
            "Explain UDP 16-bit 1's complement checksum calculation with a worked example. (8 Marks)"
        ]
    },
    {
        "code": "M2.1.3",
        "name": "M2.1.3_TCP_Architecture_Handshake_Notes.pdf",
        "legacy_aliases": ["M2.1.3_TCP_Architecture_Handshake.pptx"],
        "title": "Transmission Control Protocol (TCP) Architecture",
        "module": "Module 2",
        "scope": "TCP 20-Byte Header Format, 3-Way Handshake Connection Setup, 4-Way Connection Teardown (TIME_WAIT 2MSL), Sequence/ACK Mechanics",
        "sections": [
            ("1. TCP Header & Flags", [
                "20-60 Byte Header: Seq Num (32b), Ack Num (32b), Flags (SYN, ACK, FIN, RST, PSH, URG), Window Size (16b), Checksum (16b).",
                "Cumulative ACK: Confirms receipt of all bytes up to Ack - 1."
            ]),
            ("2. Connection Lifecycle", [
                "3-Way Handshake: SYN (Seq=x) -> SYN-ACK (Seq=y, Ack=x+1) -> ACK (Seq=x+1, Ack=y+1).",
                "4-Way Teardown: FIN -> ACK -> FIN -> ACK. TIME_WAIT (2MSL) ensures final ACK delivery."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Draw the TCP header and explain the 3-Way Handshake with Sequence and Ack numbers. (8 Marks)"
        ]
    },
    {
        "code": "M2.1.4",
        "name": "M2.1.4_TCP_Congestion_Flow_Control_Notes.pdf",
        "legacy_aliases": ["M2.1.4 TCP.pdf"],
        "title": "TCP Flow & Congestion Control Architecture",
        "module": "Module 2",
        "scope": "Sliding Window Flow Control, Silly Window Syndrome, Slow Start, AIMD, Fast Retransmit, TCP Tahoe vs Reno",
        "sections": [
            ("1. Flow Control", [
                "Receiver advertises rwnd buffer. Effective Window = min(cwnd, rwnd).",
                "Silly Window Syndrome solved via Nagle's Algorithm (sender) and Clark's Solution (receiver)."
            ]),
            ("2. Congestion Control", [
                "Slow Start (doubles cwnd per RTT) -> Congestion Avoidance AIMD (+1 MSS per RTT).",
                "Fast Retransmit & Fast Recovery on 3 duplicate ACKs (TCP Reno)."
            ])
        ],
        "worked_example": (
            "Worked Problem: TCP Reno cwnd Evolution",
            [
                "Given ssthresh = 16 MSS. Starts at RTT 1 with cwnd = 1 MSS.",
                "RTT 1: 1 -> RTT 2: 2 -> RTT 3: 4 -> RTT 4: 8 -> RTT 5: 16 (ssthresh reached).",
                "RTT 6: 17 -> RTT 7: 18 -> RTT 8: 19 MSS.",
                "3 Dup ACKs at RTT 8 -> new ssthresh = 9 MSS. Under Reno Fast Recovery: RTT 9 cwnd = 9 MSS, RTT 10 cwnd = 10 MSS."
            ]
        ),
        "exam_questions": [
            "Compare TCP Tahoe and TCP Reno congestion control algorithms. (8 Marks)"
        ]
    },
    {
        "code": "M2.1.5",
        "name": "M2.1.5_Socket_Programming_IO_Multiplexing_Notes.pdf",
        "legacy_aliases": ["M2.1.5_Socket_Programming_IO_Multiplexing.pptx"],
        "title": "Berkeley Socket API & I/O Multiplexing",
        "module": "Module 2",
        "scope": "Socket System Calls Lifecycle (TCP & UDP), I/O Multiplexing with select() and poll(), fd_set Macros, Non-Blocking Sockets",
        "sections": [
            ("1. Berkeley Socket API", [
                "TCP Server: socket() -> bind() -> listen() -> accept() -> read()/write() -> close().",
                "TCP Client: socket() -> connect() -> write()/read() -> close(). UDP: sendto() / recvfrom()."
            ]),
            ("2. I/O Multiplexing with select()", [
                "Allows a single thread to monitor multiple descriptors simultaneously using fd_set bitmasks."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain the sequence of Berkeley socket system calls and explain select() I/O multiplexing. (8 Marks)"
        ]
    },
    {
        "code": "M2.2.1",
        "name": "M2.2.1_Network_Layer_Introduction_Notes.pdf",
        "legacy_aliases": ["M2.2.1NL INTRODUCTION.pdf"],
        "title": "Network Layer Architecture & Router Design",
        "module": "Module 2",
        "scope": "Data Plane (Forwarding) vs Control Plane (Routing), Datagram Networks vs Virtual Circuits, Router Fabrics & Buffering",
        "sections": [
            ("1. Data Plane vs Control Plane", [
                "Data Plane: Local nanosecond hardware packet forwarding (ASIC/TCAM).",
                "Control Plane: Network-wide software routing determining end-to-end paths (OSPF, BGP, SDN)."
            ]),
            ("2. Datagram vs Virtual Circuit", [
                "Datagram: Stateless routers, independent per-packet routing. Virtual Circuit: Connection setup, stateful switches."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Compare Datagram networks and Virtual Circuit networks. (8 Marks)"
        ]
    },
    {
        "code": "M2.2.2",
        "name": "M2.2.2_IPv4_Subnetting_CIDR_Notes.pdf",
        "legacy_aliases": ["M2.2.2 NL PROTOCOLS.pdf"],
        "title": "IPv4 Addressing, Subnetting, CIDR & Fragmentation",
        "module": "Module 2",
        "scope": "IPv4 20-60 Byte Header, Fragmentation & Reassembly, CIDR Slash Notation, Subnet Design, NAT & ICMP",
        "sections": [
            ("1. IPv4 Header & Fragmentation", [
                "20-60 Byte Header: IHL, Total Length, ID, Flags (DF/MF), Fragment Offset (8-byte units), TTL, Protocol, Checksum, IP addresses.",
                "Fragmentation occurs when datagram size > MTU."
            ]),
            ("2. CIDR & Subnetting", [
                "CIDR prefix /N. Usable hosts = 2^(32 - N) - 2."
            ])
        ],
        "worked_example": (
            "Worked Problem: IPv4 Fragmentation",
            [
                "Given: 4000 byte packet (20B header + 3980B payload) on MTU = 1500 bytes.",
                "Frag 1: Len=1500, Payload=1480, MF=1, Offset=0 | Frag 2: Len=1500, Payload=1480, MF=1, Offset=185 | Frag 3: Len=1040, Payload=1020, MF=0, Offset=370."
            ]
        ),
        "exam_questions": [
            "Draw IPv4 header and solve a fragmentation numerical problem. (8 Marks)"
        ]
    },
    {
        "code": "M2.2.3",
        "name": "M2.2.3_Unicast_Routing_Dijkstra_RIP_Notes.pdf",
        "legacy_aliases": ["M2.2.3UNICAST ROUTING.pdf"],
        "title": "Unicast Routing Protocols & Algorithms",
        "module": "Module 2",
        "scope": "Link-State Routing & Dijkstra's Algorithm, Distance-Vector & Bellman-Ford, Count-to-Infinity, RIP, OSPF & BGP-4",
        "sections": [
            ("1. LS vs DV Routing", [
                "Link-State: Floods LSAs; Dijkstra shortest path algorithm (OSPF).",
                "Distance-Vector: Distributed Bellman-Ford. Exchanging vectors with neighbors (RIP)."
            ]),
            ("2. Internet Protocols", [
                "RIP (DV, Hop count max 15, UDP 520) | OSPF (LS, Bandwidth metric, IP 89) | BGP-4 (Path Vector, TCP 179)."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain Dijkstra's shortest path algorithm with a worked table. (9 Marks)"
        ]
    },
    {
        "code": "M2.2.4",
        "name": "M2.2.4_Multicast_Routing_Protocols_Notes.pdf",
        "legacy_aliases": ["M2.2.4MULTICAST.pdf"],
        "title": "Multicast Routing Protocols & IGMP",
        "module": "Module 2",
        "scope": "Multicast Addressing (Class D), IGMP Host-Router Membership, Source-Based Trees vs Group-Shared Trees, RPF, PIM-DM vs PIM-SM",
        "sections": [
            ("1. Multicast Fundamentals & IGMP", [
                "Class D: 224.0.0.0/4. IGMP manages local host group memberships.",
                "Reverse Path Forwarding (RPF) prevents multicast loops."
            ]),
            ("2. PIM-DM vs PIM-SM", [
                "PIM-DM: Flood & Prune (Source-based tree). PIM-SM: Explicit Joins to Rendezvous Point (Shared tree)."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain PIM-DM and PIM-SM multicast routing. (8 Marks)"
        ]
    },
    {
        "code": "M2.2.5",
        "name": "M2.2.5_NextGen_IPv6_Notes.pdf",
        "legacy_aliases": ["M2.2.5NEXTGENIP.pdf"],
        "title": "Next Generation IP: IPv6 Architecture",
        "module": "Module 2",
        "scope": "IPv6 128-Bit Addressing, 40-Byte Fixed Header, Extension Headers, IPv4 vs IPv6 Comparison, Transition (Dual Stack, Tunneling)",
        "sections": [
            ("1. IPv6 Header & Improvements", [
                "128-bit addresses in colon-hex notation. Fixed 40-byte base header (no checksum, no in-network fragmentation).",
                "Extension headers daisy-chained via Next Header field."
            ]),
            ("2. Transition Strategies", [
                "Dual Stack, Tunneling (6to4, Teredo), NAT64/DNS64 header translation."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Compare IPv4 and IPv6 header structures and transition mechanisms. (8 Marks)"
        ]
    },
    {
        "code": "M2.2.6",
        "name": "M2.2.6_QoS_Traffic_Shaping_Notes.pdf",
        "legacy_aliases": ["M2.2.6QoS.pdf"],
        "title": "Quality of Service (QoS) & Traffic Shaping",
        "module": "Module 2",
        "scope": "QoS Metrics, Policing vs Shaping, Leaky Bucket vs Token Bucket, Scheduling (FIFO, WFQ), DiffServ vs IntServ",
        "sections": [
            ("1. Traffic Shaping", [
                "Leaky Bucket: Rigid constant output rate rho.",
                "Token Bucket: Allows regulated bursts up to bucket capacity b at wire rate R for duration T = b / (R - r)."
            ]),
            ("2. DiffServ vs IntServ", [
                "DiffServ: Scalable packet classification using 6-bit DSCP markings at boundary routers."
            ])
        ],
        "worked_example": (
            "Worked Problem: Token Bucket Burst Duration",
            [
                "Given: b = 16 MB, r = 2 MB/s, R = 10 MB/s. T = 16 / (10 - 2) = 2.0 seconds. Total Data = 20 MB."
            ]
        ),
        "exam_questions": [
            "Compare Leaky Bucket and Token Bucket traffic shaping algorithms. (8 Marks)"
        ]
    },
    {
        "code": "M2.3",
        "name": "M2.3_Linux_Kernel_TCP_IP_Routing_Notes.pdf",
        "legacy_aliases": ["M2.3 Linux Kernel.pdf"],
        "title": "Linux Kernel TCP/IP Stack & Routing Implementation",
        "module": "Module 2",
        "scope": "Linux Network Packet Flow, sk_buff Structure, net_device, Forwarding Information Base (FIB), Route Cache, iproute2",
        "sections": [
            ("1. Linux Kernel Networking", [
                "sk_buff: Socket buffer with head, data, tail, end pointers for zero-copy header manipulation.",
                "FIB: Forwarding Information Base implemented as a high-speed Level-Compressed Trie (LC-trie)."
            ]),
            ("2. Hands-on iproute2", [
                "ip route add, ip rule add for Policy-Based Routing (PBR)."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain the architecture and role of sk_buff in Linux kernel packet processing. (8 Marks)"
        ]
    },

    # --- MODULE 3 ---
    {
        "code": "M3.1",
        "name": "M3.1_DataLink_Layer_Framing_Notes.pdf",
        "legacy_aliases": ["M3.1 DL Introduction.pdf"],
        "title": "Data Link Layer Design & Framing Techniques",
        "module": "Module 3",
        "scope": "Node-to-Node Link Services, Character Count, Byte Stuffing (Flag/ESC), Bit Stuffing (HDLC), Physical Coding Violations",
        "sections": [
            ("1. Framing Methods", [
                "Byte Stuffing: Uses Flag 0x7E and ESC 0x7D for character transparency.",
                "Bit Stuffing (HDLC): Inserts a 0 bit after every 5 consecutive 1s."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain the four framing methods in the Data Link Layer. (8 Marks)"
        ]
    },
    {
        "code": "M3.2",
        "name": "M3.2_Error_Detection_Correction_Flow_Notes.pdf",
        "legacy_aliases": ["M3.2 Data Link Control.pdf"],
        "title": "Data Link Control: Error Detection, Correction & Flow Control",
        "module": "Module 3",
        "scope": "Hamming Distance, 2D Parity, CRC-32 Modulo-2 Division, Hamming (7,4) Code, Stop-and-Wait, Go-Back-N, Selective Repeat",
        "sections": [
            ("1. Error Control Theory", [
                "Hamming Distance: Detect s errors -> d_min >= s + 1; Correct t errors -> d_min >= 2t + 1.",
                "CRC: Modulo-2 binary polynomial division using generator polynomial G(x).",
                "Hamming (7,4) Code: Corrects single-bit errors using syndrome position calculation."
            ]),
            ("2. Flow Control Protocols", [
                "Stop-and-Wait: Ws=1, Wr=1 | Go-Back-N: Ws=2^m - 1, Wr=1 | Selective Repeat: Ws=2^(m-1), Wr=2^(m-1)."
            ])
        ],
        "worked_example": (
            "Worked Problem: CRC Modulo-2 Division",
            [
                "Given Data D = 10100100, Generator G = 10101. Remainder R = 1100. Transmitted = 101001001100."
            ]
        ),
        "exam_questions": [
            "Explain CRC error detection with a polynomial division example. (8 Marks)",
            "Derive maximum window sizes for Go-Back-N and Selective Repeat. (8 Marks)"
        ]
    },
    {
        "code": "M3.3",
        "name": "M3.3_Multiple_Access_Protocols_Notes.pdf",
        "legacy_aliases": ["M3.3 Multiple Access Protocols.pdf"],
        "title": "Multiple Access Control (MAC) Protocols",
        "module": "Module 3",
        "scope": "Random Access (Pure & Slotted ALOHA, CSMA, CSMA/CD, CSMA/CA), Controlled Access (Polling, Token Ring), CDMA",
        "sections": [
            ("1. ALOHA Protocols", [
                "Pure ALOHA: S = G * e^(-2G), Max 18.4%. Slotted ALOHA: S = G * e^(-G), Max 36.8%."
            ]),
            ("2. CSMA/CD", [
                "Carrier Sense + Collision Detection. Minimum frame size L_min = 2 * t_prop * R.",
                "Binary Exponential Backoff: Wait r * 512 bit times where r in [0, 2^k - 1]."
            ])
        ],
        "worked_example": (
            "Worked Problem: CSMA/CD Minimum Frame Size",
            [
                "Given R = 1 Gbps, d = 1 km, s = 2*10^8 m/s -> t_prop = 5 microseconds. L_min = 10^-5 * 10^9 = 1250 Bytes."
            ]
        ),
        "exam_questions": [
            "Derive throughput for Pure ALOHA and Slotted ALOHA and explain CSMA/CD. (8 Marks)"
        ]
    },
    {
        "code": "M3.4",
        "name": "M3.4_Link_Layer_Addressing_ARP_Notes.pdf",
        "legacy_aliases": ["M3.4 Link Layer Addressing.pdf"],
        "title": "Link-Layer Addressing & Address Resolution Protocol (ARP)",
        "module": "Module 3",
        "scope": "48-Bit MAC Addresses (EUI-48), ARP Request (Broadcast) & ARP Reply (Unicast), ARP Cache & Timeout, Subnet Crossing",
        "sections": [
            ("1. MAC Addressing & ARP", [
                "48-bit hardware MAC burned into NIC ROM. ARP resolves IP to MAC on local link.",
                "ARP Request is L2 Broadcast (FF:..:FF); ARP Reply is L2 Unicast."
            ]),
            ("2. Subnet Crossing", [
                "L3 IP addresses remain unchanged end-to-end; L2 MAC addresses rewritten at every router hop."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain ARP protocol operation and trace MAC/IP rewriting across subnets. (8 Marks)"
        ]
    },
    {
        "code": "M3.5",
        "name": "M3.5_Ethernet_Protocols_IEEE_802.3_Notes.pdf",
        "legacy_aliases": ["M3.5 Ethernet Protocols.pdf"],
        "title": "Ethernet Protocols & IEEE 802.3 Architecture",
        "module": "Module 3",
        "scope": "Standard Ethernet (10M), Fast Ethernet (100M), Gigabit Ethernet (1G), 10GbE, IEEE 802.3 Frame Format (64B to 1518B)",
        "sections": [
            ("1. IEEE 802.3 Frame Format", [
                "Preamble (7B), SFD (1B), Dst MAC (6B), Src MAC (6B), Type/Len (2B), Payload (46-1500B), FCS CRC-32 (4B).",
                "Minimum frame size = 64 bytes; Maximum frame size = 1518 bytes."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Draw IEEE 802.3 frame format and explain the minimum 64-byte frame requirement. (8 Marks)"
        ]
    },
    {
        "code": "M3.5V",
        "name": "M3.5V_VLAN_IEEE_802.1Q_Notes.pdf",
        "legacy_aliases": ["M3.5VLAN.pdf"],
        "title": "Virtual Local Area Networks (VLANs - IEEE 802.1Q)",
        "module": "Module 3",
        "scope": "Broadcast Containment, Port-Based vs Tagged VLANs, IEEE 802.1Q 4-Byte Tag (VID 1-4094), Access vs Trunk Ports, Router-on-a-Stick",
        "sections": [
            ("1. IEEE 802.1Q Tagged Framing", [
                "4-Byte Tag: TPID 0x8100 (16b), PCP (3b QoS), DEI (1b), VID (12b for 4094 VLANs).",
                "Trunk ports carry tagged frames; Access ports carry untagged frames."
            ]),
            ("2. Inter-VLAN Routing", [
                "Router-on-a-Stick (sub-interfaces) and Layer 3 Switch SVIs."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain VLANs, IEEE 802.1Q tagging, and Router-on-a-Stick inter-VLAN routing. (8 Marks)"
        ]
    },
    {
        "code": "M3.6",
        "name": "M3.6_Connecting_Devices_Notes.pdf",
        "legacy_aliases": ["M3.6 Connecting Devices.pdf"],
        "title": "Connecting Devices & Spanning Tree Protocol (STP)",
        "module": "Module 3",
        "scope": "Repeaters, Hubs (L1), Bridges & Layer 2 Switches (MAC Learning), Spanning Tree Protocol (IEEE 802.1D STP), Routers",
        "sections": [
            ("1. Connecting Devices Taxonomy", [
                "Hubs (L1): Single collision/broadcast domain. Switches (L2): Microsegmented collision domains. Routers (L3): Separate broadcast domains."
            ]),
            ("2. Spanning Tree Protocol (STP)", [
                "Breaks switching loops: 1. Root Bridge election (lowest Bridge ID), 2. Root Ports, 3. Designated Ports, 4. Blocking ports."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Compare Hubs, Switches, and Routers and explain STP algorithm. (8 Marks)"
        ]
    },
    {
        "code": "M3.7",
        "name": "M3.7_Wireless_LAN_IEEE_802.11_Notes.pdf",
        "legacy_aliases": ["M3.7WirelessLAN.pdf"],
        "title": "Wireless LANs: IEEE 802.11 (Wi-Fi) Architecture",
        "module": "Module 3",
        "scope": "BSS, AP, ESS, Hidden/Exposed Terminal Problems, CSMA/CA with RTS/CTS, SIFS/PIFS/DIFS Intervals, 4-Address Frame",
        "sections": [
            ("1. 802.11 Architecture & Problems", [
                "BSS with AP; ESS with DS. Hidden Terminal resolved via RTS/CTS handshake and NAV timer."
            ]),
            ("2. CSMA/CA Timing & Frame", [
                "SIFS (ACKs/CTS) < PIFS < DIFS. 4 MAC addresses in 802.11 frame format."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain Hidden and Exposed terminal problems and CSMA/CA with RTS/CTS. (8 Marks)"
        ]
    },
    {
        "code": "M3.8",
        "name": "M3.8_Mobile_IP_Architecture_Notes.pdf",
        "legacy_aliases": ["M3.8Mobile IP.pdf"],
        "title": "Mobile IP Architecture & Protocols",
        "module": "Module 3",
        "scope": "Mobile Node (MN), Home Agent (HA), Foreign Agent (FA), Home Address (HoA), Care-of Address (CoA), Tunneling & Triangle Routing",
        "sections": [
            ("1. Mobile IP Entities & Tunneling", [
                "MN retains permanent Home Address (HoA) while acquiring temporary Care-of Address (CoA).",
                "Home Agent intercepts packets using Proxy ARP and tunnels them via IP-in-IP encapsulation to Foreign Agent."
            ]),
            ("2. Triangle Routing", [
                "Inefficient triangular path solved via Route Optimization (CN caches CoA)."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain Mobile IP entities, registration, and IP-in-IP tunneling. (8 Marks)"
        ]
    },
    {
        "code": "M3.9",
        "name": "M3.9_Linux_Raw_Sockets_PF_PACKET_Notes.pdf",
        "legacy_aliases": ["DL Hands-on.pdf", "DL Handson Lecture notes.pdf"],
        "title": "Linux Network Programming: Raw Sockets & PF_PACKET",
        "module": "Module 3",
        "scope": "Data Link Provider Interface (DLPI), BSD Packet Filter (BPF), Linux PF_PACKET / AF_PACKET (SOCK_RAW, ETH_P_ALL), Promiscuous Sniffer",
        "sections": [
            ("1. Linux PF_PACKET Raw Sockets", [
                "AF_PACKET domain bypasses kernel TCP/IP stack to capture/inject raw L2 Ethernet frames.",
                "Promiscuous Mode (IFF_PROMISC): Disables MAC filtering to capture all link traffic."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain the architecture of PF_PACKET raw sockets and write a packet sniffer in C. (8 Marks)"
        ]
    },

    # --- MODULE 4 ---
    {
        "code": "M4.1",
        "name": "M4.1_Network_Management_SNMP_Notes.pdf",
        "legacy_aliases": ["M4.1 SNMP&ASN.pdf"],
        "title": "Network Management Framework & SNMP Protocol",
        "module": "Module 4",
        "scope": "Managing Entities, Agents, MIB Database, SNMP Protocol Operations, SNMPv1 vs SNMPv2c vs SNMPv3 (USM & VACM)",
        "sections": [
            ("1. SNMP Framework & Operations", [
                "4 Pillars: Manager (NMS), Agents, MIB, SNMP protocol (UDP 161/162).",
                "Operations: GetRequest, GetNextRequest, GetBulkRequest, SetRequest, Response, Trap, InformRequest."
            ]),
            ("2. SNMPv3 Security", [
                "USM: HMAC-SHA authentication, AES encryption, replay protection."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain the SNMP architecture and operations. Compare SNMPv1, v2c, and v3. (8 Marks)"
        ]
    },
    {
        "code": "M4.2",
        "name": "M4.2_ASN.1_and_MIB_Notes.pdf",
        "legacy_aliases": [],
        "title": "Structure of Management Information (SMI) & ASN.1",
        "module": "Module 4",
        "scope": "ASN.1 Data Types, SMIv2 OBJECT-TYPE Macro, MIB OID Tree Hierarchy (1.3.6.1.2.1), Standard MIB-II Groups, BER Encoding",
        "sections": [
            ("1. MIB OID Tree Hierarchy", [
                "Standard Internet MIB-II prefix: 1.3.6.1.2.1.",
                "Groups: system (.1), interfaces (.2), ip (.4), tcp (.6), udp (.7), snmp (.11)."
            ]),
            ("2. Basic Encoding Rules (BER)", [
                "Encodes data in Tag-Length-Value (TLV) format."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Illustrate the MIB-II OID tree hierarchy and explain standard groups. (8 Marks)"
        ]
    },
    {
        "code": "M4.3",
        "name": "M4.3_Data_Signals_Channel_Capacity_Notes.pdf",
        "legacy_aliases": ["M4.2Data and Signal.pdf"],
        "title": "Data and Signals: Theoretical Channel Capacity",
        "module": "Module 4",
        "scope": "Analog vs Digital Signals, Bandwidth, Transmission Impairments (Attenuation, Noise), Nyquist Rate vs Shannon Capacity",
        "sections": [
            ("1. Signals & Impairments", [
                "Bandwidth B = f_max - f_min. Attenuation dB = 10 * log10(P2/P1). SNR_dB = 10 * log10(SNR)."
            ]),
            ("2. Channel Capacity", [
                "Nyquist (Noiseless): C = 2 * B * log2(L) bps. Shannon (Noisy): C = B * log2(1 + SNR) bps."
            ])
        ],
        "worked_example": (
            "Worked Problem: Shannon & Nyquist Capacity",
            [
                "Given B = 3000 Hz, SNR_dB = 31.62 dB -> SNR = 1452.1.",
                "Shannon C = 3000 * log2(1453.1) = 31.5 kbps. Nyquist levels: 31,515 = 6000 * log2(L) -> L = 38 levels."
            ]
        ),
        "exam_questions": [
            "State and derive Nyquist and Shannon capacity formulas with a numerical problem. (8 Marks)"
        ]
    },
    {
        "code": "M4.4",
        "name": "M4.4_Digital_Transmission_Line_Coding_Notes.pdf",
        "legacy_aliases": ["M4.3DigitalTransmission.pdf"],
        "title": "Digital Transmission & Line Coding Schemes",
        "module": "Module 4",
        "scope": "Line Coding Criteria (DC, Sync, Baseline Wander), Unipolar, Polar (NRZ, Manchester), Bipolar (AMI), PCM & DM",
        "sections": [
            ("1. Line Coding Schemes", [
                "Manchester (IEEE 802.3): Mid-bit transition (1 = High-to-Low; 0 = Low-to-High). Zero DC and perfect clock sync.",
                "Differential Manchester: Mid-bit transition + start-bit transition for 0.",
                "Bipolar AMI: Bit 0 = 0V; Bit 1 = Alternating +V and -V."
            ]),
            ("2. Pulse Code Modulation (PCM)", [
                "Sampling (fs >= 2*fmax) -> Quantization -> Encoding."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Draw line coding waveforms for bit stream 10110001 using NRZ-L, NRZ-I, Manchester, and AMI. (9 Marks)"
        ]
    },
    {
        "code": "M4.5",
        "name": "M4.5_Analog_Transmission_Multiplexing_Notes.pdf",
        "legacy_aliases": ["M4.4AnalogTransmission.pdf", "M4.5BandwidthUtilization.pdf"],
        "title": "Analog Transmission & Bandwidth Utilization (Multiplexing)",
        "module": "Module 4",
        "scope": "Digital Modulation (ASK, FSK, PSK, QAM), Multiplexing (FDM, WDM, Synchronous vs Statistical TDM), Spread Spectrum",
        "sections": [
            ("1. Modulation & QAM", [
                "ASK, FSK, PSK (BPSK, QPSK). QAM modulates both amplitude and phase (16-QAM = 4 bits/symbol)."
            ]),
            ("2. Multiplexing", [
                "FDM (Frequency), WDM (Optical wavelength), Synchronous TDM (Round-robin slots), Statistical TDM (On-demand dynamic slots)."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Explain QAM with constellation diagrams and compare Synchronous vs Statistical TDM. (8 Marks)"
        ]
    },
    {
        "code": "M4.6",
        "name": "M4.6_Transmission_Media_Notes.pdf",
        "legacy_aliases": ["M4.6TransmissionMedia.pdf"],
        "title": "Physical Transmission Media (Guided & Unguided)",
        "module": "Module 4",
        "scope": "Guided (Twisted Pair UTP/STP, Coaxial Cable, Fiber Optics MMF/SMF), Unguided Wireless (Radio, Microwaves, Infrared)",
        "sections": [
            ("1. Guided Media", [
                "Twisted-Pair (Cat 5e/6 UTP, RJ-45). Coaxial (10Base5/2, BNC). Optical Fiber (Total Internal Reflection, Single-Mode SMF zero modal dispersion)."
            ]),
            ("2. Unguided Wireless Media", [
                "Radio Waves (Omnidirectional, wall penetration), Microwaves (Line-of-sight parabolic dish), Infrared (Short range, contained by walls)."
            ])
        ],
        "worked_example": None,
        "exam_questions": [
            "Compare Single-Mode and Multimode optical fibers and compare guided vs unguided media. (8 Marks)"
        ]
    }
]

def generate_topic_pdf(topic_meta, target_filepath):
    doc = SimpleDocTemplate(
        target_filepath,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    styles = get_topic_styles()
    story = []
    
    story.append(create_banner_header(
        topic_meta['code'],
        topic_meta['title'],
        topic_meta['module'],
        topic_meta['scope'],
        styles
    ))
    story.append(Spacer(1, 8))
    
    for sec_title, sec_bullets in topic_meta['sections']:
        story.append(Paragraph(f"<b>{sec_title}</b>", styles['h1']))
        story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#cbd5e1"), spaceAfter=5))
        for b in sec_bullets:
            story.append(Paragraph(f"&bull; {b}", styles['bullet']))
        story.append(Spacer(1, 5))
        
    if topic_meta.get('worked_example'):
        ex_title, ex_steps = topic_meta['worked_example']
        story.append(Spacer(1, 3))
        story.append(create_callout_box(f"📝 {ex_title}", ex_steps, border_color="#10b981", bg_color="#f0fdf4", styles=styles))
        story.append(Spacer(1, 6))
        
    if topic_meta.get('exam_questions'):
        story.append(Spacer(1, 3))
        q_items = [f"Q: {q}" for q in topic_meta['exam_questions']]
        story.append(create_callout_box("🎯 KTU University High-Yield Exam Questions", q_items, border_color="#d97706", bg_color="#fffbeb", styles=styles))
        
    doc.build(story, canvasmaker=NumberedTopicCanvas)

def main():
    notes_dir = os.path.join(os.path.dirname(__file__), "assets", "notes_pdf")
    legacy_dir = os.path.join(os.path.dirname(__file__), "assets", "pdfs")
    os.makedirs(notes_dir, exist_ok=True)
    os.makedirs(legacy_dir, exist_ok=True)
    
    print("===================================================================")
    print("Generating Comprehensive Topic-Wise Chapter Notes PDFs (Full 36 Topics)...")
    print("Author: Prof. Anju Markose | Dept. of CSE, VJCET")
    print("===================================================================")
    
    for t in FULL_TOPICS_CATALOG:
        # Standardized file in assets/notes_pdf/
        p1 = os.path.join(notes_dir, t['name'])
        generate_topic_pdf(t, p1)
        print(f"  [+] Generated: assets/notes_pdf/{t['name']}")
        
        # Overwrite all legacy aliases in assets/pdfs/
        for alias in t.get('legacy_aliases', []):
            p2 = os.path.join(legacy_dir, alias)
            generate_topic_pdf(t, p2)
            print(f"      -> Overwrote legacy: assets/pdfs/{alias}")
            
    print("\nAll 36 topic PDFs successfully created and all legacy Arsha files replaced!")

if __name__ == "__main__":
    main()
