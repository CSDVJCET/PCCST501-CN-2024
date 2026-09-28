# PCCSL507 Network Lab — Complete Hands-On Lab Manual

**Course Code:** PCCSL507 / PCCST501 Hands-On Networking  
**Department:** Computer Science and Engineering  
**Institution:** Viswajyothi College of Engineering and Technology (VJCET)  
**Faculty In-Charge:** Prof. Anju Markose, Assistant Professor, Dept. of CSE  

---

## Experiment 1: Linux Networking CLI Commands & Configuration

### Objective
To become proficient with core Linux CLI utilities for network interface configuration, routing inspection, socket monitoring, and packet tracing.

### Commands & Practical Usage
1. **Interface Information & IP Configuration:**
   ```bash
   # View all network interfaces with IPv4/IPv6 addresses
   ip addr show
   # Bring interface up or down
   sudo ip link set eth0 up
   sudo ip link set eth0 down
   # Assign a static IP address
   sudo ip addr add 192.168.1.100/24 dev eth0
   ```
2. **Routing Table Inspection:**
   ```bash
   # View kernel routing table
   ip route show
   # Add a new static route
   sudo ip route add 10.10.0.0/16 via 192.168.1.1 dev eth0
   ```
3. **Socket Statistics & Active Port Inspection:**
   ```bash
   # List all listening TCP and UDP sockets with process IDs
   ss -tulnp
   # Traditional netstat alternative
   netstat -tuln
   ```
4. **Network Diagnostic Utilities:**
   ```bash
   # Test ICMP end-to-end reachability
   ping -c 4 google.com
   # Trace layer-3 routing hops to destination
   traceroute -n 8.8.8.8
   # View and clear ARP cache
   ip neigh show
   sudo ip neigh flush all
   ```

---

## Experiment 2: Client-Server Socket Programming (TCP & UDP)

### Objective
Implement elementary client-server communication using Berkeley Sockets API in C and Python.

### System Calls Flow (TCP)
- **Server:** `socket()` $\rightarrow$ `bind()` $\rightarrow$ `listen()` $\rightarrow$ `accept()` $\rightarrow$ `read()` / `write()` $\rightarrow$ `close()`
- **Client:** `socket()` $\rightarrow$ `connect()` $\rightarrow$ `write()` / `read()` $\rightarrow$ `close()`

### Code Reference
Refer to source files in `assets/handson_code/module2/`:
- `tcp_echo_server.c` & `tcp_echo_client.c`
- `ip_subnet_calculator.py`

---

## Experiment 3: I/O Multiplexing using `select()` and `poll()`

### Objective
Implement a single-threaded server capable of handling multiple concurrent client connections simultaneously without blocking.

### Stevens Reference (UNP Vol 1 Ch 6)
- `fd_set` macros: `FD_ZERO(&set)`, `FD_SET(fd, &set)`, `FD_CLR(fd, &set)`, `FD_ISSET(fd, &set)`.
- Code prototype and implementation: `assets/handson_code/module2/io_multiplexing_select.c`.

---

## Experiment 4: Wireshark Packet Capture & Protocol Analysis

### Objective
Capture live network packets and analyze protocol headers for HTTP, DNS, TCP 3-Way Handshake, and ARP.

### Step-by-Step Lab Procedure
1. Launch Wireshark as administrator / root and select active interface (e.g., `eth0` or `Wi-Fi`).
2. Set display filter: `tcp.flags.syn == 1 or http or dns or arp`.
3. Open a browser and navigate to `http://neverssl.com`.
4. Stop packet capture and examine:
   - **TCP 3-Way Handshake:** Filter `tcp.port == 80`. Note SYN (`Seq=0`), SYN-ACK (`Seq=0, Ack=1`), ACK (`Seq=1, Ack=1`).
   - **HTTP Request:** Note Request Method (`GET`), URI, User-Agent, Host header.
   - **HTTP Response:** Note Status Code (`200 OK` or `301 Moved`), Content-Type, Content-Length.
   - **DNS Query/Response:** Filter `dns`. Examine Question section (Query name, Type A) and Answer section (TTL, Resolved IP).

---

## Experiment 5: Cisco Packet Tracer Network Topology & Subnetting

### Objective
Design and simulate an enterprise network topology in Cisco Packet Tracer with multiple departmental subnets, default gateways, and inter-VLAN routing.

### Topology Specifications
- **Router 1841:** Gateway for Subnet A (`192.168.1.0/26`) and Subnet B (`192.168.1.64/26`).
- **Switch 2960:** Connected to 4 PCs per subnet.
- **Router CLI Commands:**
  ```cisco
  Router> enable
  Router# configure terminal
  Router(config)# interface FastEthernet0/0
  Router(config-if)# ip address 192.168.1.1 255.255.255.192
  Router(config-if)# no shutdown
  Router(config-if)# exit
  Router(config)# interface FastEthernet0/1
  Router(config-if)# ip address 192.168.1.65 255.255.255.192
  Router(config-if)# no shutdown
  ```

---

## Experiment 6: Datalink Provider Interface & Raw Sockets (`PF_PACKET`)

### Objective
Capture raw Layer-2 Ethernet frames directly from the network interface using Linux `PF_PACKET` raw sockets (UNP Chapter 29).

### Execution Instructions
```bash
gcc assets/handson_code/module3/raw_socket_packet_sniffer.c -o sniffer
sudo ./sniffer
```
Examine the decoded 14-byte Ethernet header (Destination MAC, Source MAC, EtherType: `0x0800` for IPv4, `0x0806` for ARP) and IP payload.

---

## Experiment 7: Error Detection & Correction (CRC & Hamming Code)

### Objective
Implement Cyclic Redundancy Check (CRC-CCITT) and Hamming (7,4) single-bit error detection and correction algorithms in Python.

### Execution Instructions
```bash
python assets/handson_code/module3/crc_error_detector.py
python assets/handson_code/module3/hamming_code_7_4.py
```
Demonstrate that inverted bits during transit generate a non-zero remainder in CRC and an exact syndrome bit position in Hamming code.
