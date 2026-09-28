# PCCST501 Computer Networks — Module 2 Revision Notes

**Course:** PCCST501 Computer Networks (Semester 5 B.Tech CSE)  
**Institution:** Viswajyothi College of Engineering and Technology (VJCET)  
**Faculty:** Prof. Anju Markose, Assistant Professor, Dept. of CSE  
**Prescribed Textbooks:**  
- Behrouz A. Forouzan, *Computer Networks: A Top-Down Approach*, McGraw Hill (Ch 3, Ch 4, Ch 8)  
- W. Richard Stevens, *Unix Network Programming, Volume 1: The Sockets Networking API*, Pearson 3/e (Ch 3-6, Ch 8, Ch 14)  
- Sameer Seth, M. Ajaykumar Venkatesulu, *TCP/IP Architecture, Design, and Implementation in Linux*, Wiley 1/e (Ch 14)  

---

## 1. Transport Layer Services & Protocols

### 1.1 Process-to-Process Communication & Port Numbers
- **Socket:** The combination of an IP address and a Port Number uniquely identifying a network endpoint (`IP:Port`).
- **Port Ranges:**
  - **Well-Known Ports (0 – 1023):** Managed by IANA (e.g., HTTP: 80, HTTPS: 443, DNS: 53, SSH: 22).
  - **Registered Ports (1024 – 49151):** Assigned to user processes / vendor services (e.g., MySQL: 3306).
  - **Dynamic / Ephemeral / Private Ports (49152 – 65535):** Assigned dynamically to client sockets by the OS kernel.

### 1.2 User Datagram Protocol (UDP - RFC 768)
- **Characteristics:** Connectionless, unreliable, lightweight, minimal overhead (8-byte header), no congestion control, preserves message boundaries.
- **UDP 8-Byte Header Structure:**
  - Source Port (16 bits), Destination Port (16 bits)
  - Length (16 bits, minimum 8 bytes), Checksum (16 bits, 1's complement over pseudo-header + UDP header + payload)
- **Use Cases:** Real-time multimedia (VoIP, RTP), DNS, DHCP, SNMP, online gaming.

### 1.3 Transmission Control Protocol (TCP - RFC 793 / RFC 5681)
- **Characteristics:** Connection-oriented, reliable byte-stream, point-to-point, full-duplex, flow-controlled, congestion-controlled.
- **TCP Header Structure (20 to 60 Bytes):**
  - Source Port (16 bits) & Destination Port (16 bits)
  - Sequence Number (32 bits) & Acknowledgment Number (32 bits)
  - Data Offset / Header Length (4 bits, in 32-bit 4-byte words, minimum 5 = 20 bytes)
  - Control Flags (9 bits): `URG`, `ACK`, `PSH`, `RST`, `SYN`, `FIN`, `ECE`, `CWR`, `NS`
  - Receive Window / Advertised Window (16 bits - Flow Control)
  - Checksum (16 bits) & Urgent Pointer (16 bits)
  - Options (Variable, 0–40 bytes: MSS, Window Scale, SACK, Timestamps)

### 1.4 TCP Connection Lifecycle
1. **Three-Way Handshake (Connection Establishment):**
   - Client $\rightarrow$ Server: `[SYN, Seq=x]`
   - Server $\rightarrow$ Client: `[SYN+ACK, Seq=y, Ack=x+1]`
   - Client $\rightarrow$ Server: `[ACK, Seq=x+1, Ack=y+1]`
2. **Four-Way Teardown (Connection Termination):**
   - Active Close: `[FIN, Seq=u]`, Passive Close: `[ACK, Ack=u+1]`
   - Passive Close: `[FIN, Seq=v, Ack=u+1]`, Active Close: `[ACK, Ack=v+1]`
   - `TIME_WAIT` state on active closer lasts $2 \times MSL$ (Maximum Segment Lifetime = 60-120s) to absorb delayed duplicate segments.

### 1.5 Sliding Window & Reliable Data Transfer Protocols
- **Stop-and-Wait ARQ:** Window size $= 1$. High idle time on high bandwidth-delay product networks. Efficiency $\eta = \frac{1}{1 + 2a}$, where $a = \frac{T_{prop}}{T_{trans}}$.
- **Go-Back-N (GBN) ARQ:** Sender window size $N > 1$, Receiver window size $= 1$. Cumulative ACKs. On packet loss or timeout, sender retransmits all unacknowledged packets starting from the lost packet ($N$ packets retransmitted). Max window size $N \le 2^m - 1$ for $m$-bit sequence numbers.
- **Selective Repeat (SR) ARQ:** Sender window size $N$, Receiver window size $N$. Individual ACKs. Receiver buffers out-of-order packets; sender only retransmits specific damaged or timed-out packets. Max window size $N \le 2^{m-1}$.

### 1.6 TCP Flow Control vs. Congestion Control
- **Flow Control (End-to-End):** Receiver advertises its available buffer space via the `rwnd` (Receive Window) field in the TCP header. Sender ensures $\text{FlightSize} \le \min(\text{rwnd}, \text{cwnd})$.
- **Congestion Control (Network-Wide):**
  1. **Slow Start:** `cwnd` starts at 1 MSS (or initial window) and doubles every RTT (exponential growth) until reaching `ssthresh` (Slow Start Threshold).
  2. **Congestion Avoidance (AIMD - Additive Increase Multiplicative Decrease):** `cwnd` increases linearly by 1 MSS per RTT ($\text{cwnd} = \text{cwnd} + 1/\text{cwnd}$).
  3. **Fast Retransmit & Fast Recovery (TCP Reno):**
     - Upon receiving **3 Duplicate ACKs**, TCP immediately retransmits the missing segment without waiting for RTO timeout.
     - `ssthresh` is halved ($\text{ssthresh} = \text{cwnd} / 2$), and `cwnd` is set to $\text{ssthresh} + 3\text{MSS}$ (enters Fast Recovery).
     - On timeout: `ssthresh = cwnd / 2`, and `cwnd` resets to 1 MSS (enters Slow Start).

---

## 2. UNIX Socket Programming (W. Richard Stevens)

### 2.1 Elementary Sockets API
- `int socket(int domain, int type, int protocol)`: Creates an endpoint (e.g., `AF_INET`, `SOCK_STREAM`, `0`).
- `int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen)`: Assigns a local IP and port.
- `int listen(int sockfd, int backlog)`: Converts active socket into passive listening socket with connection queue.
- `int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen)`: Extracts first connection request on the listening queue and returns a new connected socket file descriptor.
- `int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen)`: Initiates 3-way handshake with remote server.
- `ssize_t send() / recv()`, `read() / write()`: I/O operations on connected TCP streams.
- `ssize_t sendto() / recvfrom()`: Message-oriented I/O for connectionless UDP sockets.

### 2.2 I/O Multiplexing: `select()` and `poll()`
- **Problem with Blocking I/O:** A single thread blocked on `read()` cannot service other incoming clients.
- **`select()` Function:**
  ```c
  int select(int maxfdp1, fd_set *readset, fd_set *writeset, fd_set *exceptset, const struct timeval *timeout);
  ```
  - Uses bit masks (`FD_SET`, `FD_CLR`, `FD_ISSET`, `FD_ZERO`). Limited to `FD_SETSIZE` descriptors (typically 1024). Modifies descriptor sets in place.
- **`poll()` Function:**
  ```c
  int poll(struct pollfd *fdarray, unsigned long nfds, int timeout);
  ```
  - Uses an array of `struct pollfd` containing separate `events` (requested) and `revents` (returned) fields. No hardcoded descriptor limit.

---

## 3. Network Layer: Addressing & Routing

### 3.1 IPv4 Addressing & CIDR
- 32-bit logical address written in dotted-decimal format (`X.X.X.X`).
- **Classful Addressing:** Class A (`/8`), Class B (`/16`), Class C (`/24`), Class D (Multicast `224.0.0.0/4`), Class E (Reserved).
- **Classless Inter-Domain Routing (CIDR - RFC 4632):** Uses prefix length notation (`/n`).
- **Subnetting Formulas:**
  - Number of Subnets = $2^s$ (where $s$ is the number of borrowed subnet bits).
  - Usable Hosts per Subnet = $2^{32 - n} - 2$ (subtracting Network ID and Directed Broadcast ID).
- **Network Address Translation (NAT):** Translates private IP addresses (RFC 1918: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to globally routable public IPs using Port Address Translation (NAPT).

### 3.2 Unicast Routing Protocols
1. **Intra-Domain Routing (Interior Gateway Protocols - IGP):**
   - **Distance Vector (Bellman-Ford Algorithm - RIP):** Metric is Hop Count (max 15 hops, 16 = infinity). Periodic updates every 30s. Problems: Count-to-Infinity problem solved by Split Horizon and Poison Reverse.
   - **Link-State (Dijkstra SPF Algorithm - OSPF):** Each router constructs a complete topology map of the autonomous system (AS) via Link State Advertisements (LSAs) and computes shortest paths. Fast convergence, metric based on bandwidth.
2. **Inter-Domain Routing (Exterior Gateway Protocols - EGP):**
   - **Border Gateway Protocol (BGP-4):** Path-Vector protocol running over TCP Port 179. Advertises reachable CIDR prefix along with `AS-PATH` attribute to prevent routing loops and enforce policy-based routing.

### 3.3 Multicast Routing
- **Multicast Group Management:** Internet Group Management Protocol (IGMPv1, IGMPv2, IGMPv3) on IPv4, MLD on IPv6.
- **Multicast Routing Protocols:**
  - **PIM-DM (Dense Mode):** Flood-and-Prune (Source-Based Shortest Path Trees).
  - **PIM-SM (Sparse Mode):** Explicit join using Rendezvous Point (RP) Shared Trees ($\text{(*, G)}$ trees).

### 3.4 Next Generation IP (IPv6)
- **128-bit Address Space:** Written in 8 groups of 4 hexadecimal digits separated by colons (`2001:0db8:85a3::8a2e:0370:7334`). Zero compression (`::`) allowed once.
- **Fixed 40-Byte Base Header:** Eliminates checksum, removes intermediate fragmentation (Path MTU Discovery required), replaces broadcast with multicast and anycast.
- **Transition Strategies:** Dual Stack (running IPv4 & IPv6 simultaneously), Tunneling (6to4, Teredo), NAT64/DNS64.

### 3.5 Quality of Service (QoS)
- **Traffic Shaping Algorithms:**
  - **Leaky Bucket:** Regulates bursty traffic to a constant, continuous output rate (cannot handle bursts).
  - **Token Bucket:** Accumulates tokens at rate $r$ up to capacity $B$; allows bursts up to token capacity while bounding long-term average rate.
- **Packet Scheduling:** FIFO, Priority Queuing (PQ), Weighted Fair Queuing (WFQ).

---

## 4. Linux Kernel Routing Architecture (Sameer Seth & Venkatesulu)

- **FIB (Forwarding Information Base - `fib_table`):** The persistent kernel routing table organized as a radix trie (LC-trie) for longest-prefix matching.
- **Routing Cache (`rtable` / `dst_entry`):** Fast hash-table lookup for previously resolved destination IP routes.
- **Manipulating Routes using `ip` command:**
  ```bash
  # View routing table
  ip route show
  # Add static route to subnet via next-hop router
  sudo ip route add 192.168.10.0/24 via 10.0.0.1 dev eth0
  # Delete route
  sudo ip route del 192.168.10.0/24
  ```
