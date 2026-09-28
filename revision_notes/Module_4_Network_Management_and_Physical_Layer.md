# PCCST501 Computer Networks — Module 4 Revision Notes

**Course:** PCCST501 Computer Networks (Semester 5 B.Tech CSE)  
**Institution:** Viswajyothi College of Engineering and Technology (VJCET)  
**Faculty:** Prof. Anju Markose, Assistant Professor, Dept. of CSE  
**Prescribed Textbooks:**  
- Behrouz A. Forouzan, *Computer Networks: A Top-Down Approach*, McGraw Hill (Ch 7 & Ch 9)  

---

## 1. Network Management: SNMP & ASN.1

### 1.1 Network Management Framework Architecture
The Internet Network Management framework consists of three core components:
1. **SMI (Structure of Management Information - RFC 2578):** Defines the general rules for naming objects, defining object types, and specifying value representations.
2. **MIB (Management Information Base - RFC 1213):** The structured collection of managed objects residing on the network device.
3. **SNMP (Simple Network Management Protocol):** The application-layer protocol used to exchange management parameters between managers and agents over UDP Port 161 (Agent) and Port 162 (Trap/Notification Receiver).

### 1.2 MIB-II Object Hierarchy & OID Naming
- Managed objects are identified by unique **Object Identifiers (OIDs)** in a global hierarchical tree:
  - `iso (1) . org (3) . dod (6) . internet (1) . mgmt (2) . mib-2 (1)` $\rightarrow$ **`1.3.6.1.2.1`**
- **Key MIB-II Subtrees:**
  - `system (1.3.6.1.2.1.1)`: `sysDescr`, `sysUpTime`, `sysContact`, `sysName`
  - `interfaces (1.3.6.1.2.1.2)`: `ifNumber`, `ifTable` (interface status, speed, error counters)
  - `ip (1.3.6.1.2.1.4)`: IP forwarding tables, address translation
  - `tcp (1.3.6.1.2.1.6)` / `udp (1.3.6.1.2.1.7)`: Active transport connections and port statistics

### 1.3 ASN.1 (Abstract Syntax Notation One) & BER
- **ASN.1:** A standardized formal language for describing data structures independently of machine hardware architectures.
- **BER (Basic Encoding Rules):** Defines the binary encoding of ASN.1 data into a triplet structure:
  $$\mathbf{[Tag - Length - Value \ (TLV)]}$$
  - **Tag (1 Byte):** Identifies data type (e.g., `0x02` = INTEGER, `0x04` = OCTET STRING, `0x06` = OBJECT IDENTIFIER, `0x30` = SEQUENCE).
  - **Length:** Specifies the number of octets in the Value field.
  - **Value:** The actual raw data payload.

### 1.4 SNMP Operations & Protocol Data Units (PDUs)
- `GetRequest`: Manager $\rightarrow$ Agent (Retrieves value of one or more specific MIB variables).
- `GetNextRequest`: Manager $\rightarrow$ Agent (Used to iteratively walk through tables and lexicographical OID trees).
- `GetBulkRequest` (SNMPv2/v3): Retrieves large blocks of table rows in a single request.
- `SetRequest`: Manager $\rightarrow$ Agent (Modifies configuration parameters on the managed device).
- `Response`: Agent $\rightarrow$ Manager (Returns requested values or error status).
- `Trap` (Port 162): Unsolicited event alert sent by Agent $\rightarrow$ Manager (e.g., link down, power failure, unauthorized authentication attempt).
- `InformRequest`: Manager-to-Manager acknowledgment-based alert.

---

## 2. Physical Layer: Data, Signals & Transmission Limits

### 2.1 Signals & Transmission Impairments
- **Analog vs. Digital Signals:** Analog signals are continuous waveforms; digital signals are discrete discrete-valued pulses.
- **Composite Periodic Signals:** According to **Fourier Analysis**, any composite periodic signal can be decomposed into a series of sine waves with different frequencies, amplitudes, and phases:
  $$s(t) = A_0 + \sum_{n=1}^{\infty} A_n \sin(2\pi n f_0 t + \phi_n)$$
- **Transmission Impairments:**
  1. **Attenuation:** Loss of signal energy over distance (compensated by amplifiers/repeaters). Measured in Decibels: $\text{dB} = 10 \log_{10}(P_2 / P_1)$.
  2. **Distortion:** Different frequency components propagate at different velocities, altering signal shape.
  3. **Noise:** Unwanted external signals (Thermal/Johnson noise, Induced noise, Crosstalk, Impulse noise).
  4. **Signal-to-Noise Ratio (SNR):** $\text{SNR} = \frac{P_{signal}}{P_{noise}}$, $\text{SNR}_{dB} = 10 \log_{10}(\text{SNR})$.

### 2.2 Theoretical Data Rate Limits
1. **Nyquist Bit Rate (Noiseless Channel):**
   Defines the maximum theoretical bit rate for a noiseless channel with bandwidth $B$ Hz and $L$ discrete signal voltage levels:
   $$\mathbf{\text{Bit Rate} = 2 \times B \times \log_2(L) \quad \text{[bps]}}$$
2. **Shannon Capacity (Noisy Channel with Thermal Noise):**
   Defines the ultimate theoretical upper bound on channel capacity $C$ for a channel with bandwidth $B$ Hz and signal-to-noise ratio $\text{SNR}$:
   $$\mathbf{C = B \times \log_2(1 + \text{SNR}) \quad \text{[bps]}}$$

---

## 3. Digital Transmission & Line Coding

### 3.1 Line Coding Schemes
Converting binary data into discrete physical voltage waveforms:

| Line Coding Scheme | Voltage Representation | Characteristics, Advantages & Disadvantages |
| :--- | :--- | :--- |
| **NRZ-L (Level)** | Bit 0 = Positive ($+V$), Bit 1 = Negative ($-V$) | Simple, but has DC component and loses synchronization on long strings of 0s or 1s. |
| **NRZ-I (Invert)** | Bit 1 = Transition at beginning; Bit 0 = No transition | Solves sync on consecutive 1s, but still loses sync on long runs of 0s. |
| **Manchester (802.3)** | Bit 0 = High-to-Low; Bit 1 = Low-to-High (Mid-bit transition) | **Self-synchronizing**, zero DC component, but requires **double the bandwidth** ($2\times$ baud rate). |
| **Differential Manchester** | Transition at start for 0; No start transition for 1 (Always mid-bit transition) | Excellent noise immunity and clock recovery; used in Token Ring. |
| **AMI (Bipolar)** | Bit 0 = 0V; Bit 1 = Alternating $+V$ and $-V$ | Zero DC bias, but loses clock synchronization on long runs of 0s. |
| **B8ZS / HDB3** | Scrambling: Replaces 8 consecutive 0s with intentional bipolar violations (`000VB0VB`) | Maintains DC balance and guarantees clock sync on digital carrier lines (T1/E1). |

---

## 4. Analog Transmission & Modulation

- **Digital-to-Analog Modulation:**
  - **ASK (Amplitude Shift Keying):** Variations in carrier wave amplitude ($s(t) = A_1 \cos(2\pi f_c t)$ for bit 1, $A_2 \cos(2\pi f_c t)$ for bit 0). Highly susceptible to noise.
  - **FSK (Frequency Shift Keying):** Variations in carrier frequency ($f_1$ vs $f_2$). High noise immunity.
  - **PSK (Phase Shift Keying):** Variations in carrier phase ($0^\circ$ for bit 1, $180^\circ$ for bit 0 in BPSK; 4 phases in QPSK sending 2 bits/baud).
- **QAM (Quadrature Amplitude Modulation):** Combines ASK and PSK to transmit high data densities:
  - 16-QAM sends 4 bits per baud ($2^4 = 16$ constellation points).
  - 64-QAM sends 6 bits per baud; 256-QAM sends 8 bits per baud.

---

## 5. Bandwidth Utilization & Transmission Media

### 5.1 Multiplexing Techniques
- **FDM (Frequency Division Multiplexing):** Divides analog channel bandwidth into distinct non-overlapping frequency bands separated by guard bands (used in Radio/TV, Cable TV).
- **WDM (Wavelength Division Multiplexing):** Optical multiplexing combining multiple laser wavelengths over a single optical fiber.
- **TDM (Time Division Multiplexing):** Digital technique interleaving time slots:
  - **Synchronous TDM:** Fixed time slots allocated to each sender regardless of activity (wastes idle bandwidth).
  - **Statistical / Asynchronous TDM:** Dynamically assigns time slots only to active channels with data to send on-demand.

### 5.2 Guided & Unguided Media
- **Guided Media:**
  - **Twisted Pair:** UTP (Unshielded Cat 5e/6/6a - $100\text{m}$ segment limit), STP (Shielded). Twisting cancels external electromagnetic interference.
  - **Coaxial Cable:** Copper core, dielectric insulator, metallic braided shield (RG-58, RG-59).
  - **Optical Fiber:** Silica glass core; light propagates via **Total Internal Reflection** ($n_{core} > n_{cladding}$). Immune to EMI, high bandwidth, long distances ($> 40\text{ km}$). Single-Mode (laser, narrow core, zero modal dispersion) vs Multi-Mode (LED, wider core, modal dispersion).
- **Unguided (Wireless) Media:**
  - **Radio Waves (3 kHz – 1 GHz):** Omnidirectional, penetrate solid obstacles.
  - **Microwaves (1 GHz – 300 GHz):** Highly directional, line-of-sight propagation, parabolic dish antennas.
  - **Infrared (300 GHz – 400 THz):** Short range, line-of-sight, cannot penetrate walls (secure for indoor remotes/peripherals).
  - **Satellite Communication:** GEO ($\sim 36,000\text{ km}$, 270 ms delay), MEO (GPS $\sim 20,000\text{ km}$), LEO (Starlink $\sim 500\text{–}1200\text{ km}$, low latency $\approx 25\text{ ms}$).
