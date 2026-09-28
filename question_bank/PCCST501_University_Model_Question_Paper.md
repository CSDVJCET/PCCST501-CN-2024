# PCCST501 Computer Networks — University Model Question Paper

**APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY (KTU)**  
**FIFTH SEMESTER B.TECH DEGREE EXAMINATION**  
**Course Code:** PCCST501  
**Course Name:** COMPUTER NETWORKS  
*(Common to CS, CD, CM, CR, CA, AD, AI, CB, CN, CU, CI)*  
**Max. Marks:** 60 &nbsp;&nbsp;|&nbsp;&nbsp; **Duration:** 2.5 Hours  

---

### PART A (Answer all questions. Each question carries 3 marks: 8 × 3 = 24 Marks)

1. **[CO1, K2]** Differentiate between persistent and non-persistent HTTP connections with appropriate timing diagrams.
2. **[CO1, K2]** Explain the role of the DNS hierarchy and differentiate between iterative and recursive DNS queries.
3. **[CO2, K3]** A TCP connection is in the Congestion Avoidance phase with `cwnd = 16 MSS`. If a triple duplicate ACK is received, what will be the new values of `ssthresh` and `cwnd` in TCP Reno? Justify.
4. **[CO3, K3]** An organization is granted the block `192.168.10.0/24`. Design a subnetting scheme to support 4 departments requiring 25 hosts each. State the subnet mask, first host, last host, and broadcast address of the first subnet.
5. **[CO4, K3]** Explain why the minimum frame size in Standard 10 Mbps Ethernet is fixed at 64 bytes. Derive the relationship between $L_{min}$, bandwidth, and propagation delay.
6. **[CO4, K2]** What is the Hidden Station Problem in Wireless LANs (IEEE 802.11)? How does the RTS/CTS mechanism resolve it?
7. **[CO5, K2]** Describe the structure of an SNMP Management Information Base (MIB) and explain the role of Object Identifiers (OIDs).
8. **[CO5, K3]** A noiseless channel has a bandwidth of 4 kHz. Calculate the maximum theoretical bit rate if the signal uses 16 discrete voltage levels (Nyquist theorem).

---

### PART B (Answer any ONE full question from each module. Each question carries 9 marks: 4 × 9 = 36 Marks)

#### MODULE 1
9. **(a)** Describe the client-server and peer-to-peer (P2P) application paradigms. **(4 Marks) [CO1, K2]**  
   **(b)** With neat architectural diagrams, explain the working of the BitTorrent file-sharing protocol. Detail the functions of the torrent file, tracker, rarest-first piece selection, and tit-for-tat choking algorithms. **(5 Marks) [CO1, K3]**  
   *OR*  
10. **(a)** Explain the SMTP protocol message exchange for sending an email. Why is MIME required alongside SMTP? **(5 Marks) [CO1, K2]**  
    **(b)** Explain the dual-channel architecture of FTP (Control connection vs Data connection) and explain Active vs Passive FTP modes. **(4 Marks) [CO1, K2]**  

---

#### MODULE 2
11. **(a)** Explain the TCP 3-way handshake for connection establishment and 4-way handshake for connection termination with state transitions. **(5 Marks) [CO2, K3]**  
    **(b)** Discuss the concept of I/O Multiplexing in UNIX socket programming. Compare the `select()` and `poll()` system calls with code prototypes. **(4 Marks) [CO2, K3]**  
    *OR*  
12. **(a)** Explain the Link-State (OSPF) routing algorithm. Given a network topology with 6 routers, trace Dijkstra's algorithm to compute the shortest-path routing table for the root router. **(5 Marks) [CO3, K3]**  
    **(b)** Describe the IPv6 header format and discuss the strategies for transitioning from IPv4 to IPv6 (Dual Stack, Tunneling, Header Translation). **(4 Marks) [CO3, K2]**  

---

#### MODULE 3
13. **(a)** A data word `1101011011` is to be transmitted using CRC with generator polynomial $G(x) = x^4 + x + 1$.  
    &nbsp;&nbsp;&nbsp;&nbsp;i) Compute the transmitted CRC codeword.  
    &nbsp;&nbsp;&nbsp;&nbsp;ii) Verify how the receiver detects an error if the 3rd bit from the left is inverted during transmission. **(5 Marks) [CO4, K3]**  
    **(b)** Explain the working of the CSMA/CD protocol used in Ethernet. Describe the Binary Exponential Backoff algorithm in detail. **(4 Marks) [CO4, K3]**  
    *OR*  
14. **(a)** Explain the IEEE 802.3 Ethernet frame format. Describe the role of Preamble, SFD, EtherType, and FCS fields. **(4 Marks) [CO4, K2]**  
    **(b)** Explain Mobile IP architecture. Detail the roles of Home Agent, Foreign Agent, Care-of Address, and explain the Triangular Routing problem with tunneling solutions. **(5 Marks) [CO4, K3]**  

---

#### MODULE 4
15. **(a)** Explain the SNMP protocol operations and Protocol Data Units (PDUs): `GetRequest`, `GetNextRequest`, `GetBulkRequest`, `SetRequest`, `Response`, and `Trap`. **(5 Marks) [CO5, K2]**  
    **(b)** Explain ASN.1 and Basic Encoding Rules (BER) with an illustrative example of TLV (Tag, Length, Value) encoding. **(4 Marks) [CO5, K2]**  
    *OR*  
16. **(a)** For a bit sequence `01001110`, draw the digital line coding waveforms for:  
    &nbsp;&nbsp;&nbsp;&nbsp;i) NRZ-L &nbsp;&nbsp; ii) NRZ-I &nbsp;&nbsp; iii) Manchester &nbsp;&nbsp; iv) Differential Manchester &nbsp;&nbsp; v) AMI (Bipolar). **(5 Marks) [CO5, K3]**  
    **(b)** State and explain the Shannon Channel Capacity Theorem. A telephone line has a bandwidth of 3 kHz and an SNR of 30 dB. Calculate its theoretical channel capacity in bps. **(4 Marks) [CO5, K3]**  
