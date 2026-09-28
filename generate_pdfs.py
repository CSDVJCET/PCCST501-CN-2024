import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
from reportlab.pdfgen import canvas

# --- PDF Canvas with Header & Footer & Page Numbers ---
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 755, "PCCST501 COMPUTER NETWORKS — EXAM REVISION NOTES")
            self.drawRightString(558, 755, "VJCET CSE | Prof. Anju Markose")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 748, 558, 748)
            
        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawString(54, 35, "Viswajyothi College of Engineering and Technology (VJCET)")
        self.drawRightString(558, 35, page_str)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        
        self.restoreState()

def get_styles():
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1e3a8a"),
        alignment=1, # Center
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#475569"),
        alignment=1,
        spaceAfter=14
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1e3a8a"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#0e7490"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=5
    )
    
    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#1e293b"),
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    )
    
    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#0f172a"),
        backColor=colors.HexColor("#f1f5f9"),
        leftIndent=8,
        rightIndent=8,
        spaceBefore=4,
        spaceAfter=6
    )
    
    key_box_style = ParagraphStyle(
        'KeyBox_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#1e3a8a")
    )
    
    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'h1': h1_style,
        'h2': h2_style,
        'body': body_style,
        'bullet': bullet_style,
        'code': code_style,
        'key_box': key_box_style
    }

def add_header_banner(story, styles, title, subtitle):
    story.append(Paragraph(title, styles['title']))
    story.append(Paragraph(subtitle, styles['subtitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12))

def add_info_card(story, text, bg_hex="#f8fafc", border_hex="#0e7490"):
    p = Paragraph(f"<b>Key Concept / Exam Formula:</b><br/>{text}", ParagraphStyle(
        'InfoCard',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#0f172a")
    ))
    t = Table([[p]], colWidths=[500])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_hex)),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor(border_hex)),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))

# ==================== BUILD MODULE 1 CONTENT ====================
def get_module_1_story(styles):
    story = []
    add_header_banner(story, styles, "MODULE 1: Overview of Internet & Application Layer", 
                      "PCCST501 Computer Networks | Quick Exam Revision Guide | KTU S5 CSE | Prof. Anju Markose, VJCET")
    
    # 1.1 Overview of Internet
    story.append(Paragraph("1. Overview of the Internet & Protocol Layering", styles['h1']))
    story.append(Paragraph("<b>Internet Components:</b> The network is divided into the <i>Network Edge</i> (end systems, hosts, clients, servers) and the <i>Network Core</i> (mesh of interconnected routers and packet switches).", styles['body']))
    story.append(Paragraph("<b>Packet Switching vs Circuit Switching:</b>", styles['h2']))
    story.append(Paragraph("&bull; <b>Packet Switching:</b> Discrete data packets share network resources via <i>statistical multiplexing</i>. Highly efficient, handles bursty traffic, but introduces queuing delays and packet loss.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Circuit Switching:</b> Dedicated end-to-end communication channels reserved for the entire session (e.g. traditional PSTN phone network). Guaranteed bandwidth, but underutilized when idle.", styles['bullet']))
    
    add_info_card(story, "<b>Nodal Delay Formula:</b> Total Delay = d_proc + d_queue + d_trans + d_prop<br/>"
                         "&bull; <b>Transmission Delay (d_trans):</b> L / R (Packet length in bits / Link bandwidth in bps)<br/>"
                         "&bull; <b>Propagation Delay (d_prop):</b> d / s (Physical distance in meters / Speed of light ~2x10^8 m/s)")
    
    story.append(Paragraph("<b>OSI vs TCP/IP Protocol Layering:</b>", styles['h2']))
    
    table_data = [
        [Paragraph("<b>OSI Model (7 Layers)</b>", styles['key_box']), Paragraph("<b>TCP/IP Model (5 Layers)</b>", styles['key_box']), Paragraph("<b>Protocol Data Unit (PDU) & Examples</b>", styles['key_box'])],
        [Paragraph("7. Application<br/>6. Presentation<br/>5. Session", styles['body']), Paragraph("5. Application Layer", styles['body']), Paragraph("<b>Message:</b> HTTP, FTP, SMTP, DNS", styles['body'])],
        [Paragraph("4. Transport Layer", styles['body']), Paragraph("4. Transport Layer", styles['body']), Paragraph("<b>Segment / Datagram:</b> TCP, UDP", styles['body'])],
        [Paragraph("3. Network Layer", styles['body']), Paragraph("3. Network Layer", styles['body']), Paragraph("<b>Packet / Datagram:</b> IPv4, IPv6, ICMP", styles['body'])],
        [Paragraph("2. Data Link Layer", styles['body']), Paragraph("2. Data Link Layer", styles['body']), Paragraph("<b>Frame:</b> Ethernet (802.3), WiFi (802.11)", styles['body'])],
        [Paragraph("1. Physical Layer", styles['body']), Paragraph("1. Physical Layer", styles['body']), Paragraph("<b>Bits:</b> UTP Cable, Optical Fiber, Radio", styles['body'])]
    ]
    t = Table(table_data, colWidths=[160, 150, 190])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e2e8f0")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))
    
    # 1.2 Application Layer Protocols
    story.append(Paragraph("2. World Wide Web (WWW) and HTTP", styles['h1']))
    story.append(Paragraph("<b>HTTP Characteristics:</b> Stateless client-server protocol over TCP (Default Port 80, HTTPS Port 443).", styles['body']))
    story.append(Paragraph("&bull; <b>Non-Persistent HTTP (1.0):</b> Each object download requires a separate TCP connection (2 RTT per object + transmission time).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Persistent HTTP (1.1):</b> Reuses a single TCP connection for multiple web objects, drastically cutting connection establishment latency.", styles['bullet']))
    story.append(Paragraph("&bull; <b>HTTP Methods:</b> GET (retrieve data), POST (submit form/payload), HEAD (retrieve headers only), PUT (upload/replace), DELETE.", styles['bullet']))
    story.append(Paragraph("&bull; <b>HTTP Status Codes:</b> 200 (OK), 301 (Moved Permanently), 304 (Not Modified / Cached), 400 (Bad Request), 404 (Not Found), 500 (Internal Server Error).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Cookies & Web Caching:</b> Cookies provide state management over stateless HTTP via 4 components: Header in HTTP response, Header in next request, Cookie file on client host, Backend database.", styles['bullet']))
    
    story.append(Paragraph("3. File Transfer Protocol (FTP) & Electronic Mail", styles['h1']))
    story.append(Paragraph("<b>FTP Architecture:</b> Uses two separate parallel TCP connections (Out-of-band control):", styles['body']))
    story.append(Paragraph("&bull; <b>Control Connection (Port 21):</b> Carries user commands and server replies throughout the session. Remains open.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Data Connection (Port 20):</b> Opened dynamically for each file transfer and closed immediately after transfer finishes.", styles['bullet']))
    story.append(Paragraph("<b>Electronic Mail Architecture:</b>", styles['h2']))
    story.append(Paragraph("&bull; <b>SMTP (Simple Mail Transfer Protocol - Port 25/587):</b> Push protocol between client/server and server/server using direct TCP and 7-bit ASCII commands (HELO, MAIL FROM, RCPT TO, DATA, QUIT).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Mail Access Protocols (Pull):</b> POP3 (Post Office Protocol v3 - Port 110, downloads emails locally, stateless), IMAP4 (Internet Message Access Protocol v4 - Port 143, stateful, synchronizes folders across multiple devices).", styles['bullet']))
    story.append(Paragraph("&bull; <b>MIME (Multipurpose Internet Mail Extensions):</b> Extends SMTP to carry multimedia non-ASCII content using Base64 encoding.", styles['bullet']))
    
    story.append(Paragraph("4. Domain Name System (DNS) & P2P / BitTorrent", styles['h1']))
    story.append(Paragraph("<b>DNS Architecture:</b> Distributed hierarchical database running over UDP/TCP Port 53.", styles['body']))
    story.append(Paragraph("&bull; <b>Server Hierarchy:</b> 13 Root DNS server clusters &rarr; Top-Level Domain (TLD) servers (.com, .org, .in) &rarr; Authoritative DNS servers.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Resolution Types:</b> <i>Recursive</i> (local resolver queries on behalf of client until resolved) vs <i>Iterative</i> (resolver receives referral addresses).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Resource Records (RR):</b> Type A (Host &rarr; IPv4), Type AAAA (Host &rarr; IPv6), Type NS (Domain &rarr; Authoritative Name Server), Type CNAME (Canonical Alias), Type MX (Domain &rarr; Mail Server).", styles['bullet']))
    story.append(Paragraph("<b>Peer-to-Peer Paradigm & BitTorrent:</b>", styles['h2']))
    story.append(Paragraph("&bull; <b>P2P Self-Scalability:</b> As users join, they bring both demand and upload capacity. BitTorrent divides files into 256 KB chunks.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Rarest First Policy:</b> Peers request chunks that are least copied among neighbors first to maximize piece variety.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Tit-for-Tat Choking Algorithm:</b> Peers unchoke top 4 uploaders offering highest rates. Optimistic unchoking tests random new peers every 30 seconds.", styles['bullet']))
    
    return story

# ==================== BUILD MODULE 2 CONTENT ====================
def get_module_2_story(styles):
    story = []
    add_header_banner(story, styles, "MODULE 2: Transport & Network Layers with Linux Kernel", 
                      "PCCST501 Computer Networks | Quick Exam Revision Guide | KTU S5 CSE | Prof. Anju Markose, VJCET")
    
    story.append(Paragraph("1. Transport Layer: UDP & TCP Protocols", styles['h1']))
    story.append(Paragraph("<b>Transport Layer Role:</b> Logical process-to-process communication using 16-bit Port Numbers (0-65535).", styles['body']))
    story.append(Paragraph("&bull; <b>UDP (User Datagram Protocol):</b> Connectionless, unreliable, 8-byte fixed header (Src Port, Dst Port, Length, Checksum). Uses 1's complement addition over pseudo-header + UDP header + payload.", styles['bullet']))
    story.append(Paragraph("&bull; <b>TCP (Transmission Control Protocol):</b> Connection-oriented, reliable byte stream, full-duplex, flow-controlled, congestion-controlled.", styles['bullet']))
    story.append(Paragraph("&bull; <b>TCP Header (20-60 Bytes):</b> Sequence Number, Acknowledgment Number, Header Length (Data Offset), Flags (URG, ACK, PSH, RST, SYN, FIN), Advertised Window (rwnd), Checksum, Urgent Pointer.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Connection Setup & Tear-down:</b> 3-Way Handshake (SYN &rarr; SYN-ACK &rarr; ACK) and 4-Way Handshake (FIN &rarr; ACK, FIN &rarr; ACK).", styles['bullet']))
    
    add_info_card(story, "<b>TCP Congestion Control Phases:</b><br/>"
                         "1. <b>Slow Start:</b> cwnd starts at 1 MSS, doubles every RTT (exponential growth: 1, 2, 4, 8...) until reaching ssthresh.<br/>"
                         "2. <b>Congestion Avoidance (AIMD):</b> When cwnd >= ssthresh, cwnd increases linearly by 1 MSS per RTT.<br/>"
                         "3. <b>On Loss Detection:</b><br/>"
                         "   &bull; <i>Timeout (Severe):</i> ssthresh = cwnd/2, cwnd = 1 MSS &rarr; enters Slow Start.<br/>"
                         "   &bull; <i>3 Duplicate ACKs (Mild):</i> ssthresh = cwnd/2. In <b>TCP Reno</b>, cwnd = ssthresh + 3 MSS (Fast Recovery).")

    story.append(Paragraph("2. Socket Programming & I/O Multiplexing (Hands-on)", styles['h1']))
    story.append(Paragraph("<b>TCP Socket Lifecycle:</b>", styles['h2']))
    story.append(Paragraph("&bull; <b>Server:</b> <code>socket()</code> &rarr; <code>bind()</code> &rarr; <code>listen()</code> &rarr; <code>accept()</code> &rarr; <code>read()/write()</code> &rarr; <code>close()</code>", styles['bullet']))
    story.append(Paragraph("&bull; <b>Client:</b> <code>socket()</code> &rarr; <code>connect()</code> &rarr; <code>write()/read()</code> &rarr; <code>close()</code>", styles['bullet']))
    story.append(Paragraph("<b>I/O Multiplexing (select vs poll):</b>", styles['h2']))
    story.append(Paragraph("&bull; <code>select()</code>: Monitors bit-masks of file descriptors (<code>readfds, writefds</code>) up to <code>FD_SETSIZE</code> (1024). Reconstructs fd_set on each loop.", styles['bullet']))
    story.append(Paragraph("&bull; <code>poll()</code>: Uses an array of <code>struct pollfd</code> (fd, events, revents). Eliminates the 1024 fd limit and avoids fd_set reconstruction.", styles['bullet']))
    
    story.append(Paragraph("3. Network Layer: IPv4, Subnetting & Unicast Routing", styles['h1']))
    story.append(Paragraph("<b>IPv4 Datagram Header (20-60 Bytes):</b> Ver (4b), IHL (4b), Type of Service (8b), Total Length (16b), ID (16b), Flags [DF, MF] (3b), Fragment Offset (13b), TTL (8b), Protocol [TCP=6, UDP=17] (8b), Header Checksum (16b), Src IP (32b), Dst IP (32b).", styles['body']))
    
    add_info_card(story, "<b>Subnetting Calculations:</b><br/>"
                         "Given prefix /n &rarr; Subnet mask has n leading 1s. Host bits = 32 - n.<br/>"
                         "&bull; Number of usable hosts = 2^(32 - n) - 2<br/>"
                         "&bull; Network ID = IP bitwise AND Subnet Mask<br/>"
                         "&bull; Directed Broadcast Address = IP with all host bits set to 1")

    story.append(Paragraph("<b>Unicast Routing Protocols:</b>", styles['h2']))
    story.append(Paragraph("&bull; <b>Distance Vector (RIP):</b> Based on Bellman-Ford algorithm. Metric = Hop count (Max 15 hops, 16 = infinity). Suffers from <i>Count-to-Infinity</i> (mitigated by Split Horizon & Poison Reverse).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Link State (OSPF):</b> Based on Dijkstra's Shortest Path First (SPF) algorithm. Floods Link State Advertisements (LSAs) within hierarchical Areas (Area 0 = Backbone). Metric = Cost (Bandwidth based).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Path Vector (BGP):</b> Inter-Autonomous System (Inter-AS) protocol. Exchanges complete AS-Path vectors to eliminate loops and enforce routing policies.", styles['bullet']))

    story.append(Paragraph("4. Multicast Routing, Next-Gen IP (IPv6) & QoS", styles['h1']))
    story.append(Paragraph("&bull; <b>Multicast Protocols:</b> IGMP (group joins/leaves). DVMRP (Reverse Path Forwarding with flood & prune), PIM-DM (dense mode flood/prune), PIM-SM (sparse mode Rendezvous Point shared tree).", styles['bullet']))
    story.append(Paragraph("&bull; <b>IPv6 Enhancements:</b> 128-bit addresses (hex: <code>2001:db8::1</code>), fixed 40-byte base header (no checksum, faster processing), built-in security (IPsec), SLAAC stateless auto-configuration.", styles['bullet']))
    story.append(Paragraph("&bull; <b>QoS Traffic Shaping:</b> <i>Leaky Bucket</i> (enforces strict constant rate, discards excess bursts) vs <i>Token Bucket</i> (tokens accumulate periodically, allowing burst transmission up to token capacity).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Linux Routing Table Hands-on:</b> Kernel FIB (Forwarding Information Base). Command: <code>ip route add 192.168.10.0/24 via 10.0.0.1 dev eth0</code>, <code>ip route show</code>.", styles['bullet']))

    return story

# ==================== BUILD MODULE 3 CONTENT ====================
def get_module_3_story(styles):
    story = []
    add_header_banner(story, styles, "MODULE 3: Data Link Layer, Ethernet & Wireless LANs", 
                      "PCCST501 Computer Networks | Quick Exam Revision Guide | KTU S5 CSE | Prof. Anju Markose, VJCET")
    
    story.append(Paragraph("1. Data Link Control (DLC): Framing, Flow & Error Control", styles['h1']))
    story.append(Paragraph("<b>Framing Methods:</b>", styles['h2']))
    story.append(Paragraph("&bull; <b>Character Count:</b> Specifies number of characters in header (single bit error desynchronizes all subsequent frames).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Byte Stuffing:</b> Uses FLAG byte (e.g. 0x7E) with ESC escape bytes when FLAG appears in data payload.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Bit Stuffing (HDLC):</b> Flag = <code>01111110</code>. Sender inserts a '0' after every five consecutive '1's. Receiver strips the '0' following five '1's.", styles['bullet']))
    
    add_info_card(story, "<b>Cyclic Redundancy Check (CRC):</b><br/>"
                         "Given data bitstream M of length k and divisor polynomial G(x) of degree r:<br/>"
                         "1. Append r zeros to M (M * 2^r).<br/>"
                         "2. Perform Modulo-2 binary division (using XOR operations).<br/>"
                         "3. The r-bit remainder R is the Frame Check Sequence (FCS).<br/>"
                         "4. Transmit M followed by R. Receiver divides by G(x); if remainder is 0, frame is error-free.")

    story.append(Paragraph("2. Multiple Access Protocols (MAC)", styles['h1']))
    story.append(Paragraph("&bull; <b>Pure ALOHA:</b> Transmit immediately. Vulnerable period = 2 * T_fr. Max throughput S_max = 1/(2e) &asymp; <b>18.4%</b>.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Slotted ALOHA:</b> Transmit only at slot boundaries. Vulnerable period = T_fr. Max throughput S_max = 1/e &asymp; <b>36.8%</b>.", styles['bullet']))
    story.append(Paragraph("&bull; <b>CSMA/CD (Carrier Sense Multiple Access with Collision Detection):</b> Listen before and while transmitting. If collision occurs, transmit 32-bit jam signal and use <b>Binary Exponential Backoff</b> (wait k * 512 bit times, k in [0, 2^n - 1]).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Minimum Frame Size in CSMA/CD:</b> Frame transmission time must be at least 2 * Propagation delay: <code>L_min = 2 * d_prop * Bandwidth</code> (Standard Ethernet = 64 Bytes).", styles['bullet']))
    
    story.append(Paragraph("3. Link-Layer Addressing, Ethernet & Connecting Devices", styles['h1']))
    story.append(Paragraph("&bull; <b>MAC Address:</b> 48-bit (6 octets) globally unique physical address. First 24 bits = OUI (vendor), last 24 bits = NIC identifier.", styles['bullet']))
    story.append(Paragraph("&bull; <b>ARP Protocol:</b> Broadcasts ARP Request (<code>FF:FF:FF:FF:FF:FF</code>) to find MAC of target IP. Destination replies with unicast ARP Reply.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Standard Ethernet Frame (IEEE 802.3):</b> Preamble (7B) + SFD (1B) + Dst MAC (6B) + Src MAC (6B) + Type (2B) + Payload (46-1500B) + CRC FCS (4B).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Learning Switches & VLANs:</b> Switches automatically build MAC tables by recording source MAC of incoming frames. VLANs (IEEE 802.1Q) partition a physical switch into multiple isolated broadcast domains.", styles['bullet']))

    story.append(Paragraph("4. Wireless LANs (IEEE 802.11) & Mobile IP", styles['h1']))
    story.append(Paragraph("&bull; <b>IEEE 802.11 Architecture:</b> Basic Service Set (BSS) &rarr; Extended Service Set (ESS) connected via Distribution System (DS).", styles['bullet']))
    story.append(Paragraph("&bull; <b>CSMA/CA Protocol:</b> Uses DCF (Distributed Coordination Function) with SIFS < PIFS < DIFS inter-frame spaces and Network Allocation Vector (NAV).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Hidden & Exposed Node Problems:</b> Solved using optional RTS (Request to Send) / CTS (Clear to Send) 4-way handshake.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Mobile IP:</b> Mobile Node (MN) retains Home Address while assigning temporary Care-of Address (COA) via Foreign Agent (FA). Home Agent (HA) intercepts packets and tunnels them to FA (Triangle Routing).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Hands-on Raw Sockets:</b> <code>socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))</code> enables packet sniffing and frame injection at the link layer.", styles['bullet']))

    return story

# ==================== BUILD MODULE 4 CONTENT ====================
def get_module_4_story(styles):
    story = []
    add_header_banner(story, styles, "MODULE 4: Network Management & Physical Layer", 
                      "PCCST501 Computer Networks | Quick Exam Revision Guide | KTU S5 CSE | Prof. Anju Markose, VJCET")
    
    story.append(Paragraph("1. Network Management: SNMP & ASN.1", styles['h1']))
    story.append(Paragraph("<b>SNMP Architecture:</b> Manager (NMS), Managed Agent, Management Information Base (MIB), and Structure of Management Information (SMI).", styles['body']))
    story.append(Paragraph("&bull; <b>SNMP PDUs (UDP Port 161 Manager &rarr; Agent, Port 162 Agent &rarr; Manager):</b> <code>GetRequest</code>, <code>GetNextRequest</code>, <code>GetBulkRequest</code>, <code>SetRequest</code>, <code>Response</code>, <code>Trap</code> (unsolicited alarm), <code>InformRequest</code>.", styles['bullet']))
    story.append(Paragraph("&bull; <b>SNMP Versions:</b> SNMPv1 (plaintext community string), SNMPv2c (GetBulkRequest), SNMPv3 (USM user security: SHA/MD5 authentication + AES encryption; VACM view access control).", styles['bullet']))
    story.append(Paragraph("&bull; <b>ASN.1 (Abstract Syntax Notation One):</b> Formal language specifying data structures independently of machine architecture.", styles['bullet']))
    story.append(Paragraph("&bull; <b>BER (Basic Encoding Rules):</b> Encodes ASN.1 using TLV (Type-Length-Value) triplet format.", styles['bullet']))
    story.append(Paragraph("&bull; <b>MIB Tree & OID:</b> Hierarchical tree under <code>iso.org.dod.internet.mgmt.mib-2</code> (1.3.6.1.2.1). E.g. <code>sysDescr</code> = 1.3.6.1.2.1.1.1.", styles['bullet']))

    story.append(Paragraph("2. Physical Layer: Data, Signals & Capacity Limits", styles['h1']))
    story.append(Paragraph("<b>Transmission Impairments:</b> Attenuation (signal energy loss, measured in dB = 10 log10(P2/P1)), Distortion (phase shifts across harmonics), Noise (Thermal, Induced, Crosstalk, Impulse).", styles['body']))
    
    add_info_card(story, "<b>Theoretical Channel Capacity Formulas:</b><br/>"
                         "&bull; <b>Nyquist Bit Rate (Noiseless Channel):</b> C = 2 * B * log2(L) bps<br/>"
                         "   Where B = Bandwidth in Hz, L = Number of discrete signal levels.<br/>"
                         "&bull; <b>Shannon Capacity Theorem (Noisy Channel):</b> C = B * log2(1 + SNR) bps<br/>"
                         "   Where SNR is linear power ratio: SNR_dB = 10 * log10(SNR_linear). E.g., 30 dB &rarr; SNR = 1000.")

    story.append(Paragraph("3. Digital Transmission: Line Coding Techniques", styles['h1']))
    story.append(Paragraph("&bull; <b>Unipolar NRZ:</b> 1 = High voltage, 0 = 0V. Simple, but large DC component and clock synchronization loss.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Polar NRZ-L vs NRZ-I:</b> NRZ-L (0 = Positive, 1 = Negative). NRZ-I (Transition at bit boundary for 1, no transition for 0).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Manchester Encoding (IEEE 802.3):</b> 0 = High-to-Low transition, 1 = Low-to-High transition in middle of bit interval. Self-synchronizing, requires 2x bandwidth.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Differential Manchester:</b> Transition always present at mid-bit for clocking; transition at beginning represents 0, no transition at beginning represents 1.", styles['bullet']))
    story.append(Paragraph("&bull; <b>Bipolar AMI:</b> 0 = 0V, 1 = Alternating positive and negative voltages. Zero DC component; scrambled by B8ZS/HDB3 to prevent long runs of 0s.", styles['bullet']))

    story.append(Paragraph("4. Analog Transmission, Multiplexing & Media", styles['h1']))
    story.append(Paragraph("&bull; <b>Digital-to-Analog Modulation:</b> ASK (Amplitude Shift Keying), FSK (Frequency Shift Keying), PSK (Phase Shift Keying: BPSK, QPSK), QAM (Quadrature Amplitude Modulation: combines ASK + PSK; 16-QAM carries 4 bits/baud, 64-QAM carries 6 bits/baud).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Multiplexing:</b> FDM (Analog frequency bands), WDM (Optical light wavelengths over fiber), Synchronous TDM (Fixed time slots), Statistical TDM (On-demand time slots).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Guided Transmission Media:</b> Twisted Pair (UTP Cat 5e/6, STP), Coaxial Cable (copper conductor + mesh shield), Optical Fiber (Step-Index & Graded-Index, Single-mode vs Multi-mode; immune to EMI, immense bandwidth).", styles['bullet']))
    story.append(Paragraph("&bull; <b>Unguided Media:</b> Radio Waves (Omnidirectional, wall penetrating), Microwaves (Line-of-sight parabolic dish), Infrared (Short-range line of sight).", styles['bullet']))

    return story

# ==================== BUILD QUESTION BANK STORY ====================
def get_question_bank_story(styles):
    story = []
    add_header_banner(story, styles, "PCCST501 COMPUTER NETWORKS — COMPREHENSIVE QUESTION BANK", 
                      "Aligned with KTU Exam Pattern (Part A: 3-Mark & Part B: 9-Mark Questions) | Prof. Anju Markose, VJCET")
    
    modules_qb = [
        ("MODULE 1: Overview of Internet & Application Layer", [
            ("Part A (3 Marks Each)", [
                "1. Differentiate between packet switching and circuit switching with respect to resource allocation.",
                "2. Define transmission delay and propagation delay. State the formulas for both.",
                "3. Why is HTTP called a stateless protocol? How are cookies used to maintain session state?",
                "4. Differentiate between persistent and non-persistent HTTP connections.",
                "5. Why does FTP use two separate parallel TCP connections? Name their default port numbers.",
                "6. Distinguish between recursive and iterative DNS query resolution with suitable sketches.",
                "7. Explain the role of Type A, Type CNAME, and Type MX DNS resource records.",
                "8. How does BitTorrent achieve fast content distribution using the Rarest First piece selection policy?"
            ]),
            ("Part B (9 Marks Each)", [
                "1. (a) Explain the ISO-OSI 7-layer reference model in detail, highlighting the functions and PDUs of each layer. (6 Marks)<br/>   (b) Illustrate the encapsulation and decapsulation process as data traverses through the protocol stack. (3 Marks)",
                "2. (a) Describe the architecture and protocol flow of the File Transfer Protocol (FTP). Differentiate between Active and Passive FTP modes. (5 Marks)<br/>   (b) Explain the components and message exchange in Electronic Mail (SMTP, POP3, IMAP4, and MIME). (4 Marks)",
                "3. (a) Explain the Domain Name System (DNS) architecture, server hierarchy, and DNS caching mechanism in detail. (5 Marks)<br/>   (b) Describe the Peer-to-Peer (P2P) file distribution paradigm. Explain the Tit-for-Tat and Optimistic Unchoking algorithms in BitTorrent. (4 Marks)"
            ])
        ]),
        ("MODULE 2: Transport Layer & Network Layer", [
            ("Part A (3 Marks Each)", [
                "1. Differentiate between UDP and TCP protocols based on reliability, connection state, and header overhead.",
                "2. Explain the 3-Way Handshake mechanism for TCP connection establishment with sequence numbers.",
                "3. What is Silly Window Syndrome? How is it resolved by Nagle's and Clark's algorithms?",
                "4. Distinguish between TCP Tahoe and TCP Reno on receiving 3 duplicate ACKs.",
                "5. Differentiate between select() and poll() I/O multiplexing system calls in Linux.",
                "6. What is the Count-to-Infinity problem in Distance Vector routing? How does Split Horizon resolve it?",
                "7. Differentiate between Leaky Bucket and Token Bucket traffic shaping algorithms.",
                "8. Compare the base header features of IPv4 and IPv6."
            ]),
            ("Part B (9 Marks Each)", [
                "1. (a) Explain the TCP Congestion Control mechanism in detail, explaining Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery phases with a cwnd vs RTT graph. (6 Marks)<br/>   (b) Explain the calculation of the 16-bit UDP checksum using pseudo-header. (3 Marks)",
                "2. (a) An organization is granted the block 192.168.10.0/24. Subnet this block to create 4 subnets. Find the subnet mask, network address, broadcast address, and usable host range for each subnet. (5 Marks)<br/>   (b) Explain the working of Dijkstra's Link-State Routing Algorithm with an example network graph. (4 Marks)",
                "3. (a) Explain the implementation of the Linux Kernel routing table (fib_table) and route cache. Provide the syntax to add and delete routes using the `ip route` command. (5 Marks)<br/>   (b) Describe Multicast Routing concepts, IGMP, and compare DVMRP with PIM-SM routing protocols. (4 Marks)"
            ])
        ]),
        ("MODULE 3: Data Link Layer, Ethernet & Wireless LANs", [
            ("Part A (3 Marks Each)", [
                "1. Explain the Bit Stuffing and Byte Stuffing framing mechanisms in Data Link Control.",
                "2. Compare the maximum throughputs of Pure ALOHA and Slotted ALOHA protocols.",
                "3. Why is collision detection (CSMA/CD) not feasible in wireless networks? What protocol is used instead?",
                "4. Derive the minimum frame size equation in Ethernet CSMA/CD networks.",
                "5. Explain the working and packet formats of Address Resolution Protocol (ARP).",
                "6. How does a Learning Switch build its forwarding table dynamically?",
                "7. Explain the Hidden Terminal and Exposed Terminal problems in IEEE 802.11 Wireless LANs.",
                "8. What is Triangle Routing in Mobile IP? How is it optimized?"
            ]),
            ("Part B (9 Marks Each)", [
                "1. (a) A bit stream 1101011011 is transmitted using the CRC generator polynomial G(x) = x^4 + x + 1. Calculate the transmitted frame FCS. Show how the receiver detects errors. (5 Marks)<br/>   (b) Explain the 7-bit Hamming Code generation and error correction for data word 1011. (4 Marks)",
                "2. (a) Explain the IEEE 802.3 Standard Ethernet frame format in detail. Discuss the evolution from 10 Mbps to Gigabit and 10-Gigabit Ethernet. (5 Marks)<br/>   (b) Explain Virtual LANs (VLAN - IEEE 802.1Q) and explain how VLAN tagging isolates broadcast domains. (4 Marks)",
                "3. (a) Explain the IEEE 802.11 MAC sublayer operations including CSMA/CA, NAV, Inter-Frame Spaces (SIFS, PIFS, DIFS), and RTS/CTS handshake. (5 Marks)<br/>   (b) Explain the implementation of packet capturing using Linux raw sockets with SOCK_PACKET and PF_PACKET. (4 Marks)"
            ])
        ]),
        ("MODULE 4: Network Management & Physical Layer", [
            ("Part A (3 Marks Each)", [
                "1. List the key components of the SNMP Network Management architecture.",
                "2. Differentiate between SNMPv1, SNMPv2c, and SNMPv3 with respect to security and performance.",
                "3. Explain the Type-Length-Value (TLV) encoding in ASN.1 Basic Encoding Rules (BER).",
                "4. State Nyquist's Bit Rate formula and Shannon's Channel Capacity theorem.",
                "5. Differentiate between Manchester and Differential Manchester line coding techniques.",
                "6. Explain Quadrature Amplitude Modulation (QAM). How many bits/baud does 16-QAM carry?",
                "7. Compare Synchronous TDM and Statistical TDM multiplexing techniques.",
                "8. Compare Single-Mode and Multi-Mode optical fibers."
            ]),
            ("Part B (9 Marks Each)", [
                "1. (a) Explain the SNMP protocol operations (GetRequest, GetBulkRequest, SetRequest, Trap) and the MIB-2 tree hierarchy with Object Identifiers (OIDs). (5 Marks)<br/>   (b) Explain the ASN.1 data structure definition and encode an example INTEGER and OCTET STRING using BER TLV format. (4 Marks)",
                "2. (a) Calculate the theoretical maximum capacity of a noisy telephone channel having a bandwidth of 4 kHz and a Signal-to-Noise Ratio (SNR) of 30 dB using Shannon's theorem. If we use 16 signal levels, what is the Nyquist bit rate? (5 Marks)<br/>   (b) Draw the digital signal waveforms for the bit sequence 01001110 using: (i) NRZ-L, (ii) NRZ-I, (iii) Manchester, (iv) Differential Manchester, (v) Bipolar AMI. (4 Marks)",
                "3. (a) Explain Frequency Division Multiplexing (FDM), Wavelength Division Multiplexing (WDM), and Time Division Multiplexing (TDM) in detail. (5 Marks)<br/>   (b) Discuss the physical characteristics, advantages, and limitations of Twisted Pair, Coaxial Cable, and Optical Fiber guided media. (4 Marks)"
            ])
        ])
    ]
    
    for mod_title, sections in modules_qb:
        story.append(Paragraph(mod_title, styles['h1']))
        for sec_title, q_list in sections:
            story.append(Paragraph(sec_title, styles['h2']))
            for q in q_list:
                story.append(Paragraph(f"&bull; {q}", styles['bullet']))
        story.append(Spacer(1, 8))
        
    return story

# ==================== BUILD LAB MANUAL STORY ====================
def get_lab_manual_story(styles):
    story = []
    add_header_banner(story, styles, "PCCST501 COMPUTER NETWORKS — HANDS-ON LAB MANUAL", 
                      "Module-wise Hands-on Implementations in C & Python | Prof. Anju Markose, VJCET")
    
    labs = [
        ("MODULE 1 LAB: Wireshark HTTP / DNS & Python Socket Client", 
         "1. Wireshark Packet Sniffing: Capture HTTP GET requests and analyze headers, 200 OK responses, cookies, and cache control headers.<br/>"
         "2. Python Web Client: Implementing basic HTTP GET / DNS resolver script using Python socket library.",
         """# Python HTTP Client Example
import socket

host = "example.com"
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
req = f"GET / HTTP/1.1\\r\\nHost: {host}\\r\\nConnection: close\\r\\n\\r\\n"
s.sendall(req.encode())
res = s.recv(4096)
print(res.decode('utf-8', errors='ignore'))
s.close()"""),
        ("MODULE 2 LAB: TCP/UDP Sockets, I/O Multiplexing (select/poll) & Linux Routing",
         "1. TCP Multi-Client Echo Server in C using select() / poll() system calls.<br/>"
         "2. Elementary UDP Client-Server program.<br/>"
         "3. Linux Routing Table Configuration: Using `ip route` commands to inspect FIB and add static routing entries.",
         """// TCP Server using select() multiplexing snippet
fd_set readfds;
FD_ZERO(&readfds);
FD_SET(server_fd, &readfds);
int max_sd = server_fd;

int activity = select(max_sd + 1, &readfds, NULL, NULL, NULL);
if (FD_ISSET(server_fd, &readfds)) {
    int new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen);
    printf("New client connected on socket %d\\n", new_socket);
}"""),
        ("MODULE 3 LAB: Raw Sockets (PF_PACKET), Frame Sniffing & CRC Generator",
         "1. Linux Raw Socket Packet Sniffer using `PF_PACKET` and `SOCK_RAW` to capture Ethernet frames.<br/>"
         "2. CRC Error Detection algorithm implemented in C / Python.",
         """#include <stdio.h>
#include <sys/socket.h>
#include <netinet/if_ether.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int sock_raw = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    unsigned char buffer[65536];
    while(1) {
        int data_size = recvfrom(sock_raw, buffer, 65536, 0, NULL, NULL);
        struct ethhdr *eth = (struct ethhdr *)buffer;
        printf("Frame: Dest: %.2X:%.2X:%.2X:%.2X:%.2X:%.2X Proto: 0x%04X\\n",
               eth->h_dest[0], eth->h_dest[1], eth->h_dest[2],
               eth->h_dest[3], eth->h_dest[4], eth->h_dest[5], ntohs(eth->h_proto));
    }
    close(sock_raw);
    return 0;
}"""),
        ("MODULE 4 LAB: SNMP Network Management & Line Coding Generator",
         "1. SNMP Walk and Get in Linux using `net-snmp` utilities.<br/>"
         "2. Line Coding Generator: Python script generating NRZ, Manchester, and AMI signal representations.",
         """# SNMP Query Example using pysnmp / net-snmp command
# Shell command:
# snmpget -v2c -c public 127.0.0.1 1.3.6.1.2.1.1.1.0
# snmpwalk -v2c -c public 127.0.0.1 1.3.6.1.2.1.2.2.1.2 (Interfaces)

def line_code_manchester(bits):
    signal = []
    for b in bits:
        if b == 0:
            signal.extend([1, -1]) # High to Low
        else:
            signal.extend([-1, 1]) # Low to High
    return signal""")
    ]
    
    for title, desc, code in labs:
        story.append(Paragraph(title, styles['h1']))
        story.append(Paragraph(desc, styles['body']))
        story.append(Paragraph(f"<pre>{code.replace('<', '&lt;').replace('>', '&gt;')}</pre>", styles['code']))
        story.append(Spacer(1, 8))
        
    return story

# ==================== MAIN PDF EXPORT ====================
def main():
    os.makedirs("assets/notes_pdf", exist_ok=True)
    styles = get_styles()
    
    # 1. Module 1 Notes PDF
    doc1 = SimpleDocTemplate("assets/notes_pdf/Module_1_Exam_Revision_Notes.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    doc1.build(get_module_1_story(styles), canvasmaker=NumberedCanvas)
    print("Generated Module_1_Exam_Revision_Notes.pdf")
    
    # 2. Module 2 Notes PDF
    doc2 = SimpleDocTemplate("assets/notes_pdf/Module_2_Exam_Revision_Notes.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    doc2.build(get_module_2_story(styles), canvasmaker=NumberedCanvas)
    print("Generated Module_2_Exam_Revision_Notes.pdf")
    
    # 3. Module 3 Notes PDF
    doc3 = SimpleDocTemplate("assets/notes_pdf/Module_3_Exam_Revision_Notes.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    doc3.build(get_module_3_story(styles), canvasmaker=NumberedCanvas)
    print("Generated Module_3_Exam_Revision_Notes.pdf")
    
    # 4. Module 4 Notes PDF
    doc4 = SimpleDocTemplate("assets/notes_pdf/Module_4_Exam_Revision_Notes.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    doc4.build(get_module_4_story(styles), canvasmaker=NumberedCanvas)
    print("Generated Module_4_Exam_Revision_Notes.pdf")
    
    # 5. Master Notes PDF (All Modules)
    doc_all = SimpleDocTemplate("assets/notes_pdf/PCCST501_Complete_CN_Exam_Notes.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    all_story = []
    all_story.extend(get_module_1_story(styles))
    all_story.append(PageBreak())
    all_story.extend(get_module_2_story(styles))
    all_story.append(PageBreak())
    all_story.extend(get_module_3_story(styles))
    all_story.append(PageBreak())
    all_story.extend(get_module_4_story(styles))
    doc_all.build(all_story, canvasmaker=NumberedCanvas)
    print("Generated PCCST501_Complete_CN_Exam_Notes.pdf")
    
    # 6. Question Bank PDF
    doc_qb = SimpleDocTemplate("assets/notes_pdf/PCCST501_Comprehensive_Question_Bank.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    doc_qb.build(get_question_bank_story(styles), canvasmaker=NumberedCanvas)
    print("Generated PCCST501_Comprehensive_Question_Bank.pdf")
    
    # 7. Lab Manual PDF
    doc_lab = SimpleDocTemplate("assets/notes_pdf/PCCST501_HandsOn_Lab_Manual.pdf", pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    doc_lab.build(get_lab_manual_story(styles), canvasmaker=NumberedCanvas)
    print("Generated PCCST501_HandsOn_Lab_Manual.pdf")

if __name__ == "__main__":
    main()
