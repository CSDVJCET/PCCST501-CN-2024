# PCCST501 Computer Networks — Module 3 Revision Notes

**Course:** PCCST501 Computer Networks (Semester 5 B.Tech CSE)  
**Institution:** Viswajyothi College of Engineering and Technology (VJCET)  
**Faculty:** Prof. Anju Markose, Assistant Professor, Dept. of CSE  
**Prescribed Textbooks:**  
- Behrouz A. Forouzan, *Computer Networks: A Top-Down Approach*, McGraw Hill (Ch 5 & Ch 6)  
- W. Richard Stevens, *Unix Network Programming, Volume 1: The Sockets Networking API*, Pearson 3/e (Ch 29)  

---

## 1. Data Link Control (DLC)

### 1.1 Framing Techniques
- **Character-Oriented Framing (Byte Stuffing):** Uses 8-bit flag bytes (e.g., `FLAG = 0x7E`). If `FLAG` or `ESC` occurs in the payload, an `ESC` byte is inserted before it.
- **Bit-Oriented Framing (Bit Stuffing):** Uses flag pattern `01111110` (six consecutive 1s). The sender inserts a `0` bit after any sequence of five consecutive `1`s in the payload. The receiver removes any `0` that immediately follows five consecutive `1`s.

### 1.2 Error Detection & Correction Codes
1. **Cyclic Redundancy Check (CRC):**
   - Based on Modulo-2 binary polynomial arithmetic (XOR without carry).
   - Given Data Word $D(x)$ and Generator Polynomial $G(x)$ of degree $r$:
     - Append $r$ zeros to $D(x)$: $D(x) \times 2^r$.
     - Divide $(D(x) \times 2^r)$ by $G(x)$ using Modulo-2 division to obtain remainder $R(x)$.
     - Transmitted Codeword $T(x) = (D(x) \times 2^r) + R(x)$.
     - Receiver divides $T'(x)$ by $G(x)$. If remainder is zero, no error detected.
   - **Standard CRC Polynomials:**
     - CRC-8: $x^8 + x^2 + x + 1$
     - CRC-16 (ANSI): $x^{16} + x^{15} + x^2 + 1$
     - CRC-32 (IEEE 802.3 Ethernet): $x^{32} + x^{26} + x^{23} + \dots + 1$
2. **Hamming Error-Correcting Code:**
   - To detect $d$ single-bit errors: Minimum Hamming Distance $d_{min} \ge d + 1$.
   - To correct $t$ single-bit errors: Minimum Hamming Distance $d_{min} \ge 2t + 1$.
   - **Hamming $(7,4)$ Code:** Encodes 4 data bits $(d_1, d_2, d_3, d_4)$ with 3 parity bits $(p_1, p_2, p_3)$ positioned at powers of 2 (positions 1, 2, 4). Corrects single-bit error via syndrome index.

---

## 2. Multiple Access Protocols (MAC)

### 2.1 Random Access Protocols
- **Pure ALOHA:** Any station can transmit whenever it has a frame. Vulnerable period $T_{vuln} = 2 \times T_{fr}$. Maximum throughput $S_{max} = \frac{1}{2e} \approx 18.4\%$ at traffic load $G = 0.5$.
- **Slotted ALOHA:** Time divided into discrete slots equal to $T_{fr}$. Transmission allowed only at slot boundary. Vulnerable period $T_{vuln} = T_{fr}$. Maximum throughput $S_{max} = \frac{1}{e} \approx 36.8\%$ at $G = 1.0$.
- **CSMA (Carrier Sense Multiple Access):** Listen before transmitting ("Carrier Sense").
  - **1-Persistent CSMA:** Transmits immediately when channel is sensed idle; if busy, senses continuously. High collision probability when multiple nodes wait.
  - **Non-Persistent CSMA:** If channel busy, waits a random backoff time before sensing again. Reduces collisions but increases idle channel time.
  - **p-Persistent CSMA:** Transmits with probability $p$ if idle, waits for next slot with probability $(1-p)$.
- **CSMA/CD (Carrier Sense Multiple Access with Collision Detection - IEEE 802.3):**
  - "Listen while talking". If a collision is detected during transmission, node aborts transmission immediately, transmits a 32-bit **Jamming Signal**, and executes the **Binary Exponential Backoff** algorithm.
  - **Condition for Collision Detection:** Transmission time must be at least twice the maximum round-trip propagation delay:
    $$T_{trans} \ge 2 \times T_{prop} \implies \frac{L_{min}}{\text{Bandwidth}} \ge 2 \times \frac{\text{Distance}}{v}$$
  - **Standard Ethernet Minimum Frame Size:** $L_{min} = 64 \text{ bytes (512 bits)}$.
  - **Binary Exponential Backoff:** After $k$-th collision ($k \le 10$), choose random slot $R \in [0, 2^k - 1]$, wait $R \times 512\text{ bit times}$. Abort after 16 collisions.
- **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance - IEEE 802.11):**
  - Used in wireless where collision detection is infeasible due to signal fading and the Hidden Terminal Problem.
  - Uses **Interframe Spaces (IFS)**: SIFS (Shortest), PIFS, DIFS (Distributed IFS).
  - Uses **RTS/CTS (Request-to-Send / Clear-to-Send)** virtual carrier sensing using Network Allocation Vector (NAV) timers.

### 2.2 Controlled Access & Channelization
- **Controlled Access:** Reservation, Polling (Primary-Secondary), Token Passing (Token Ring IEEE 802.5).
- **Channelization:** FDMA (Frequency Division), TDMA (Time Division), CDMA (Code Division Multiple Access using orthogonal Walsh-Hadamard codes).

---

## 3. Link-Layer Addressing, Ethernet & Connecting Devices

### 3.1 MAC Addressing & ARP
- **MAC Address:** 48-bit physical address formatted as 6 hexadecimal pairs (`00:1A:2B:3C:4D:5E`). First 24 bits = OUI (Organizationally Unique Identifier assigned by IEEE), last 24 bits = Vendor-assigned NIC serial.
- **ARP (Address Resolution Protocol - RFC 826):** Resolves a known destination IPv4 address to its corresponding physical MAC address using broadcast ARP Request and unicast ARP Reply.

### 3.2 IEEE 802.3 Standard Ethernet Frame Format
| Preamble | SFD | Destination MAC | Source MAC | EtherType / Length | Payload (Data) | FCS (CRC-32) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 7 Bytes | 1 Byte | 6 Bytes | 6 Bytes | 2 Bytes | 46 – 1500 Bytes | 4 Bytes |
- **Preamble:** Alternating 10101010 pattern for physical clock synchronization.
- **SFD (Start Frame Delimiter):** `10101011` marks the beginning of the frame header.
- **Minimum Frame Size:** $6 + 6 + 2 + 46 + 4 = 64 \text{ bytes}$.
- **Maximum Frame Size (MTU 1500):** $6 + 6 + 2 + 1500 + 4 = 1518 \text{ bytes}$ (1522 with 802.1Q VLAN tag).

### 3.3 Network Connecting Devices
- **Repeater / Hub (Layer 1):** Regenerates and broadcasts electrical signals to all ports (Single Collision Domain, Single Broadcast Domain).
- **Bridge / Switch (Layer 2):** Forwards frames based on MAC address table (CAM Table learned via source MAC filtering). Splits collision domains (Each port is an independent collision domain), single broadcast domain. Uses **Spanning Tree Protocol (IEEE 802.1D)** to prevent switching loops.
- **Router (Layer 3):** Forwards packets based on IP destination address. Splits both collision and broadcast domains.

---

## 4. Wireless LANs (IEEE 802.11) & Mobile IP

### 4.1 IEEE 802.11 Wireless LAN Architecture
- **BSS (Basic Service Set):** Group of wireless stations controlled by an Access Point (AP) in Infrastructure mode, or peer-to-peer in Ad-Hoc / IBSS mode.
- **ESS (Extended Service Set):** Multiple BSSs interconnected via a wired Distribution System (DS).
- **Hidden Station Problem:** Station A and Station C cannot hear each other, but both transmit to AP B simultaneously causing a collision. Solved by RTS/CTS handshaking.
- **Exposed Station Problem:** Station B transmits to A; Station C mistakenly defers transmission to D because it senses B's carrier.

### 4.2 Mobile IP (RFC 5944)
- **Entities:** Mobile Node (MN), Home Agent (HA), Foreign Agent (FA).
- **Addresses:** Home Address (permanent IP in home network), Care-of Address (CoA - temporary IP assigned in visited network).
- **Triangular Routing:**
  - Correspondent Node (CN) sends packet to MN's permanent Home Address.
  - Home Agent intercepts packet, encapsulates it in a tunnel (IP-in-IP encapsulation), and forwards it to the Care-of Address (FA/MN).
  - MN sends replies directly to CN (or via reverse tunneling).

---

## 5. Linux Datalink Provider Interface & Raw Sockets (UNP Ch 29)
- **`PF_PACKET` / `AF_PACKET`:** Linux-specific protocol family allowing user-space applications to send and receive raw link-layer Ethernet frames directly bypassing the kernel TCP/IP stack.
- **Socket Creation:**
  ```c
  int sock = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
  ```
- **Use Cases:** Network packet sniffers (Wireshark, tcpdump), custom protocol analyzers, ARP spoofing detection.
