"""
ppts_module2_detailed.py
Comprehensive, classroom-ready presentation decks for Module 2: Transport & Network Layer Architecture.
Prepared exclusively for:
Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
PCCST501 Computer Networks (KTU 2024 Scheme)
"""

from build_master_ppts_framework import (
    init_prs, create_title_slide, create_content_slide, 
    create_comparison_slide, create_numerical_slide, create_code_slide, create_exam_booster_slide
)

def build_m2_1_1(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.1.1", "Transport Layer Services & Multiplexing Principles",
        "Process-to-Process Communication, Port Addressing, Connectionless vs Connection-Oriented Demultiplexing (2-Tuple vs 4-Tuple)",
        "Module 2"
    )
    
    create_content_slide(prs, "2.1.1.1 Transport Layer Core Responsibilities", "M2.1.1 TRANSPORT SERVICES", [
        ("Process-to-Process Logical Delivery", "While the Network Layer delivers packets host-to-host between IP addresses, the Transport Layer extends this to deliver messages process-to-process between application sockets."),
        ("Port Addressing & Socket Binding", "Processes are identified via 16-bit Port Numbers (0 to 65,535). Sockets bind an IP address and Port number together as an end-to-end communication endpoint."),
        ("Transport Layer Responsibilities", "1. Multiplexing & Demultiplexing, 2. Reliability (Loss detection, ACKs, retransmissions), 3. Flow Control (Preventing receiver buffer overflow), 4. Congestion Control (Preventing network core collapse)."),
        ("Transport Limitations", "Transport protocols cannot provide hard real-time delay bounds or guaranteed bandwidth on standard best-effort IP networks.")
    ], "Key Port Numbers", [
        "Port 80: HTTP",
        "Port 443: HTTPS",
        "Port 22: SSH",
        "Port 53: DNS",
        "Port 25: SMTP",
        "Port 21: FTP Control"
    ])
    
    create_comparison_slide(prs, "2.1.1.2 Demultiplexing: Connectionless (UDP) vs Connection-Oriented (TCP)", "M2.1.1 DEMULTIPLEXING",
        "UDP Demultiplexing (2-Tuple)", [
            ("Identifier Tuple", "Identified strictly by: `(Destination IP, Destination Port)`"),
            ("Behavior", "Two UDP datagrams arriving from different source IP/ports targeted at same Dest Port are delivered to the exact same socket"),
            ("State", "Completely stateless; no connection handshake or per-peer buffers"),
            ("Speed", "Zero connection establishment latency")
        ],
        "TCP Demultiplexing (4-Tuple)", [
            ("Identifier Tuple", "Identified by 4-tuple: `(Source IP, Source Port, Destination IP, Destination Port)`"),
            ("Behavior", "Server listening socket (`listen()`) forks/spawns a distinct connected socket (`accept()`) for each unique client 4-tuple"),
            ("State", "Full connection state, sequence tracking, and dedicated receive buffers per connection"),
            ("Scalability", "Enables concurrent multi-client web/database servers")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M2.1.1", "Transport Layer Services", "K2 Understand",
        [
            "Differentiate between host-to-host delivery and process-to-process delivery with a neat diagram. (6 Marks)",
            "Explain how multiplexing and demultiplexing work in UDP and TCP. Why does TCP require a 4-tuple while UDP needs only a 2-tuple? (8 Marks)"
        ],
        [
            "Network layer provides host-to-host IP delivery; Transport layer provides process-to-process port delivery.",
            "UDP demux uses Destination Port only; TCP demux uses Source IP, Source Port, Dest IP, Dest Port.",
            "TCP creates separate connected sockets for every distinct client connection."
        ]
    )
    return prs

def build_m2_1_2(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.1.2", "Transport Protocols & User Datagram Protocol (UDP)",
        "UDP Segment Header Structure, 16-Bit 1's Complement Checksum with Pseudo-Header, UDP Applications & Use Cases",
        "Module 2"
    )
    
    create_content_slide(prs, "2.1.2.1 UDP Protocol Architecture & 8-Byte Header", "M2.1.2 UDP ARCHITECTURE", [
        ("UDP Characteristics (RFC 768)", "Connectionless, unreliable, lightweight, message-oriented transport protocol. Provides bare minimum services: process multiplexing and optional error checking."),
        ("Why Use UDP?", "1. No connection establishment delay (0-RTT), 2. No connection state at server, 3. Small header overhead (8 bytes vs TCP 20 bytes), 4. Unregulated send rate (no congestion throttling)."),
        ("UDP 8-Byte Header Format (32-bit width)", "Source Port (16 bits) | Destination Port (16 bits) \\n Length (16 bits, header + payload in bytes) | Checksum (16 bits)."),
        ("Message Boundary Preservation", "UDP sends data in discrete datagrams. If sender writes 500 bytes twice, receiver reads 500 bytes twice (preserves message boundaries, unlike TCP byte stream).")
    ], "Header Breakdown", [
        "Source Port: 16 bits",
        "Destination Port: 16 bits",
        "Length: 16 bits (Min 8 B)",
        "Checksum: 16 bits",
        "Total Header: Exactly 8 Bytes"
    ])
    
    create_numerical_slide(
        prs, "2.1.2.2 UDP 16-Bit 1's Complement Checksum Calculation", "M2.1.2 CHECKSUM CALCULATION",
        "Compute the UDP checksum for three 16-bit words: Word 1 = 0x66B4 (0110 0110 1011 0100), Word 2 = 0x5555 (0101 0101 0101 0101), Word 3 = 0x8F0C (1000 1111 0000 1100). Show wraparound carry addition and 1's complement inversion. Also explain how the receiver verifies checksum integrity.",
        [
            "Step 1: Sum 16-bit words using standard binary addition.",
            "Step 2: If sum produces a 17th bit (carry overflow), wrap it around and add to the least significant bit.",
            "Step 3: Invert all bits (1's complement) to obtain the transmitted Checksum field.",
            "Receiver: Sums all received words including Checksum; valid result must be 0xFFFF (all 1s)."
        ],
        [
            (1, "Sum Word 1 + Word 2: 0x66B4 + 0x5555 = 0xBC09 (1011 1100 0000 1001)"),
            (2, "Add Word 3: 0xBC09 + 0x8F0C = 0x14B15 (1 0100 1011 0001 0101 - Carry generated!)"),
            (3, "Wrap carry around: 0x4B15 + 1 = 0x4B16 (0100 1011 0001 0110)"),
            (4, "Take 1's complement (~0x4B16): 1011 0100 1110 1001 = 0xB4E9 (Checksum transmitted)"),
            (5, "Receiver Verification: 0x4B16 + 0xB4E9 = 0xFFFF (1111 1111 1111 1111 -> Verified Valid!)")
        ],
        "Transmitted Checksum = 0xB4E9 | Receiver sum = 0xFFFF",
        "Note: UDP includes an IP Pseudo-Header (Source IP, Dest IP, Protocol 17, UDP Length) in checksum calculation to detect misrouted packets."
    )
    
    create_exam_booster_slide(
        prs, "M2.1.2", "UDP Protocol & Checksum", "K3 Apply",
        [
            "Draw the UDP segment header format and explain all fields. Why is UDP header size fixed at 8 bytes? (6 Marks)",
            "Explain the step-by-step procedure for computing the UDP 16-bit 1's complement checksum. What is the role of the pseudo-header? (8 Marks)",
            "Why is UDP preferred over TCP for DNS queries, SNMP, and real-time gaming? (5 Marks)"
        ],
        [
            "UDP header is minimal (8 bytes) with Source Port, Dest Port, Length, and Checksum.",
            "Checksum calculation wraps around carry bits and inverts result for easy receiver verification (0xFFFF).",
            "UDP avoids TCP connection overhead and latency fluctuations from retransmissions."
        ]
    )
    return prs

def build_m2_1_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.1.3", "Transmission Control Protocol (TCP) Architecture",
        "TCP 20-Byte Header Format, 3-Way Handshake Connection Setup, 4-Way Connection Teardown (TIME_WAIT 2MSL), Sequence/ACK Mechanics",
        "Module 2"
    )
    
    create_content_slide(prs, "2.1.3.1 TCP Header Architecture (RFC 793 / 9293)", "M2.1.3 TCP HEADER", [
        ("Connection-Oriented Byte Stream", "TCP provides full-duplex, reliable, sequenced byte-stream transfer between communicating processes."),
        ("Header Format (20 to 60 Bytes)", "Source Port (16b) | Destination Port (16b) \\n Sequence Number (32b: byte-stream offset) \\n Acknowledgment Number (32b: next expected byte) \\n Data Offset (4b: header length in 32-bit words) | Reserved (4b) | Flags (8b) | Window Size (16b) \\n Checksum (16b) | Urgent Pointer (16b) \\n Options (0 to 40 bytes: MSS, Window Scale, SACK, Timestamps)."),
        ("TCP Control Flags", "SYN (Establish connection), ACK (Ack valid), FIN (Close connection), RST (Reset/abort connection), PSH (Push data immediately to app), URG (Urgent pointer active), ECE & CWR (Explicit Congestion Notification)."),
        ("Cumulative Acknowledgment", "TCP Ack number $N$ indicates the receiver has successfully received all contiguous bytes up to $N-1$ and is expecting byte $N$.")
    ], "TCP Control Flags", [
        "SYN: Connection request",
        "ACK: Acknowledgment field",
        "FIN: Graceful teardown",
        "RST: Reset connection",
        "PSH: Push buffer to app",
        "URG: Out-of-band data"
    ])
    
    create_comparison_slide(prs, "2.1.3.2 Connection Lifecycle: 3-Way Handshake vs 4-Way Teardown", "M2.1.3 TCP LIFECYCLE",
        "3-Way Handshake (Connection Setup)", [
            ("Step 1 (Client -> Server)", "Client sends `SYN = 1`, `Seq = x` (Initial Sequence Number $ISN_c$). Enters `SYN_SENT` state"),
            ("Step 2 (Server -> Client)", "Server allocates buffers, replies `SYN = 1`, `ACK = 1`, `Seq = y` ($ISN_s$), `Ack = x + 1`. Enters `SYN_RCVD`"),
            ("Step 3 (Client -> Server)", "Client sends `ACK = 1`, `Seq = x + 1`, `Ack = y + 1` (may piggyback initial application data). Enters `ESTABLISHED`"),
            ("SYN Flood Defense", "TCP SYN Cookies prevent server memory exhaustion from bogus SYN requests")
        ],
        "4-Way Connection Teardown (Graceful Close)", [
            ("Step 1 (Client -> Server)", "Client finishes sending, transmits `FIN = 1`, `Seq = u`. Enters `FIN_WAIT_1`"),
            ("Step 2 (Server -> Client)", "Server acknowledges with `ACK = 1`, `Ack = u + 1`. Enters `CLOSE_WAIT`; Client enters `FIN_WAIT_2`"),
            ("Step 3 (Server -> Client)", "Server finishes outstanding data, transmits `FIN = 1`, `Seq = v`. Enters `LAST_ACK`"),
            ("Step 4 (Client -> Server)", "Client replies `ACK = 1`, `Ack = v + 1`. Client enters `TIME_WAIT` for 2MSL (Maximum Segment Lifetime = 60-120s) before terminating to ensure final ACK delivery")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M2.1.3", "TCP Connection Management", "K3 Apply",
        [
            "Draw the complete TCP segment header format and explain all fields, especially Sequence Number, ACK Number, and Control Flags. (8 Marks)",
            "Illustrate the TCP 3-Way Handshake with sequence and acknowledgment numbers. Why is a 2-way handshake insufficient? (8 Marks)",
            "Explain the purpose of the `TIME_WAIT` state and the 2MSL timer during TCP connection termination. (5 Marks)"
        ],
        [
            "TCP Sequence number tracks the byte offset of transmitted data; ACK number represents the next expected byte.",
            "3-way handshake is mandatory to synchronize Initial Sequence Numbers (ISNs) bi-directionally and verify full-duplex connectivity.",
            "`TIME_WAIT` (2MSL) guarantees that any lingering duplicate packets in the network expire before the socket is reused."
        ]
    )
    return prs

def build_m2_1_4(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.1.4", "TCP Flow & Congestion Control Mechanisms",
        "Sliding Window Flow Control, Silly Window Syndrome, Congestion Window (cwnd), Slow Start, AIMD, Fast Retransmit, TCP Tahoe vs Reno",
        "Module 2"
    )
    
    create_content_slide(prs, "2.1.4.1 Flow Control & Silly Window Syndrome", "M2.1.4 FLOW CONTROL", [
        ("Flow Control Goal", "Matches the sender's transmission rate to the receiver's consumption rate to prevent receiver buffer overflow."),
        ("Receive Window (`rwnd`) Mechanics", "Receiver advertises remaining buffer space via `rwnd` field in TCP header. Sender ensures: $\\text{LastByteSent} - \\text{LastByteAcked} \\le \\min(\\text{cwnd}, \\text{rwnd})$."),
        ("Zero-Window Probing", "When receiver buffer is full (`rwnd = 0`), sender stops transmitting but periodically sends 1-byte probe segments to force receiver to return window update ACKs."),
        ("Silly Window Syndrome (SWS)", "Occurs when data is transmitted in tiny chunks (1 byte payload + 40 bytes header = 97.5% overhead)."),
        ("SWS Solutions", "1. **Nagle's Algorithm (Sender-side)**: Send first small segment; buffer subsequent data until all previous data is ACKed or MSS is reached. 2. **Clark's Solution (Receiver-side)**: Receiver advertises `rwnd = 0` until buffer space is at least MSS or 50% buffer capacity.")
    ], "Key Variables", [
        "rwnd: Receiver buffer limit",
        "cwnd: Network congestion limit",
        "Effective Win = min(cwnd, rwnd)",
        "Nagle's: Buffers small writes",
        "Clark's: Suppresses tiny rwnd"
    ])
    
    create_comparison_slide(prs, "2.1.4.2 Congestion Control: TCP Tahoe vs TCP Reno", "M2.1.4 TAHOE VS RENO",
        "TCP Tahoe (Legacy)", [
            ("Slow Start Phase", "Begins with `cwnd = 1 MSS`. Increases `cwnd` exponentially: doubles every RTT (`cwnd += 1 MSS` per ACK received)"),
            ("Congestion Avoidance", "When `cwnd >= ssthresh`, transitions to AIMD: increases `cwnd` linearly by 1 MSS per RTT"),
            ("On Loss Detection (Timeout or 3 Dup ACKs)", "1. `ssthresh = cwnd / 2` \\n 2. Drops `cwnd = 1 MSS` (always resets to slow start)"),
            ("Performance", "Severe throughput collapse upon any single packet loss")
        ],
        "TCP Reno (Standard)", [
            ("Slow Start & Congestion Avoidance", "Identical to Tahoe during normal growth"),
            ("On Timeout Loss", "Severe congestion: `ssthresh = cwnd / 2`, `cwnd = 1 MSS` (resets to Slow Start)"),
            ("On 3 Duplicate ACKs (Fast Retransmit)", "Mild congestion: Retransmits lost segment immediately without waiting for retransmission timer to expire"),
            ("Fast Recovery Phase", "Skips slow start! Sets `ssthresh = cwnd / 2`, sets `cwnd = ssthresh + 3 MSS`, continues linear AIMD growth")
        ]
    )
    
    create_numerical_slide(
        prs, "2.1.4.3 Worked KTU Numerical: TCP Congestion Window Evolution", "M2.1.4 WORKED PROBLEM",
        "A TCP Reno connection has ssthresh = 16 MSS. Starting at RTT 1 with cwnd = 1 MSS in Slow Start: (a) Trace cwnd values up to RTT 8. (b) At RTT 8, three duplicate ACKs are received. Calculate new ssthresh and cwnd for RTT 9 and RTT 10 under Fast Recovery.",
        [
            "Slow Start: cwnd doubles every RTT until ssthresh is reached.",
            "Congestion Avoidance (AIMD): cwnd increases by +1 MSS per RTT.",
            "Fast Retransmit / Fast Recovery (3 Dup ACKs): ssthresh_new = cwnd / 2, cwnd_new = ssthresh_new."
        ],
        [
            (1, "RTT 1: cwnd = 1 MSS (Slow Start)"),
            (2, "RTT 2: cwnd = 2 MSS | RTT 3: cwnd = 4 MSS | RTT 4: cwnd = 8 MSS | RTT 5: cwnd = 16 MSS (ssthresh reached)"),
            (3, "RTT 6: cwnd = 17 MSS (AIMD Linear) | RTT 7: cwnd = 18 MSS | RTT 8: cwnd = 19 MSS"),
            (4, "At RTT 8, 3 Dup ACKs occur: ssthresh_new = 19 / 2 = 9.5 -> 9 MSS."),
            (5, "RTT 9: Under TCP Reno Fast Recovery, cwnd = 9 MSS. RTT 10: cwnd = 10 MSS (continues linear AIMD).")
        ],
        "RTT 8: 19 MSS -> Loss -> RTT 9: cwnd = 9 MSS, ssthresh = 9 MSS",
        "If loss was caused by Timeout instead of 3 Dup ACKs, cwnd would drop to 1 MSS."
    )
    
    create_exam_booster_slide(
        prs, "M2.1.4", "TCP Flow & Congestion Control", "K3 Apply",
        [
            "Explain TCP Sliding Window flow control and how the receiver window `rwnd` prevents buffer overrun. (7 Marks)",
            "What is Silly Window Syndrome? Explain Nagle's algorithm and Clark's solution with examples. (8 Marks)",
            "Compare TCP Tahoe and TCP Reno congestion control algorithms with a neat graph plotting `cwnd` versus Transmission RTTs. (8 Marks)"
        ],
        [
            "Flow control is receiver-driven (`rwnd`); Congestion control is network-driven (`cwnd`).",
            "Effective transmission window is the minimum of `cwnd` and `rwnd`.",
            "TCP Reno avoids slow start upon 3 duplicate ACKs via Fast Retransmit and Fast Recovery."
        ]
    )
    return prs

def build_m2_1_5(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.1.5", "Berkeley Socket API & I/O Multiplexing",
        "Socket System Calls Lifecycle (TCP & UDP), I/O Multiplexing with select() and poll(), fd_set Macros, Non-Blocking Sockets",
        "Module 2"
    )
    
    create_content_slide(prs, "2.1.5.1 Berkeley Socket API System Call Lifecycle", "M2.1.5 SOCKET API", [
        ("Socket Abstraction", "A socket is a kernel endpoint for network I/O represented as an integer file descriptor in Linux (`int sockfd`)."),
        ("TCP Server Lifecycle", "1. `socket(AF_INET, SOCK_STREAM, 0)` -> Creates endpoint \\n 2. `bind(sockfd, &addr, sizeof)` -> Associates socket with IP/Port \\n 3. `listen(sockfd, backlog)` -> Sets passive listening mode and backlog queue \\n 4. `accept(sockfd, &client_addr, &len)` -> Blocks until client connects, returns new connected descriptor \\n 5. `read()` / `write()` or `recv()` / `send()` -> Data exchange \\n 6. `close(sockfd)` -> Tears down connection."),
        ("TCP Client Lifecycle", "1. `socket()` -> 2. `connect(sockfd, &server_addr, sizeof)` (initiates 3-way handshake) -> 3. `write()` / `read()` -> 4. `close()`."),
        ("UDP Sockets", "Connectionless: Server calls `socket()` -> `bind()` -> `recvfrom()` -> `sendto()`. Client calls `socket()` -> `sendto()` -> `recvfrom()` without `listen()` or `accept()`.")
    ], "Key System Calls", [
        "socket(): Create fd",
        "bind(): Bind IP & Port",
        "listen(): Passive queue",
        "accept(): Return client fd",
        "connect(): 3-way handshake",
        "sendto()/recvfrom(): UDP"
    ])
    
    code_select_example = """#include <sys/select.h>
int max_fd = listen_fd;
fd_set read_fds;

while (1) {
    FD_ZERO(&read_fds);
    FD_SET(listen_fd, &read_fds);
    // Add active client descriptors
    for (int i = 0; i < max_clients; i++) {
        if (client_fds[i] > 0) FD_SET(client_fds[i], &read_fds);
        if (client_fds[i] > max_fd) max_fd = client_fds[i];
    }
    // Block until at least one descriptor is ready for read
    int activity = select(max_fd + 1, &read_fds, NULL, NULL, NULL);
    if (FD_ISSET(listen_fd, &read_fds)) {
        int new_fd = accept(listen_fd, ...);
        // Add new_fd to client list
    }
}"""
    create_code_slide(
        prs, "2.1.5.2 I/O Multiplexing: `select()` System Call", "M2.1.5 IO MULTIPLEXING",
        code_select_example,
        [
            ("Why I/O Multiplexing?", "Allows a single-threaded server process to monitor multiple socket descriptors simultaneously without blocking on any single slow client."),
            ("`fd_set` Bitmask Macros", "`FD_ZERO(&set)` clears mask, `FD_SET(fd, &set)` adds fd, `FD_CLR(fd, &set)` removes fd, `FD_ISSET(fd, &set)` tests readiness."),
            ("`select()` Parameters", "`int select(int nfds, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, struct timeval *timeout)`. `nfds` is `max_fd + 1`."),
            ("`poll()` vs `select()`", "`poll()` uses array of `struct pollfd` (no `FD_SETSIZE` 1024 descriptor limit and separate input/output events).")
        ],
        "Single-threaded I/O multiplexing handles hundreds of concurrent connections with minimal memory overhead compared to multi-threading."
    )
    
    create_exam_booster_slide(
        prs, "M2.1.5", "Socket API & select()", "K3 Apply",
        [
            "Write the sequence of Berkeley socket system calls executed on both server and client for TCP connection establishment and data transfer. (8 Marks)",
            "Explain the working of I/O multiplexing using the `select()` system call with code structure and `fd_set` macros. (8 Marks)",
            "Differentiate between blocking, non-blocking, and I/O multiplexed socket architectures. (6 Marks)"
        ],
        [
            "`listen()` creates a passive socket queue; `accept()` extracts the next connection from the queue.",
            "`select()` monitors multiple file descriptors simultaneously, unblocking as soon as any fd is ready.",
            "`poll()` and `epoll()` overcome the 1024 file descriptor limitation of traditional `select()`."
        ]
    )
    return prs

def build_m2_2_1(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.1", "Network Layer Architecture & Router Design",
        "Data Plane (Forwarding) vs Control Plane (Routing), Datagram Networks vs Virtual Circuits, Router Fabrics & Buffer Queuing",
        "Module 2"
    )
    
    create_content_slide(prs, "2.2.1.1 Network Layer: Data Plane vs Control Plane", "M2.2.1 NETWORK ARCHITECTURE", [
        ("Network Layer Core Mission", "Achieving end-to-end host-to-host packet delivery across multiple heterogeneous intermediate networks."),
        ("Data Plane (Forwarding)", "Local, per-router action. Takes a packet arriving on an input link interface and moves it to the appropriate output link interface in nanoseconds. Implemented in high-speed hardware ASIC/TCAM."),
        ("Control Plane (Routing)", "Network-wide logic. Determines the end-to-end global path that packets take from source to destination. Implemented in software routing algorithms (OSPF, RIP, BGP) or centralized SDN controllers."),
        ("Service Models", "Internet uses Best-Effort Service Model: no guarantees on delivery, delay, bandwidth, or ordering. Simplicity in the network core pushed intelligence to end hosts.")
    ], "Plane Separation", [
        "Data Plane: Local forwarding (ASIC/Hardware)",
        "Control Plane: Global routing (Software/OSPF)",
        "Nanosecond speed in Data Plane",
        "Millisecond speed in Control Plane"
    ])
    
    create_comparison_slide(prs, "2.2.1.2 Network Models: Datagram vs Virtual Circuit", "M2.2.1 DATAGRAM VS VC",
        "Datagram Networks (Internet IP)", [
            ("Connection Setup", "No connection setup phase; packets injected immediately"),
            ("Addressing", "Packets carry full global 32-bit/128-bit Source and Destination IP"),
            ("Routing Path", "Each packet routed independently; successive packets may follow different paths"),
            ("Router State", "Stateless routers; failure of a link triggers automatic rerouting"),
            ("Complexity", "Pushed to network edge end hosts")
        ],
        "Virtual Circuit Networks (ATM / Frame Relay)", [
            ("Connection Setup", "Mandatory end-to-end signaling setup before data transfer"),
            ("Addressing", "Packets carry small local Virtual Circuit Identifier (VCI)"),
            ("Routing Path", "All packets in a connection follow the exact same fixed virtual path"),
            ("Router State", "Routers maintain per-connection state tables; link failure drops VC"),
            ("Complexity", "Heavy complexity in network core switches")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M2.2.1", "Network Layer Architecture", "K2 Understand",
        [
            "Differentiate between the Data Plane and Control Plane of the Network Layer. (6 Marks)",
            "Compare Datagram networks and Virtual Circuit networks with respect to connection setup, addressing, and router state. (8 Marks)",
            "Describe the internal architecture of a modern high-speed router (Input Ports, Switching Fabric, Output Ports). (7 Marks)"
        ],
        [
            "Forwarding is local and hardware-based; Routing is global and software-based.",
            "Internet uses datagram packet switching with stateless routers for maximum resilience.",
            "Crossbar switching fabrics eliminate internal shared bus contention in high-speed routers."
        ]
    )
    return prs

def build_m2_2_2(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.2", "IPv4 Addressing, Subnetting, CIDR & NAT",
        "IPv4 20-60 Byte Header, Fragmentation & Reassembly, Classless Addressing (CIDR), Subnet Design, NAT/PAT, ICMP Protocol",
        "Module 2"
    )
    
    create_content_slide(prs, "2.2.2.1 IPv4 Header Format & Fragmentation", "M2.2.2 IPV4 HEADER", [
        ("IPv4 Header Structure (20 to 60 Bytes)", "Version (4b: 4) | IHL (4b: Header length in 32-bit words, min 5 = 20B) | DSCP/ECN (8b: QoS) | Total Length (16b: Header + Payload, max 65535B) \\n Identification (16b) | Flags (3b: Reserved, DF, MF) | Fragment Offset (13b: measured in 8-byte units) \\n TTL (8b: Time-to-Live, decremented per hop) | Protocol (8b: ICMP=1, TCP=6, UDP=17) | Header Checksum (16b) \\n Source IP (32b) \\n Destination IP (32b) \\n Options (0-40B)."),
        ("Fragmentation Fields", "**Identification**: Identifies fragments belonging to same original datagram. **DF (Don't Fragment)**: If set to 1, router drops packet if larger than MTU. **MF (More Fragments)**: 1 for all fragments except the final one (0). **Fragment Offset**: Byte offset divided by 8."),
        ("Reassembly", "Occurs strictly at the final destination host before delivering to the transport layer.")
    ], "Key Header Fields", [
        "IHL: Header words (x4 bytes)",
        "Total Length: Max 65,535 B",
        "TTL: Prevents routing loops",
        "Protocol: 6=TCP, 17=UDP, 1=ICMP",
        "Offset unit = 8 Bytes"
    ])
    
    create_numerical_slide(
        prs, "2.2.2.2 Worked KTU Numerical: IPv4 Fragmentation", "M2.2.2 FRAGMENTATION PROBLEM",
        "An IPv4 datagram with Total Length = 4000 bytes (20-byte IP header + 3980 bytes payload) arrives at a router whose outgoing link has Maximum Transmission Unit MTU = 1500 bytes. Calculate the Total Length, Payload Length, MF flag, and Fragment Offset for all resulting fragments.",
        [
            "MTU = 1500 bytes (Max payload per fragment = 1500 - 20 = 1480 bytes).",
            "1480 is divisible by 8 (1480 / 8 = 185) -> Valid maximum payload per fragment.",
            "Total payload to fragment = 3980 bytes.",
            "Fragment Offset = Total previous payload bytes divided by 8."
        ],
        [
            (1, "Frag 1: Header = 20 B, Payload = 1480 B, Total Length = 1500 B, MF = 1, Offset = 0 / 8 = 0"),
            (2, "Frag 2: Header = 20 B, Payload = 1480 B, Total Length = 1500 B, MF = 1, Offset = 1480 / 8 = 185"),
            (3, "Remaining payload = 3980 - 1480 - 1480 = 1020 B."),
            (4, "Frag 3: Header = 20 B, Payload = 1020 B, Total Length = 1040 B, MF = 0 (last fragment!), Offset = 2960 / 8 = 370")
        ],
        "Frag 1: Len 1500, MF=1, Off=0 | Frag 2: Len 1500, MF=1, Off=185 | Frag 3: Len 1040, MF=0, Off=370",
        "Always verify that Fragment Offset values are integer multiples of 8 bytes!"
    )
    
    create_numerical_slide(
        prs, "2.2.2.3 Worked KTU Numerical: CIDR Subnetting", "M2.2.2 SUBNETTING PROBLEM",
        "An organization is allocated the block `200.50.16.0/24`. Design 4 equal-sized subnets. For each subnet, specify: (a) Subnet Mask, (b) Network Address, (c) Usable Host Range, (d) Direct Broadcast Address, (e) Maximum usable hosts.",
        [
            "Given /24 network: 8 host bits (256 addresses).",
            "To create 4 subnets: Need 2 subnet bits (2^2 = 4). New prefix = /24 + 2 = /26.",
            "Block size per subnet = 256 / 4 = 64 addresses.",
            "Usable hosts per subnet = 2^(32 - 26) - 2 = 64 - 2 = 62 hosts."
        ],
        [
            (1, "Subnet Mask: 255.255.255.192 (/26)"),
            (2, "Subnet 1: Net = 200.50.16.0/26 | Hosts = 200.50.16.1 to 200.50.16.62 | Broadcast = 200.50.16.63"),
            (3, "Subnet 2: Net = 200.50.16.64/26 | Hosts = 200.50.16.65 to 200.50.16.126 | Broadcast = 200.50.16.127"),
            (4, "Subnet 3: Net = 200.50.16.128/26 | Hosts = 200.50.16.129 to 200.50.16.190 | Broadcast = 200.50.16.191"),
            (5, "Subnet 4: Net = 200.50.16.192/26 | Hosts = 200.50.16.193 to 200.50.16.254 | Broadcast = 200.50.16.255")
        ],
        "4 Subnets of /26 mask (255.255.255.192), each accommodating 62 usable hosts",
        "First address is Network ID; Last address is Directed Broadcast; both cannot be assigned to hosts."
    )
    
    create_exam_booster_slide(
        prs, "M2.2.2", "IPv4, CIDR & NAT", "K3 Apply",
        [
            "Draw the complete IPv4 header format and explain all fields with numerical significance. (8 Marks)",
            "Explain the working of Network Address Translation (NAT) and Port Address Translation (PAT) with translation table examples. (7 Marks)",
            "What is ICMP? Explain its role in error reporting (Destination Unreachable, Time Exceeded) and diagnostic tools (`ping`, `traceroute`). (6 Marks)"
        ],
        [
            "IPv4 fragmentation uses ID, Flags (DF, MF), and Offset in 8-byte blocks.",
            "CIDR replaces classful boundaries with arbitrary prefix lengths (/N) and Longest Prefix Matching.",
            "NAT allows private IP subnets (RFC 1918) to share a single public IP using port mapping tables."
        ]
    )
    return prs

def build_m2_2_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.3", "Unicast Routing Protocols & Algorithms",
        "Link-State Routing & Dijkstra's Algorithm, Distance-Vector & Bellman-Ford, Count-to-Infinity, RIP, OSPF & BGP-4",
        "Module 2"
    )
    
    create_comparison_slide(prs, "2.2.3.1 Link-State (LS) vs Distance-Vector (DV) Algorithms", "M2.2.3 LS VS DV ROUTING",
        "Link-State (LS) Routing (e.g., OSPF)", [
            ("Global Topology Knowledge", "Every router floods link-state advertisements (LSAs); all nodes possess full network topology graph"),
            ("Algorithm", "Dijkstra's Shortest Path Algorithm run locally on each router"),
            ("Convergence Speed", "Ultra-fast convergence; zero routing loops"),
            ("Message Overhead", "$O(N \\cdot E)$ messages flooded periodically"),
            ("Complexity", "$O(V^2)$ or $O(E \\log V)$ computation per router")
        ],
        "Distance-Vector (DV) Routing (e.g., RIP)", [
            ("Local Knowledge Only", "Routers only know cost to immediate direct neighbors; exchange vectors periodically"),
            ("Algorithm", "Distributed Bellman-Ford equation: $d_x(y) = \\min_v \\{c(x,v) + d_v(y)\\}$"),
            ("Convergence Speed", "Slow convergence; susceptible to Count-to-Infinity problem"),
            ("Mitigation", "Split Horizon and Poisoned Reverse rules"),
            ("Simplicity", "Lightweight computation; suitable for small networks")
        ]
    )
    
    create_content_slide(prs, "2.2.3.2 Internet Routing Protocols: RIP vs OSPF vs BGP-4", "M2.2.3 PROTOCOL COMPARISON", [
        ("RIP (Routing Information Protocol - RFC 2453)", "Intra-AS Distance Vector protocol. Uses Hop Count metric (max 15 hops; 16 = infinity). Updates broadcast every 30s over UDP port 520."),
        ("OSPF (Open Shortest Path First - RFC 2328)", "Intra-AS Link State protocol. Uses link cost based on inverse bandwidth. Hierarchical design with Area 0 (Backbone Area) and non-backbone areas. Runs directly over IP protocol 89. Supports authenticated LSA flooding and ECMP (Equal-Cost Multi-Path)."),
        ("BGP-4 (Border Gateway Protocol - RFC 4271)", "Inter-AS Path Vector protocol glueing the global Internet together. Operates over reliable TCP port 179. Advertises AS-PATH attributes to prevent loops and enforces policy-based business routing between Autonomous Systems (eBGP and iBGP).")
    ], "Protocol Matrix", [
        "RIP: DV, Hop count (Max 15), UDP 520",
        "OSPF: LS, Dijkstra, IP 89, Areas",
        "BGP: Path Vector, AS-PATH, TCP 179",
        "Intra-AS: RIP, OSPF",
        "Inter-AS: BGP-4"
    ])
    
    create_exam_booster_slide(
        prs, "M2.2.3", "Unicast Routing Protocols", "K3 Apply",
        [
            "Explain Dijkstra's shortest path algorithm with a step-by-step table derivation for a 5-node network graph. (9 Marks)",
            "What is the Count-to-Infinity problem in Distance Vector routing? Explain how Split Horizon and Poisoned Reverse mitigate it. (8 Marks)",
            "Compare RIP, OSPF, and BGP-4 with respect to routing algorithm, metric, transport protocol, and scalability. (8 Marks)"
        ],
        [
            "Dijkstra computes shortest path trees using complete topological knowledge.",
            "Distance vector iterates Bellman-Ford equations among adjacent neighbors.",
            "OSPF structures networks into areas with Area 0 backbone to scale within large enterprises.",
            "BGP-4 implements policy routing and loop prevention across Autonomous Systems using AS-PATH."
        ]
    )
    return prs

def build_m2_2_4(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.4", "Multicast Routing Protocols & IGMP",
        "Multicast Addressing (Class D), IGMP Host-Router Membership, Source-Based Trees vs Group-Shared Trees, RPF, PIM-DM vs PIM-SM",
        "Module 2"
    )
    
    create_content_slide(prs, "2.2.4.1 Multicast Fundamentals & IGMP Protocol", "M2.2.4 MULTICAST BASICS", [
        ("Multicast Concept", "Delivering a single stream of datagrams from one or more sources to a specific group of interested receivers simultaneously without duplicate packet transmission on shared links."),
        ("Multicast Addressing", "IPv4 Class D range `224.0.0.0` to `239.255.255.255`. Special groups: `224.0.0.1` (All systems on subnet), `224.0.0.2` (All routers)."),
        ("IGMP (Internet Group Management Protocol - RFC 3376)", "Operates locally between end hosts and their attached first-hop multicast router. Hosts send IGMP Membership Reports; router sends periodic Membership Queries."),
        ("Multicast Routing Trees", "1. **Source-Based Tree (Shortest Path Tree)**: Builds a separate tree rooted at each sender source (used in DVMRP, PIM-DM). 2. **Group-Shared Tree (Core-Based Tree)**: All sources transmit to a shared Rendezvous Point (RP) / Core router (used in PIM-SM)."),
        ("Reverse Path Forwarding (RPF)", "Loop-prevention rule: Router accepts a multicast packet only if it arrived on the interface that is the shortest path back to the sender source.")
    ], "Key Mechanisms", [
        "Class D: 224.0.0.0/4",
        "IGMP: Local group membership",
        "Source Tree: Optimal delay per source",
        "Shared Tree: Minimal router state",
        "RPF: Prevents multicast loops"
    ])
    
    create_comparison_slide(prs, "2.2.4.2 PIM Protocols: Dense Mode (PIM-DM) vs Sparse Mode (PIM-SM)", "M2.2.4 PIM DENSE VS SPARSE",
        "PIM Dense Mode (PIM-DM / Flood & Prune)", [
            ("Assumed Environment", "Receivers densely populated across almost every subnet"),
            ("Tree Construction", "Source-Based Shortest Path Trees"),
            ("Mechanics", "1. **Flood**: Broadcasts multicast traffic everywhere \\n 2. **Prune**: Routers with no interested members send Prune messages back upstream \\n 3. **Graft**: New receivers send Graft to re-attach"),
            ("Overhead", "High periodic flooding overhead")
        ],
        "PIM Sparse Mode (PIM-SM / Explicit Join)", [
            ("Assumed Environment", "Receivers sparsely distributed across wide area WAN"),
            ("Tree Construction", "Group-Shared Tree rooted at Rendezvous Point (RP)"),
            ("Mechanics", "1. Receivers send explicit `IGMP Join` -> Router sends `PIM Join` towards RP \\n 2. Sources register with RP \\n 3. Traffic flows down shared tree"),
            ("Overhead", "Zero flooding; highly scalable for enterprise IPTV")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M2.2.4", "Multicast Routing", "K2 Understand",
        [
            "Explain the role of IGMP in managing multicast group memberships on local subnets. (6 Marks)",
            "Compare Source-Based Trees and Group-Shared Trees in multicast routing. (7 Marks)",
            "Explain the working of PIM-DM (Flood and Prune) versus PIM-SM (Rendezvous Point and Explicit Joins). (8 Marks)"
        ],
        [
            "IGMP connects local hosts to their edge multicast router.",
            "Source-based trees minimize latency per sender; Shared trees minimize router state.",
            "RPF algorithm discards packets that do not arrive on the shortest return path to the source."
        ]
    )
    return prs

def build_m2_2_5(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.5", "Next Generation IP: IPv6 Architecture",
        "IPv6 128-Bit Addressing, 40-Byte Fixed Header, Extension Headers, IPv4 vs IPv6 Comparison, Transition Strategies (Dual Stack, Tunneling, NAT64)",
        "Module 2"
    )
    
    create_content_slide(prs, "2.2.5.1 IPv6 Addressing & 40-Byte Fixed Header", "M2.2.5 IPV6 ARCHITECTURE", [
        ("Motivation for IPv6", "Exhaustion of the 32-bit IPv4 address space ($2^{32} \\approx 4.3 \\times 10^9$ addresses). IPv6 provides $2^{128} \\approx 3.4 \\times 10^{38}$ unique addresses."),
        ("IPv6 Address Notation", "8 groups of 4 hexadecimal digits separated by colons (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`). Leading zeros omitted (`2001:db8:85a3::8a2e:370:7334`); `::` compresses consecutive zero blocks once."),
        ("40-Byte Fixed Header Format", "Version (4b: 6) | Traffic Class (8b: QoS DSCP) | Flow Label (20b: identifies packet flow for non-default routing) \\n Payload Length (16b: data + extension headers) | Next Header (8b: specifies upper layer or extension header) | Hop Limit (8b: decremented per hop, replaces TTL) \\n Source IPv6 Address (128 bits / 16 bytes) \\n Destination IPv6 Address (128 bits / 16 bytes)."),
        ("Key Structural Improvements", "No header checksum (speeds up router processing), no in-network fragmentation (handled via Path MTU Discovery by end hosts), fixed 40-byte base size.")
    ], "Header Breakdown", [
        "Fixed Header: Exactly 40 Bytes",
        "Source IP: 128 bits (16 B)",
        "Destination IP: 128 bits (16 B)",
        "Hop Limit: Replaces TTL",
        "Next Header: Chains extensions",
        "Flow Label: 20-bit stream tagging"
    ])
    
    create_comparison_slide(prs, "2.2.5.2 IPv4 vs IPv6 & Transition Strategies", "M2.2.5 IPV4 VS IPV6",
        "IPv4 vs IPv6 Header Comparison", [
            ("Address Size", "IPv4: 32 bits (4 Bytes) vs IPv6: 128 bits (16 Bytes)"),
            ("Header Length", "IPv4: Variable 20-60B (IHL field) vs IPv6: Fixed 40 Bytes"),
            ("Checksum", "IPv4: 16-bit header checksum vs IPv6: Removed entirely"),
            ("Fragmentation", "IPv4: Routers fragment packets vs IPv6: End systems only (PMTUD)"),
            ("Broadcast", "IPv4: Broadcast supported vs IPv6: Replaced by Multicast & Anycast")
        ],
        "IPv4 to IPv6 Migration Mechanisms", [
            ("Dual Stack", "Nodes run both IPv4 and IPv6 protocol stacks simultaneously on all interfaces"),
            ("Tunneling (6to4 / Teredo)", "IPv6 datagrams encapsulated as payload inside IPv4 packets across legacy IPv4 transit networks"),
            ("Header Translation (NAT64/DNS64)", "Translates IPv6 packet headers directly to IPv4 headers for legacy server interoperation")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M2.2.5", "IPv6 Architecture", "K2 Understand",
        [
            "Draw the IPv6 fixed header format and explain all fields. How does it improve router forwarding performance over IPv4? (8 Marks)",
            "Compare IPv4 and IPv6 across addressing, header structure, fragmentation, and error checking. (8 Marks)",
            "Explain the three transition mechanisms from IPv4 to IPv6: Dual Stack, Tunneling, and NAT64. (7 Marks)"
        ],
        [
            "IPv6 fixed 40-byte header streamlines hardware ASIC forwarding.",
            "Extension headers (Hop-by-Hop, Routing, Fragment, ESP, AH) are daisy-chained via `Next Header`.",
            "Dual stack and encapsulation tunneling enable smooth evolutionary migration from IPv4."
        ]
    )
    return prs

def build_m2_2_6(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.2.6", "Quality of Service (QoS) & Traffic Shaping",
        "QoS Metrics (Delay, Jitter, Loss), Traffic Policing vs Shaping, Leaky Bucket vs Token Bucket, Scheduling (FIFO, WFQ), DiffServ vs IntServ",
        "Module 2"
    )
    
    create_comparison_slide(prs, "2.2.6.1 Traffic Shaping: Leaky Bucket vs Token Bucket", "M2.2.6 TRAFFIC SHAPING",
        "Leaky Bucket Algorithm (Constant Output)", [
            ("Concept", "A bucket with a hole at the bottom; incoming packets buffer up to bucket capacity $C$ and leak out at a strictly constant rate $\\rho$"),
            ("Output Profile", "Strictly constant, smooth output stream regardless of incoming burstiness"),
            ("Burst Handling", "Eliminates bursts entirely; discards packets if bucket overflows"),
            ("Suitability", "Constant Bit Rate (CBR) traffic like uncompressed voice")
        ],
        "Token Bucket Algorithm (Burst-Tolerant)", [
            ("Concept", "Tokens generate at rate $r$ tokens/sec up to max token capacity $b$. A packet of size $m$ bytes consumes $m$ tokens to transmit"),
            ("Output Profile", "Allows short-term traffic bursts up to bucket size $b$ while enforcing average long-term rate $r$"),
            ("Burst Handling", "Max burst transmission speed = link wire rate $R$ for duration $T = b / (R - r)$"),
            ("Suitability", "Variable Bit Rate (VBR) video streaming and web traffic")
        ]
    )
    
    create_numerical_slide(
        prs, "2.2.6.2 Worked KTU Numerical: Token Bucket Burst Calculation", "M2.2.6 TOKEN BUCKET NUMERICAL",
        "A token bucket has token arrival rate r = 2 MB/sec and token bucket capacity b = 16 MB. The transmission link wire rate is R = 10 MB/sec. Calculate: (a) Maximum burst duration at wire rate R, (b) Maximum total data transmitted during this burst period.",
        [
            "Burst duration formula: T = b / (R - r)",
            "Where b = bucket size (MB), R = peak transmission rate (MB/s), r = token replenishment rate (MB/s).",
            "Total data transmitted during burst: D = R * T = (b * R) / (R - r)."
        ],
        [
            (1, "b = 16 MB, R = 10 MB/s, r = 2 MB/s"),
            (2, "T = 16 / (10 - 2) = 16 / 8 = 2.0 seconds"),
            (3, "Total data transmitted = R * T = 10 MB/s * 2.0 s = 20 MB"),
            (4, "Verification: Initial tokens (16 MB) + Newly generated tokens in 2s (2 MB/s * 2s = 4 MB) = 20 MB.")
        ],
        "Max Burst Duration T = 2.0 seconds | Total Burst Data = 20 MB",
        "After 2 seconds, the transmission rate drops strictly to the average token rate r = 2 MB/sec."
    )
    
    create_exam_booster_slide(
        prs, "M2.2.6", "Quality of Service (QoS)", "K3 Apply",
        [
            "Differentiate between Traffic Policing and Traffic Shaping with neat diagrams. (6 Marks)",
            "Compare Leaky Bucket and Token Bucket traffic shaping algorithms with equations and operating principles. (8 Marks)",
            "Explain Differentiated Services (DiffServ) architecture: Packet Classification, DSCP marking, and Per-Hop Behaviors (EF & AF). (7 Marks)"
        ],
        [
            "Leaky bucket produces rigid constant output; Token bucket permits regulated bursts.",
            "Weighted Fair Queuing (WFQ) guarantees minimum bandwidth shares to different service classes.",
            "DiffServ scales across WANs by classifying packets at boundary routers and using 6-bit DSCP markings."
        ]
    )
    return prs

def build_m2_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M2.3", "Linux Kernel TCP/IP Stack & Routing Implementation",
        "Linux Network Packet Flow, sk_buff Data Structure, net_device, Forwarding Information Base (FIB), Route Cache, Linux iproute2",
        "Module 2"
    )
    
    create_content_slide(prs, "2.3.1 Linux Kernel Network Subsystem Architecture", "M2.3 LINUX KERNEL STACK", [
        ("The `sk_buff` (Socket Buffer) Structure", "The universal data structure representing network packets in Linux. Contains pointers: `head`, `data`, `tail`, `end`. Allows zero-copy header prepending/stripping across layers simply by moving the `data` pointer."),
        ("Packet Ingress Flow (RX)", "NIC receives frame -> DMA transfer to Ring Buffer -> Triggers Hard IRQ -> NAPI poll scheduled (SoftIRQ `NET_RX_SOFTIRQ`) -> `netif_receive_skb()` -> L3 `ip_rcv()` -> L4 `tcp_v4_rcv()` -> Socket receive queue -> `read()`."),
        ("Packet Egress Flow (TX)", "App calls `write()` -> L4 `tcp_sendmsg()` creates `sk_buff` -> L3 `ip_queue_xmit()` routes packet -> L2 `dev_queue_xmit()` enqueues to `qdisc` -> NIC DMA transmit -> Hardware TX IRQ."),
        ("Forwarding Information Base (FIB)", "The core kernel routing table in Linux organized as a fast LC-trie (Level-Compressed Trie) supporting sub-microsecond Longest Prefix Matching."),
        ("Policy-Based Routing (PBR)", "Linux supports multiple routing tables selected via `ip rule` based on source IP, TOS, fwmark, or incoming interface.")
    ], "Kernel Data Structures", [
        "sk_buff: Packet descriptor",
        "net_device: Hardware NIC abstraction",
        "FIB: Kernel routing table trie",
        "qdisc: Traffic queuing discipline",
        "NAPI: Interrupt mitigation polling"
    ])
    
    code_iproute_example = """# Linux iproute2 Advanced Routing Commands

# 1. Inspect kernel routing table
ip route show

# 2. Add static route via gateway
ip route add 192.168.10.0/24 via 10.0.0.1 dev eth0

# 3. Create Policy-Based Routing (PBR) table
echo "200 custom_table" >> /etc/iproute2/rt_tables
ip rule add from 192.168.1.50 table custom_table
ip route add default via 10.0.0.254 dev eth1 table custom_table

# 4. Flush and inspect route cache
ip route flush cache"""
    create_code_slide(
        prs, "2.3.2 Hands-On: Linux Kernel Routing with `iproute2`", "M2.3 LINUX IPROUTE2",
        code_iproute_example,
        [
            ("`ip route` Suite", "Replaces deprecated `route` and `ifconfig` tools with direct Netlink socket communication to kernel."),
            ("Custom Routing Tables", "Linux supports up to 255 independent routing tables for multi-homing and ISP failover."),
            ("`ip rule` Subsystem", "Evaluates routing policy database (RPDB) rules sequentially to select appropriate routing table."),
            ("Route Cache Behavior", "Historical kernels maintained route hash cache; modern kernels use ultra-fast lockless FIB trie lookups.")
        ],
        "Kernel `sk_buff` zero-copy architecture allows Linux to process millions of packets per second per CPU core."
    )
    
    create_exam_booster_slide(
        prs, "M2.3", "Linux Kernel Routing Stack", "K3 Apply",
        [
            "Explain the architecture and role of the `sk_buff` data structure in Linux packet processing. (7 Marks)",
            "Trace the step-by-step path of an incoming packet from physical NIC reception to application socket delivery in the Linux kernel. (8 Marks)",
            "Demonstrate Policy-Based Routing (PBR) in Linux using `ip rule` and `ip route` commands. (6 Marks)"
        ],
        [
            "`sk_buff` avoids costly memory copies across protocol layers using internal buffer pointers.",
            "NAPI SoftIRQs prevent interrupt livelock during heavy packet bursts.",
            "FIB LC-trie enables sub-microsecond Longest Prefix Matching across hundreds of thousands of BGP routes."
        ]
    )
    return prs

def build_module_2_master(prs=None):
    """Builds the comprehensive master deck combining all Module 2 topics."""
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "MODULE 2 MASTER DECK", "Transport & Network Layer Architecture",
        "Complete Lecture Slides for KTU PCCST501 Computer Networks | Topics M2.1.1 through M2.3",
        "Module 2 Master"
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
