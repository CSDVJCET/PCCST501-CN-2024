# PCCST501 Computer Networks — KTU 2024 Scheme Course Portal

**Official Course Repository & Learning Portal**  
**Course Code:** PCCST501 | **Course Name:** Computer Networks  
**Curriculum Scheme:** KTU 2024 Scheme (Semester S5 B.Tech CSE / AI / CY / DS)  
**Institution:** Viswajyothi College of Engineering and Technology (VJCET), Vazhakulam  
**Faculty In-Charge:** Prof. Anju Markose, Assistant Professor, Department of Computer Science & Engineering  
**Contact Email:** `csd@vjcet.com`  

---

## 🌐 Live Web Portal on GitHub Pages

When pushed to your GitHub repository, this web portal will be instantly accessible online at:
```
https://<your-github-username>.github.io/<your-repo-name>/
```

### 🚀 How to Publish to Your GitHub Repository & Enable GitHub Pages:

1. **Initialize and Push to your GitHub Repository:**
   ```bash
   git init
   git config user.name "Prof. Anju Markose"
   git config user.email "csd@vjcet.com"
   git add .
   git commit -m "Initial commit: PCCST501 Computer Networks 2024 Scheme Course Portal"
   
   # Add your GitHub repository remote
   git branch -M main
   git remote add origin https://github.com/<your-github-username>/<your-repo-name>.git
   git push -u origin main
   ```

2. **Enable Free Hosting on GitHub Pages:**
   - Open your repository on GitHub.
   - Click on **Settings** (top right tab) $\rightarrow$ **Pages** (left sidebar).
   - Under **Build and deployment** $\rightarrow$ **Source**, choose **Deploy from a branch**.
   - Under **Branch**, select `main` and folder `/ (root)`, then click **Save**.
   - In 1–2 minutes, your website link `https://<your-github-username>.github.io/<your-repo-name>/` will be live for students and faculty!

---

## 📚 Course Curriculum & Module Overview (KTU 2024 Scheme)

| Module | Contact Hours | Core Topics | Hands-On / Code Focus |
| :--- | :---: | :--- | :--- |
| **Module 1** | **6 Hrs** | Overview of Internet, Protocol Layering, Client-Server Applications (HTTP/1.1/2, FTP, SMTP/MIME, DNS), Peer-to-Peer Paradigm & BitTorrent Case Study. | Multi-threaded HTTP Server, DNS Query Resolver, BitTorrent Swarm Simulator |
| **Module 2** | **18 Hrs** | Transport Layer (UDP, TCP 3-way handshake, Congestion Control: AIMD, Reno), Berkeley Sockets API, I/O Multiplexing (`select()`, `poll()`), Network Layer (IPv4/IPv6, CIDR Subnetting, RIP Distance Vector, OSPF Link State, BGP, Multicast IGMP/PIM), Linux Kernel Routing Architecture. | TCP/UDP Echo in C, `select()` Server in C, IPv4 Subnet Calculator, Dijkstra & Bellman-Ford Simulators |
| **Module 3** | **11 Hrs** | Data Link Layer (Framing, Byte/Bit Stuffing, CRC-32, Hamming Code), MAC Protocols (ALOHA, CSMA/CD, CSMA/CA), IEEE 802.3 Ethernet, IEEE 802.11 Wi-Fi, Mobile IP, Linux Datalink Provider Interface (`PF_PACKET` Raw Sockets). | CRC Modulo-2 Divider, Hamming (7,4) Single-bit Corrector, Linux `PF_PACKET` Raw Socket Sniffer |
| **Module 4** | **9 Hrs** | Network Management (SNMP Operations & PDUs, SMI, MIB-II tree, ASN.1 & BER TLV encoding), Physical Layer (Data & Signals, Nyquist Bit Rate, Shannon Channel Capacity, Line Coding: Manchester, Diff Manchester, AMI, Multiplexing: FDM/TDM, Transmission Media). | Line Coding Waveform Generator, Nyquist & Shannon Capacity Calculator |

---

## 🧰 Interactive Browser-Based Simulators (`tutorials.html`)

- **IPv4 CIDR Subnet Calculator:** Computes Network ID, Broadcast IP, Subnet Mask, and Total Usable Hosts.
- **CRC Modulo-2 Binary Divisor:** Step-by-step polynomial division and error detection verification.
- **HTML5 Canvas Line Coding Waveform Generator:** Visualizes NRZ-L, NRZ-I, Manchester, Differential Manchester, and AMI waveforms.
- **Shannon & Nyquist Capacity Calculator:** Computes theoretical data rate limits for bandlimited noisy/noiseless channels.

---

## 📂 Repository Directory Structure

```
├── index.html                   # Main Course Portal Homepage
├── syllabus.html                # KTU 2024 Scheme Syllabus & CO-PO Mapping
├── modules.html                 # Lecture Modules Curriculum Hub
├── module1.html                 # Module 1 Detailed Lecture Notes
├── module2.html                 # Module 2 Detailed Lecture Notes
├── module3.html                 # Module 3 Detailed Lecture Notes
├── module4.html                 # Module 4 Detailed Lecture Notes
├── networklab.html              # PCCSL507 Network Lab Manual
├── tutorials.html               # Interactive Calculators & Simulators
├── questionbank.html            # Solved KTU Model Exam Question Bank
├── assignments.html             # CIE Assignments & Mini Project Ideas
├── resources.html               # Central Download Center
├── assets/
│   ├── css/style.css            # Modern Glassmorphic Design System
│   ├── js/main.js               # Interactive Application Logic & Calculators
│   ├── ppts/                    # Master PowerPoint Presentations (.pptx)
│   ├── notes_pdf/               # Exam Revision Notes & Lab Manuals (.pdf)
│   └── handson_code/            # C and Python Socket & Protocol Programs
├── revision_notes/              # Markdown Revision Summaries
├── question_bank/               # University Model Question Papers
└── lab_manuals/                 # Complete Hands-on Lab Manuals
```

---

## 📖 Prescribed Textbooks (KTU 2024 Scheme)
1. **Behrouz A. Forouzan**, *Computer Networks: A Top-Down Approach*, McGraw Hill, Special Indian Edition, 2017.
2. **W. Richard Stevens, Bill Fenner, Andrew M. Rudoff**, *Unix Network Programming, Volume 1: The Sockets Networking API*, Pearson Education, 3/e, 2004.
3. **Sameer Seth, M. Ajaykumar Venkatesulu**, *TCP/IP Architecture, Design, and Implementation in Linux*, Wiley, 1/e, 2008.

---
&copy; 2026-27 Viswajyothi College of Engineering and Technology (VJCET) &bull; Prof. Anju Markose (`csd@vjcet.com`)
