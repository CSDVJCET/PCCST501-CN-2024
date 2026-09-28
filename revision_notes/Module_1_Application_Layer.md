# PCCST501 Computer Networks — Module 1 Revision Notes

**Course:** PCCST501 Computer Networks (Semester 5 B.Tech CSE)  
**Institution:** Viswajyothi College of Engineering and Technology (VJCET)  
**Faculty:** Prof. Anju Markose, Assistant Professor, Dept. of CSE  
**Prescribed Textbooks:**  
- Behrouz A. Forouzan, *Computer Networks: A Top-Down Approach*, McGraw Hill, SIE 2017 (Ch 1 & Ch 2)  
- J. F. Kurose and K. W. Ross, *Computer Networking: A Top-Down Approach Featuring Internet*, Pearson 8/e  

---

## 1. Overview of the Internet & Protocol Layering

### 1.1 The Internet Architecture
The Internet is a globally interconnected network of networks consisting of:
- **Network Edge (Hosts/End Systems):** Clients, servers, IoT devices running network applications.
- **Network Core:** Interconnected routers and switches that forward packets through packet switching.
- **Access Networks & Physical Media:** Fiber optic cables, coaxial cable, twisted pair copper, 4G/5G, and Wi-Fi.

### 1.2 Protocol Layering (OSI 7-Layer vs. TCP/IP 5-Layer Stack)
Protocol layering divides complex communication tasks into modular, manageable layers where each layer offers specific services to the layer above while relying on the layer below.

| TCP/IP Layer | Primary Protocol Data Unit (PDU) | Core Responsibilities & Functions | Key Protocols |
| :--- | :--- | :--- | :--- |
| **5. Application** | **Message** | User interface, application logic, high-level message exchange | HTTP, HTTPS, DNS, SMTP, FTP, SSH, BitTorrent |
| **4. Transport** | **Segment (TCP) / Datagram (UDP)** | Process-to-process communication, port multiplexing, reliability, flow/congestion control | TCP, UDP, SCTP |
| **3. Network** | **Datagram / Packet** | Host-to-host delivery, logical IP addressing, unicast/multicast routing | IPv4, IPv6, ICMP, OSPF, BGP, RIP |
| **2. Data Link** | **Frame** | Node-to-node (hop-by-hop) frame transfer, physical MAC addressing, media access control | IEEE 802.3 Ethernet, IEEE 802.11 Wi-Fi, PPP |
| **1. Physical** | **Bits** | Transmission of raw bit streams over physical media, line coding, signal modulation | UTP Cat 6, Optical Fiber, Microwave, Radio |

### 1.3 Encapsulation & Decapsulation
- **Encapsulation (Sender side):** At each layer from top to bottom, a header (and trailer at Layer 2) containing protocol control information is prepended to the payload data.
- **Decapsulation (Receiver side):** The reverse process where each layer strips off its corresponding header and passes the payload upward.

---

## 2. Application-Layer Paradigms

### 2.1 Client-Server Paradigm
- **Centralized Architecture:** A dedicated server with a fixed, well-known IP address is always active listening on a well-known port.
- **Clients:** Transiently connected devices that initiate requests to the server. Clients do not communicate directly with each other.
- **Bottlenecks:** Single point of failure, scalability limits under heavy traffic loads requiring server farm load balancing.

### 2.2 Peer-to-Peer (P2P) Paradigm
- **Decentralized Architecture:** Arbitrary end systems (peers) communicate directly with each other without relying on a centralized server.
- **Self-Scalability:** Each peer contributes upload bandwidth as it downloads files (e.g., BitTorrent, Blockchain).

---

## 3. Core Client-Server Applications

### 3.1 World Wide Web & HTTP (HyperText Transfer Protocol)
- **Port:** TCP Port 80 (HTTP) / Port 443 (HTTPS with TLS/SSL).
- **Stateless Nature:** The HTTP server maintains no session state about client requests. Cookies and local storage maintain application state.
- **Persistent vs. Non-Persistent HTTP:**
  - **Non-Persistent HTTP (HTTP/1.0):** Opens a new TCP connection for every single referenced object. Overhead: $2 \times RTT + \text{Transmission Time}$ per object.
  - **Persistent HTTP (HTTP/1.1):** Reuses a single TCP connection for multiple object transfers. Supports pipelining.
  - **HTTP/2 & HTTP/3:** Multiplexing multiple requests over a single connection using binary framing (HTTP/2) and QUIC over UDP (HTTP/3).
- **HTTP Request Methods:** `GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`.
- **HTTP Status Code Categories:**
  - `1xx`: Informational (e.g., `100 Continue`)
  - `2xx`: Success (e.g., `200 OK`, `201 Created`)
  - `3xx`: Redirection (e.g., `301 Moved Permanently`, `304 Not Modified`)
  - `4xx`: Client Error (e.g., `400 Bad Request`, `403 Forbidden`, `404 Not Found`)
  - `5xx`: Server Error (e.g., `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`)

### 3.2 File Transfer Protocol (FTP)
- **Out-of-Band Control:** Uses two separate TCP connections:
  1. **Control Connection (TCP Port 21):** Carries authentication, directory navigation, and commands. Remains open throughout the session.
  2. **Data Connection (TCP Port 20):** Dynamically opened and closed for every file transfer / directory listing.

### 3.3 Electronic Mail (SMTP, POP3, IMAP)
- **SMTP (Simple Mail Transfer Protocol - TCP Port 25 / 587):** Push protocol used by Mail User Agents (MUA) to submit email to Mail Transfer Agents (MTA) and between MTAs. Restricts body text to 7-bit ASCII (extended by MIME).
- **MIME (Multipurpose Internet Mail Extensions):** Extends SMTP to support non-ASCII text, attachments, audio, video, and multipart payloads.
- **Mail Access Protocols (Pull Protocols):**
  - **POP3 (Post Office Protocol v3 - TCP Port 110 / 995):** Downloads messages to client and deletes them from server (or leaves copies); offline access.
  - **IMAP (Internet Message Access Protocol - TCP Port 143 / 993):** Maintains mailboxes and folders on the remote server; allows multi-device synchronization.

### 3.4 Domain Name System (DNS)
- **Port:** UDP Port 53 (standard queries) and TCP Port 53 (zone transfers and large responses $> 512$ bytes).
- **Hierarchical Namespace:**
  1. **Root DNS Servers:** 13 logical root server IP addresses (replicated worldwide via Anycast).
  2. **Top-Level Domain (TLD) Servers:** Manage `.com`, `.org`, `.edu`, `.in`, etc.
  3. **Authoritative DNS Servers:** Maintained by organizations hosting public DNS records.
  4. **Local / Recursive DNS Resolvers:** Maintained by ISPs or public resolvers (e.g., `8.8.8.8`, `1.1.1.1`).
- **Resolution Mechanisms:**
  - **Recursive Resolution:** Local DNS server queries root, TLD, and authoritative on behalf of client and returns final answer.
  - **Iterative Resolution:** Root server returns IP of TLD; local DNS queries TLD; TLD returns authoritative server IP.
- **Key DNS Resource Records (RR):**
  - `A Record`: Hostname $\rightarrow$ IPv4 Address
  - `AAAA Record`: Hostname $\rightarrow$ IPv6 Address
  - `CNAME Record`: Canonical Name (alias mapping)
  - `MX Record`: Mail Exchange Server priority and domain
  - `NS Record`: Authoritative Name Server for a zone
  - `PTR Record`: Reverse DNS (IP $\rightarrow$ Hostname)

---

## 4. Peer-to-Peer Paradigm & BitTorrent Case Study

### 4.1 BitTorrent Swarm Architecture
- **Torrent (.torrent file):** Contains metadata, piece length (typically 256 KB - 1 MB), SHA-1 cryptographic hashes of all pieces, and Tracker URL.
- **Tracker:** Centralized/distributed node that maintains the list of currently active peers in a swarm.
- **Bitfield:** Array of bits exchanged during handshake representing which pieces a peer currently possesses.
- **Seeder:** A peer that has the complete file (100%) and only uploads.
- **Leecher:** A peer currently downloading missing pieces while uploading acquired pieces.

### 4.2 Core BitTorrent Algorithms
1. **Rarest-First Piece Selection:** Peers prioritize requesting the pieces that are least common in the swarm, preventing rare pieces from disappearing if seeders leave.
2. **Tit-for-Tat Choking Algorithm:**
   - Every 10 seconds, a peer measures upload rates of all neighbors and unchokes the top 4 fastest uploaders.
   - Every 30 seconds, an **Optimistically Unchoked** peer is selected at random to discover new high-bandwidth peers and allow new leechers to bootstrap.
