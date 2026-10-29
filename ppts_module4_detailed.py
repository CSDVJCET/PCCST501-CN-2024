"""
ppts_module4_detailed.py
Comprehensive, classroom-ready presentation decks for Module 4: Network Management & Physical Layer Fundamentals.
Prepared exclusively for:
Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
PCCST501 Computer Networks (KTU 2024 Scheme)
"""

from build_master_ppts_framework import (
    init_prs, create_title_slide, create_content_slide, 
    create_comparison_slide, create_numerical_slide, create_code_slide, create_exam_booster_slide
)

def build_m4_1(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.1", "Network Management Architecture & SNMP Protocol",
        "Managing Entities (Managers), Managed Devices (Agents), MIB, SNMP Protocol Operations, SNMPv1 vs SNMPv2c vs SNMPv3 (USM & VACM)",
        "Module 4"
    )
    
    create_content_slide(prs, "4.1.1 Network Management Framework & SNMP Operations", "M4.1 SNMP FRAMEWORK", [
        ("Network Management Architecture", "Consists of 4 pillars: 1. **Managing Entity (Manager / NMS)**: Centralized workstation running management software. 2. **Managed Devices**: Routers, switches, servers, hosts containing management data. 3. **Management Agent**: Software daemon running inside managed device. 4. **Management Information Base (MIB)**: Virtual database of manageable object variables."),
        ("SNMP Protocol (Simple Network Management Protocol - RFC 3411)", "Operates over UDP port 161 (Manager to Agent queries) and UDP port 162 (Agent to Manager asynchronous Traps)."),
        ("Core SNMP Protocol Operations", "1. **GetRequest**: Manager fetches value of 1 or more MIB variables from Agent. \\n 2. **GetNextRequest**: Manager fetches the lexicographically next MIB variable (used for MIB tree walking and table traversal). \\n 3. **GetBulkRequest (v2c/v3)**: Fetches large blocks of table rows in a single packet. \\n 4. **SetRequest**: Manager sets/modifies configuration value on Agent device. \\n 5. **Response**: Agent returns requested data values or error status. \\n 6. **Trap / InformRequest**: Unsolicited alert sent by Agent to Manager upon an event (e.g., link failure, reboot). `InformRequest` requires Manager ACK.")
    ], "SNMP Ports & PDUs", [
        "UDP Port 161: Agent listener",
        "UDP Port 162: Manager Trap listener",
        "GetRequest: Read variable",
        "SetRequest: Write configuration",
        "GetNext: Sequential MIB walk",
        "GetBulk: Fast table download",
        "Trap: Asynchronous alert"
    ])
    
    create_comparison_slide(prs, "4.1.2 SNMP Version Evolution: SNMPv1 vs SNMPv2c vs SNMPv3", "M4.1 SNMP EVOLUTION",
        "SNMPv1 & SNMPv2c", [
            ("Security Model", "Plaintext Community Strings (`public` for read-only, `private` for read-write). Vulnerable to packet sniffing"),
            ("Operations (v1)", "Get, GetNext, Set, Response, Trap"),
            ("Enhancements (v2c)", "Adds `GetBulkRequest` for fast table fetching and 64-bit high-capacity counters (`Counter64`), but retains plaintext community security"),
            ("Suitability", "Isolated, trusted internal LANs only")
        ],
        "SNMPv3 (Cryptographically Secure)", [
            ("Security Model", "User-Based Security Model (USM) + View-Based Access Control Model (VACM)"),
            ("Authentication", "Message digest authentication via HMAC-MD5 or HMAC-SHA (verifies origin and prevents tampering)"),
            ("Confidentiality", "Payload encryption via DES or AES-128 / AES-256 (prevents eavesdropping)"),
            ("Message Freshness", "Timestamps and boot counters prevent Replay attacks"),
            ("Enterprise Standard", "Mandatory standard for secure network management")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M4.1", "Network Management & SNMP", "K2 Understand",
        [
            "Explain the four components of the Network Management architecture (Manager, Agent, MIB, SNMP) with a neat diagram. (7 Marks)",
            "Describe the various SNMP protocol operations (GetRequest, GetNextRequest, GetBulkRequest, SetRequest, Trap, InformRequest). (8 Marks)",
            "Compare SNMPv1, SNMPv2c, and SNMPv3 with focus on the User-Based Security Model (USM) in SNMPv3. (7 Marks)"
        ],
        [
            "SNMP uses UDP port 161 for synchronous polling and port 162 for asynchronous event Traps.",
            "SNMPv2c introduced `GetBulk` and 64-bit counters; SNMPv3 added cryptographic authentication and AES encryption.",
            "`InformRequest` provides reliable delivery of trap notifications with manager acknowledgments."
        ]
    )
    return prs

def build_m4_2(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.2", "Structure of Management Information (SMI) & ASN.1",
        "Abstract Syntax Notation One (ASN.1), SMIv2 Macro Definitions, MIB OID Tree Hierarchy (1.3.6.1.2.1), Standard MIB-II Groups, BER Encoding",
        "Module 4"
    )
    
    create_content_slide(prs, "4.2.1 SMIv2 & MIB Object Identifier (OID) Tree Hierarchy", "M4.2 SMI & MIB HIERARCHY", [
        ("SMI (Structure of Management Information - RFC 2578)", "The formal language defining the rules for naming, specifying data types, and structuring management objects in the MIB."),
        ("ASN.1 (Abstract Syntax Notation One)", "A formal notation for describing data structures independently of machine hardware architectures. Defines primitives (INTEGER, OCTET STRING, OBJECT IDENTIFIER, SEQUENCE)."),
        ("Globally Unique OID Tree Hierarchy", "Every manageable variable is assigned a globally unique dot-delimited Object Identifier (OID) arranged in an inverted tree:"),
        ("Standard Internet MIB-2 Path", "`iso(1)` -> `org(3)` -> `dod(6)` -> `internet(1)` -> `mgmt(2)` -> `mib-2(1)` = **`1.3.6.1.2.1`**."),
        ("Standard MIB-II Functional Groups", "1. `system (1.3.6.1.2.1.1)`: Device name, description, uptime, contact. \\n 2. `interfaces (1.3.6.1.2.1.2)`: Subnet interfaces, MTU, speed, packet counters. \\n 3. `ip (1.3.6.1.2.1.4)`: IP routing tables, forward state, TTL, packet discards. \\n 4. `tcp (1.3.6.1.2.1.6)`: Active TCP connection table, current connections, timeouts. \\n 5. `udp (1.3.6.1.2.1.7)`: UDP listener table and datagram counters."),
        ("Basic Encoding Rules (BER)", "Transfers data over wire using **TLV format**: `Tag (Type)` | `Length` | `Value`.")
    ], "Standard MIB-2 Groups", [
        "1.3.6.1.2.1.1: system",
        "1.3.6.1.2.1.2: interfaces",
        "1.3.6.1.2.1.4: ip",
        "1.3.6.1.2.1.6: tcp",
        "1.3.6.1.2.1.7: udp",
        "1.3.6.1.2.1.11: snmp",
        "Encoding: BER TLV format"
    ])
    
    create_exam_booster_slide(
        prs, "M4.2", "SMI & ASN.1", "K2 Understand",
        [
            "Explain the role of SMI and ASN.1 in SNMP network management. (6 Marks)",
            "Illustrate the MIB Object Identifier (OID) tree hierarchy from Root to MIB-II (`1.3.6.1.2.1`) and describe the primary MIB-II groups (`system`, `interfaces`, `ip`, `tcp`). (8 Marks)",
            "Explain Basic Encoding Rules (BER) and the Tag-Length-Value (TLV) encoding format with an example. (6 Marks)"
        ],
        [
            "SMI defines how MIB data objects are formally defined using ASN.1 syntax.",
            "OID `1.3.6.1.2.1` is the root prefix for all standard Internet MIB-II management objects.",
            "BER encodes variables into machine-independent Tag-Length-Value (TLV) binary streams."
        ]
    )
    return prs

def build_m4_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.3", "Data and Signals: Theoretical Channel Capacity",
        "Analog vs Digital Signals, Bandwidth, Transmission Impairments (Attenuation, Noise), Signal-to-Noise Ratio (SNR), Nyquist Rate vs Shannon Capacity",
        "Module 4"
    )
    
    create_content_slide(prs, "4.3.1 Signals, Bandwidth & Transmission Impairments", "M4.3 DATA & SIGNALS", [
        ("Analog vs Digital Signals", "Analog signals have infinitely many continuous values over time (e.g., sine wave $s(t) = A \\sin(2\\pi f t + \\phi)$). Digital signals have discrete discrete levels (e.g., 0V and 5V pulses representing bits 0 and 1)."),
        ("Bandwidth ($B$)", "The range of frequencies contained in a composite signal: $B = f_{max} - f_{min}$ Hertz (Hz)."),
        ("Transmission Impairments", "1. **Attenuation**: Loss of signal energy over distance (measured in decibels $dB = 10 \\log_{10} (P_2 / P_1)$). Corrected via amplifiers/repeaters. \\n 2. **Distortion**: Different frequency components travel at different speeds, altering composite waveform shape. \\n 3. **Noise**: Unwanted external energy added to signal (Thermal noise $N_0 = kTB$, Induced noise, Crosstalk, Impulse noise)."),
        ("Signal-to-Noise Ratio (SNR)", "Ratio of signal power to noise power: $SNR = \\frac{P_{signal}}{P_{noise}}$. In decibels: $SNR_{dB} = 10 \\log_{10} (SNR)$ (e.g., $SNR = 1000 \\implies SNR_{dB} = 30$ dB).")
    ], "Key Formulas", [
        "Bandwidth: B = f_max - f_min (Hz)",
        "Decibels: dB = 10 * log10(P2 / P1)",
        "SNR = P_signal / P_noise",
        "SNR_dB = 10 * log10(SNR)",
        "SNR = 10^(SNR_dB / 10)"
    ])
    
    create_comparison_slide(prs, "4.3.2 Channel Capacity Limits: Nyquist vs Shannon", "M4.3 NYQUIST VS SHANNON",
        "Nyquist Bit Rate (Noiseless Channel)", [
            ("Formulated By", "Harry Nyquist (1928)"),
            ("Channel Condition", "Assumes theoretical **noiseless** channel with bandwidth $B$ Hz and $L$ discrete signaling levels"),
            ("Formula", "$C = 2 \\times B \\times \\log_2 (L)$ bps"),
            ("Implication", "Data rate can be increased indefinitely by increasing the number of signal levels $L$, but is constrained by noise in practice")
        ],
        "Shannon Capacity (Noisy Channel)", [
            ("Formulated By", "Claude Shannon (1948)"),
            ("Channel Condition", "Assumes real-world channel contaminated with Thermal White Noise (Gaussian Noise)"),
            ("Formula", "$C = B \\times \\log_2 (1 + SNR)$ bps"),
            ("Implication", "Defines the absolute physical upper bound on error-free channel capacity regardless of how many signal levels $L$ are used")
        ]
    )
    
    create_numerical_slide(
        prs, "4.3.3 Worked KTU Numerical: Nyquist & Shannon Capacity", "M4.3 CAPACITY NUMERICAL",
        "A telephone line has bandwidth B = 3000 Hz and Signal-to-Noise ratio SNR_dB = 31.62 dB (SNR approx 1452). (a) Calculate the theoretical maximum Shannon channel capacity. (b) To achieve this capacity on a noiseless line with B = 3000 Hz, how many signal levels L are required by Nyquist formula?",
        [
            "Shannon Capacity: C = B * log2(1 + SNR) bps",
            "Given SNR_dB = 31.62 dB -> SNR = 10^(31.62 / 10) = 10^3.162 = 1452.1",
            "Nyquist Bit Rate: C = 2 * B * log2(L) bps -> log2(L) = C / (2 * B) -> L = 2^(C / 2B)."
        ],
        [
            (1, "1 + SNR = 1 + 1452.1 = 1453.1"),
            (2, "log2(1453.1) = log10(1453.1) / log10(2) = 3.1623 / 0.30103 = 10.505 bits"),
            (3, "Shannon Capacity C = 3000 Hz * 10.505 = 31,515 bps (approx 31.5 kbps)."),
            (4, "Equating to Nyquist: 31,515 = 2 * 3000 * log2(L) = 6000 * log2(L)"),
            (5, "log2(L) = 31,515 / 6000 = 5.2525 -> L = 2^5.2525 = 38.12 -> L = 38 signal levels.")
        ],
        "Shannon Capacity C = 31.5 kbps | Required Nyquist signal levels L = 38",
        "Shannon determines the upper capacity limit; Nyquist tells us how many signal levels L are required to realize it."
    )
    
    create_exam_booster_slide(
        prs, "M4.3", "Channel Capacity & Signals", "K3 Apply",
        [
            "Explain the three transmission impairments: Attenuation, Distortion, and Noise with diagrams and formulas. (7 Marks)",
            "State and derive the Nyquist Bit Rate formula for noiseless channels and Shannon Capacity theorem for noisy channels. (8 Marks)",
            "A channel has bandwidth B = 4 kHz. Calculate Shannon capacity if SNR_dB = 20 dB. (5 Marks)"
        ],
        [
            "Nyquist bit rate ($2B \\log_2 L$) applies to ideal noiseless channels.",
            "Shannon capacity ($B \\log_2(1+SNR)$) establishes the fundamental thermodynamic limit of noisy channels.",
            "Decibels convert logarithmic power ratios into simple additive terms."
        ]
    )
    return prs

def build_m4_4(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.4", "Digital Transmission & Line Coding Schemes",
        "Line Coding Criteria (DC, Sync, Baseline Wander), Unipolar, Polar (NRZ, RZ, Manchester, Diff Manchester), Bipolar (AMI), Block Coding (4B/5B), PCM & DM",
        "Module 4"
    )
    
    create_content_slide(prs, "4.4.1 Line Coding Design Criteria & Characteristics", "M4.4 LINE CODING CRITERIA", [
        ("Line Coding Definition", "The process of converting a sequence of digital bits (1s and 0s) into a discrete electrical/optical signal waveform for baseband transmission."),
        ("Key Line Coding Design Criteria", "1. **Signal Level vs Data Level**: Number of voltage states ($L$) vs bit values. \\n 2. **DC Component**: Frequencies around 0 Hz create heat, cannot pass through transformers/capacitors, and waste transmitter power. Desirable = Zero DC. \\n 3. **Self-Synchronization**: Signal transitions (edges) must allow receiver clock to synchronize timing, especially during long strings of consecutive 0s or 1s. \\n 4. **Baseline Wander**: Running average of signal voltage must remain constant to maintain accurate decision slicing threshold. \\n 5. **Error Detection**: Built-in coding violations indicate physical link errors."),
        ("Pulse Code Modulation (PCM)", "Digitizes analog signals in 3 steps: 1. **Sampling** (Nyquist Rate $f_s \\ge 2 f_{max}$), 2. **Quantization** (approximates sample amplitudes to discrete levels; introduces Quantization Error), 3. **Encoding** (maps quantized levels into $n$-bit binary codewords: Bit Rate $= n \\times f_s$).")
    ], "Line Coding Goals", [
        "Eliminate DC components",
        "Provide self-synchronization",
        "Prevent baseline wander",
        "Minimize bandwidth needs",
        "PCM: Sample -> Quantize -> Encode"
    ])
    
    create_comparison_slide(prs, "4.4.2 Major Line Coding Schemes Comparison", "M4.4 SCHEMES COMPARISON",
        "Unipolar & Polar NRZ", [
            ("Unipolar NRZ", "Bit 1 = Positive voltage $+V$, Bit 0 = Zero 0V. Severe DC component; no synchronization on long 0s/1s"),
            ("Polar NRZ-L (Level)", "Bit 1 = Negative $-V$, Bit 0 = Positive $+V$. Sensitive to polarity inversion"),
            ("Polar NRZ-I (Invert)", "Bit 1 = Transition at start of bit interval; Bit 0 = No transition. Immune to polarity inversion, but fails on consecutive 0s")
        ],
        "Biphase: Manchester & Differential Manchester", [
            ("Manchester (IEEE 802.3)", "Mid-bit transition: Bit 1 = High-to-Low transition; Bit 0 = Low-to-High transition. Perfect clock synchronization and Zero DC component, but doubles bandwidth requirement ($2 \\times$ baud rate)"),
            ("Differential Manchester (Token Ring)", "Always transitions in the middle for clocking. Bit 0 = Transition at start of bit interval; Bit 1 = No transition at start. Highly robust against wire twists")
        ],
        "Bipolar AMI & Multilevel", [
            ("Bipolar AMI", "Bit 0 = Zero 0V; Bit 1 = Alternating positive $+V$ and negative $-V$. Zero DC component, low bandwidth, but loses sync on long 0s (solved via B8ZS/HDB3 scrambling)")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M4.4", "Digital Transmission & Line Coding", "K3 Apply",
        [
            "Draw the line coding waveforms for the bit stream `10110001` using: (a) Unipolar NRZ, (b) NRZ-L, (c) NRZ-I, (d) Manchester, (e) Differential Manchester, (f) Bipolar AMI. (9 Marks)",
            "Explain the working of Pulse Code Modulation (PCM) with Sampling Theorem ($f_s \\ge 2f_{max}$), Quantization, and Encoding. (8 Marks)",
            "What is the DC component problem and baseline wander in digital transmission? (5 Marks)"
        ],
        [
            "Manchester coding guarantees a transition in every single bit cell for foolproof clock synchronization.",
            "Differential Manchester transitions at the start for bit 0, and has no start transition for bit 1.",
            "PCM digitizes voice signals at 8000 samples/sec $\\times$ 8 bits/sample = 64 kbps (standard DS0 channel)."
        ]
    )
    return prs

def build_m4_5(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.5", "Analog Transmission & Bandwidth Utilization (Multiplexing)",
        "Digital-to-Analog Modulation (ASK, FSK, PSK, QAM), Multiplexing Techniques (FDM, WDM, Synchronous vs Statistical TDM), Spread Spectrum (FHSS, DSSS)",
        "Module 4"
    )
    
    create_comparison_slide(prs, "4.5.1 Digital Modulation Schemes: ASK vs FSK vs PSK vs QAM", "M4.5 MODULATION SCHEMES",
        "ASK, FSK & PSK", [
            ("ASK (Amplitude Shift Keying / BASK)", "Bit 1 = High amplitude carrier $A_1 \\cos(2\\pi f_c t)$; Bit 0 = Low amplitude $A_2$ (or 0 in OOK). Susceptible to noise"),
            ("FSK (Frequency Shift Keying / BFSK)", "Bit 1 = Frequency $f_1$; Bit 0 = Frequency $f_2$. Robust against amplitude noise; requires higher bandwidth"),
            ("PSK (Phase Shift Keying / BPSK & QPSK)", "BPSK: Bit 1 = $0^\\circ$ phase, Bit 0 = $180^\\circ$ phase. QPSK: 2 bits per baud ($00, 01, 10, 11$) using 4 orthogonal phases ($45^\\circ, 135^\\circ, 225^\\circ, 315^\\circ$)")
        ],
        "QAM (Quadrature Amplitude Modulation)", [
            ("Concept", "Combines Amplitude Modulation (ASK) and Phase Modulation (PSK) simultaneously to maximize spectral efficiency"),
            ("16-QAM & 64-QAM", "16-QAM encodes 4 bits/symbol ($2^4 = 16$ constellation points); 64-QAM encodes 6 bits/symbol; 256-QAM encodes 8 bits/symbol"),
            ("Constellation Diagrams", "Visualizes constellation constellation points in In-Phase ($I$) and Quadrature ($Q$) 2D plane"),
            ("Applications", "Wi-Fi (802.11ac/ax), 4G/5G LTE, Cable modems (DOCSIS)")
        ]
    )
    
    create_comparison_slide(prs, "4.5.2 Multiplexing: FDM vs WDM vs Synchronous TDM vs Statistical TDM", "M4.5 MULTIPLEXING TAXONOMY",
        "Frequency & Optical Multiplexing", [
            ("FDM (Frequency-Division Multiplexing)", "Divides total analog bandwidth into distinct frequency channels separated by **Guard Bands** (e.g., FM radio, cable TV)"),
            ("WDM (Wavelength-Division Multiplexing)", "Optical analog of FDM. Combines multiple laser light beams of different wavelengths (e.g., 1550 nm, 1310 nm) onto a single optical fiber using diffraction prisms. DWDM handles 80+ channels")
        ],
        "Time-Division Multiplexing (TDM)", [
            ("Synchronous TDM", "Time divided into fixed recurring frames containing dedicated slots allocated round-robin to each input line. Slot wasted if an input line is idle"),
            ("Statistical TDM (Asynchronous)", "Dynamically allocates time slots **on demand** only to active lines transmitting data. Eliminates idle slot waste by adding channel address headers to each slot")
        ]
    )
    
    create_exam_booster_slide(
        prs, "M4.5", "Analog Transmission & Multiplexing", "K3 Apply",
        [
            "Explain Quadrature Amplitude Modulation (QAM) and draw the constellation diagrams for 4-QAM and 16-QAM. (8 Marks)",
            "Compare Synchronous TDM and Statistical TDM with framing and slot allocation diagrams. (7 Marks)",
            "Explain Spread Spectrum techniques: Frequency Hopping Spread Spectrum (FHSS) vs Direct Sequence Spread Spectrum (DSSS). (7 Marks)"
        ],
        [
            "QAM modulates both amplitude and phase to pack multiple bits into a single baud symbol.",
            "FDM shares bandwidth in frequency; TDM shares bandwidth in time slots.",
            "Statistical TDM dynamically allocates slots on demand, achieving much higher link utilization than Synchronous TDM."
        ]
    )
    return prs

def build_m4_6(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.6", "Physical Transmission Media",
        "Guided Media (Twisted Pair UTP/STP, Coaxial Cable, Fiber Optics SMF/MMF), Unguided Wireless (Radio Waves, Microwaves, Infrared)",
        "Module 4"
    )
    
    create_comparison_slide(prs, "4.6.1 Guided Media: Twisted Pair vs Coaxial vs Optical Fiber", "M4.6 GUIDED MEDIA",
        "Twisted-Pair & Coaxial Cable", [
            ("Twisted-Pair (UTP / STP)", "Two insulated copper wires twisted together to cancel electromagnetic interference (crosstalk). Cat 5e (100 MHz, 1 Gbps), Cat 6 (250 MHz, 10 Gbps up to 55m), Cat 6a (500 MHz, 10 Gbps 100m). Terminated with RJ-45 connectors"),
            ("Coaxial Cable", "Central copper core surrounded by dielectric insulator, metallic braided shield, and outer jacket. 10Base5 (Thicknet, 500m), 10Base2 (Thinnet, 185m), RG-59 (Cable TV). Terminated with BNC connectors")
        ],
        "Optical Fiber (Total Internal Reflection)", [
            ("Physics Principle", "Light pulses propagate via Total Internal Reflection inside glass core (refractive index $n_1$) surrounded by cladding ($n_2 < n_1$) when incident angle exceeds critical angle"),
            ("Multimode Step-Index", "Multiple light rays reflect abruptly at core-cladding boundary; causes modal dispersion (short distances)"),
            ("Multimode Graded-Index", "Core refractive index decreases gradually outward; light rays curve smoothly, reducing modal dispersion"),
            ("Single-Mode Fiber (SMF)", "Ultra-narrow core (8-10 $\\mu$m); single light ray propagates straight; zero modal dispersion; enables 100+ km long-haul backbone links")
        ]
    )
    
    create_content_slide(prs, "4.6.2 Unguided Media: Wireless Electromagnetic Spectrum", "M4.6 UNGUIDED WIRELESS", [
        ("Radio Waves (3 kHz to 1 GHz)", "Omnidirectional radiation pattern (transmitting antenna broadcasts signals in all directions). Penetrates physical walls effortlessly. Subject to multi-path interference. Used in AM/FM radio and cordless phones."),
        ("Microwaves (1 GHz to 300 GHz)", "Unidirectional, Line-of-Sight propagation. Focused beam using parabolic dish or horn antennas. Cannot penetrate solid obstacles (walls, hills). Used in cellular networks, satellite communications, and GPS."),
        ("Infrared Waves (300 GHz to 400 THz)", "High-frequency, short-range line-of-sight communication. Completely blocked by walls and solid obstacles (ensures indoor security without room-to-room interference). Used in TV remote controls and IrDA devices.")
    ], "Wireless Spectrum", [
        "Radio: Omnidirectional (Wall penetration)",
        "Microwaves: Line-of-sight (Dish antenna)",
        "Infrared: Short range (Blocked by walls)",
        "Satellite: Geosynchronous (36,000 km)",
        "Fiber: Total Internal Reflection"
    ])
    
    create_exam_booster_slide(
        prs, "M4.6", "Transmission Media", "K2 Understand",
        [
            "Compare Step-Index Multimode, Graded-Index Multimode, and Single-Mode optical fibers with refractive index profiles and light propagation paths. (8 Marks)",
            "Compare Twisted-Pair Cable, Coaxial Cable, and Optical Fiber across bandwidth, attenuation, EMI immunity, and cost. (7 Marks)",
            "Differentiate between Radio waves, Microwaves, and Infrared wireless media. (6 Marks)"
        ],
        [
            "Optical fibers provide immense bandwidth, zero EMI susceptibility, and ultra-low attenuation.",
            "Single-mode fiber eliminates modal dispersion for high-speed long-distance backbones.",
            "Microwaves require line-of-sight parabolic antennas; Infrared is safely contained by room walls."
        ]
    )
    return prs

def build_module_4_master(prs=None):
    """Builds the comprehensive master deck combining all Module 4 topics."""
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "MODULE 4 MASTER DECK", "Network Management & Physical Layer Fundamentals",
        "Complete Lecture Slides for KTU PCCST501 Computer Networks | Topics M4.1 through M4.6",
        "Module 4 Master"
    )
    build_m4_1(prs)
    build_m4_2(prs)
    build_m4_3(prs)
    build_m4_4(prs)
    build_m4_5(prs)
    build_m4_6(prs)
    return prs
