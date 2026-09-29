"""
ppts_module4.py
Topic-wise slide deck builders for Module 4: Network Management & Physical Layer Fundamentals
Author: Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET
"""

from generate_comprehensive_ppts import (
    init_prs, create_title_slide, create_content_slide, create_comparison_slide
)

def build_m4_1(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.1", "Network Management & SNMP Architecture",
        "Framework Components (NMS, Agent, MIB), SNMP Protocol Operations (UDP 161/162), Evolution: SNMPv1 vs SNMPv2c vs SNMPv3",
        "Module 4"
    )
    
    create_content_slide(prs, "4.1.1 Network Management Framework Components", "M4.1 SNMP FRAMEWORK", [
        ("Network Management Framework", "Consists of 4 fundamental components: Managing Entity, Managed Devices, Management Agents, and Management Information Base."),
        ("Managing Entity (NMS - Network Management System)", "Central workstation executing network management applications. Polls agents, receives alerts, and presents graphical dashboards."),
        ("Managed Device & Agent", "Routers, switches, servers running an SNMP Management Agent software module that collects local operational metrics and executes configuration commands."),
        ("Management Information Base (MIB)", "Hierarchical structured collection of managed object variables maintained inside each device (e.g., packets transmitted, CPU utilization, interface status)."),
        ("UDP Port Protocol Transport", "SNMP Manager sends requests to Agent on UDP Port 161; Agent sends unsolicited alerts (Traps) to Manager on UDP Port 162.")
    ], "SNMP Core Elements", [
        "NMS: Central manager console",
        "Agent: Software on managed node",
        "MIB: Device database variables",
        "Port 161 UDP: Requests (Get/Set)",
        "Port 162 UDP: Alerts (Traps/Inform)"
    ])
    
    create_content_slide(prs, "4.1.2 SNMP Protocol Operations", "M4.1 SNMP OPERATIONS", [
        ("`GetRequest`", "Manager requests value of one or more specific MIB variables by OID from Agent."),
        ("`GetNextRequest`", "Manager requests value of lexicographically next object in MIB tree (used for table traversal / walk)."),
        ("`GetBulkRequest` (SNMPv2/v3)", "Manager efficiently fetches large blocks of tabular data in a single PDU response, minimizing network roundtrips."),
        ("`SetRequest`", "Manager writes a new value to a MIB variable to reconfigure device state (e.g. enable/disable an interface)."),
        ("`Response`", "Agent replies to Manager with requested data values or error status."),
        ("`Trap` (Unsolicited Alert)", "Agent proactively sends alert to NMS reporting an asynchronous critical event (e.g. link down, power supply failure, authentication failure). Unacknowledged."),
        ("`InformRequest` (SNMPv2/v3)", "Manager-to-Manager or Agent-to-Manager acknowledged trap.")
    ], "Operation Summary", [
        "GetRequest: Fetch variable",
        "GetNextRequest: Tree traversal",
        "GetBulkRequest: Table retrieval",
        "SetRequest: Modify configuration",
        "Trap: Unsolicited async event",
        "InformRequest: Acknowledged trap"
    ])
    
    create_comparison_slide(prs, "4.1.3 Evolution of SNMP: SNMPv1 vs SNMPv2c vs SNMPv3", "M4.1 SNMP EVOLUTION",
        "SNMPv1 & SNMPv2c (Legacy)", [
            ("Authentication", "Plaintext Community Strings (`public` for read, `private` for write) transmitted in cleartext"),
            ("Security", "Vulnerable to packet sniffing, replay attacks, and unauthorized configuration modification"),
            ("Data Types", "v1: 32-bit counters only (rollover in 34s on 1 Gbps links!). v2c: Added 64-bit counters (`Counter64`) & `GetBulkRequest`")
        ],
        "SNMPv3 (Modern Standard - RFC 3411)", [
            ("User-based Security Model (USM)", "Provides Message Integrity (HMAC-MD5/SHA) and Confidentiality (DES/AES-128/256 payload encryption)"),
            ("View-based Access Control (VACM)", "Defines granular read/write access permissions per user group for specific MIB subtrees"),
            ("Anti-Replay", "Timestamps and boot counters prevent replaying captured SNMP packets")
        ]
    )
    
    return prs

def build_m4_2(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.2", "Abstract Syntax Notation One (ASN.1) & MIB-2",
        "ASN.1 Data Types, Basic Encoding Rules (BER) Tag-Length-Value Format, MIB-2 Tree Hierarchy & OID Structure",
        "Module 4"
    )
    
    create_content_slide(prs, "4.2.1 ASN.1 Data Types & BER Wire Encoding", "M4.2 ASN.1 & BER", [
        ("Role of ASN.1", "A formal, machine-independent language for specifying data types and structured messages independently of operating system hardware or byte-ordering conventions."),
        ("Primitive ASN.1 Data Types", "`INTEGER` (signed integer), `OCTET STRING` (byte sequence), `OBJECT IDENTIFIER` (dotted OID path), `BOOLEAN` (True/False), `NULL` (empty placeholder)."),
        ("Constructed ASN.1 Data Types", "`SEQUENCE` (ordered list of different types - like a C struct), `SEQUENCE OF` (ordered list of same type - like an array)."),
        ("Basic Encoding Rules (BER - TLV Format)", "Serializes ASN.1 objects into wire bytes as `[Tag | Length | Value]`."),
        ("BER Example", "Tag specifies data type (e.g. `0x02` for INTEGER), Length specifies payload byte count (e.g. `0x01`), Value contains actual data (e.g. `0x05` $\\implies$ `02 01 05` encodes integer 5).")
    ], "BER TLV Structure", [
        "Tag (Type): 1 Byte identifier",
        "Length: Byte count of Value",
        "Value: Actual binary payload",
        "02 01 05: INTEGER 5",
        "04 03 41 42 43: OCTET STRING 'ABC'"
    ])
    
    create_content_slide(prs, "4.2.2 Management Information Base (MIB-2) Tree & OIDs", "M4.2 MIB-2 HIERARCHY", [
        ("MIB-2 Tree Hierarchy", "All managed objects are organized into a globally unique hierarchical tree identified by dotted numeric Object Identifiers (OIDs)."),
        ("Standard Internet Root Path", "`iso(1) . org(3) . dod(6) . internet(1) . mgmt(2) . mib-2(1)` = `1.3.6.1.2.1`."),
        ("Key MIB-2 Functional Groups", "1. `system (1.3.6.1.2.1.1)`: Device name, description, uptime, contact."),
        ("2. `interfaces (1.3.6.1.2.1.2)`", "Number of interfaces, interface speed, MTU, packet counters (`ifInOctets`, `ifOutOctets`)."),
        ("3. `ip (1.3.6.1.2.1.4)` & `tcp (1.3.6.1.2.1.6)`", "IP routing table (`ipRouteTable`), forwarding counters, active TCP connection table (`tcpConnTable`).")
    ], "Key MIB OIDs", [
        "sysDescr: 1.3.6.1.2.1.1.1",
        "sysUpTime: 1.3.6.1.2.1.1.3",
        "ifNumber: 1.3.6.1.2.1.2.1",
        "ipForwarding: 1.3.6.1.2.1.4.1",
        "Scalar append .0: sysDescr.0"
    ])
    
    return prs

def build_m4_3(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.3", "Physical Layer: Data, Signals & Capacity Limits",
        "Analog vs Digital Signals, Fourier Decomposition, Transmission Impairments, Nyquist Bit Rate & Shannon Capacity Theorem",
        "Module 4"
    )
    
    create_content_slide(prs, "4.3.1 Data, Signals & Transmission Impairments", "M4.3 SIGNALS & IMPAIRMENTS", [
        ("Analog vs Digital Signals", "Analog: Continuous signal waveform over time with infinite voltage levels. Digital: Discrete discrete voltage levels representing binary 0s and 1s."),
        ("Fourier Harmonic Analysis", "Any periodic composite signal can be decomposed into an infinite series of fundamental and harmonic sine waves: $s(t) = \\frac{A_0}{2} + \\sum [A_n \\sin(2\\pi n f t) + B_n \\cos(2\\pi n f t)]$."),
        ("Transmission Impairment 1: Attenuation", "Loss of signal energy over transmission distance. Measured in decibels (dB): $\\text{dB} = 10 \\log_{10} \\left( \\frac{P_2}{P_1} \\right)$ (Negative dB = signal loss). Compensated by amplifiers / repeaters."),
        ("Transmission Impairment 2: Distortion", "Different harmonic frequency components travel at slightly different speeds in guided media, shifting relative phase and altering signal shape."),
        ("Transmission Impairment 3: Noise", "Thermal noise (Johnson noise: $N = kTB$), Induced noise, Crosstalk (coupling between adjacent wires), Impulse noise (sudden spikes).")
    ], "Decibel Formulas", [
        "Power: dB = 10 * log10(P2 / P1)",
        "Voltage: dB = 20 * log10(V2 / V1)",
        "Half power = -3 dB",
        "10x power = +10 dB",
        "100x power = +20 dB"
    ])
    
    create_comparison_slide(prs, "4.3.2 Channel Capacity Limits: Nyquist vs Shannon", "M4.3 THEORETICAL LIMITS",
        "Nyquist Bit Rate (Noiseless Channel)", [
            ("Condition", "Ideal noiseless channel of bandwidth $B$ Hz"),
            ("Signal Levels", "$L$ distinct discrete signal voltage levels"),
            ("Formula", "$\\text{Bit Rate} = 2 \\times B \\times \\log_2(L) \\text{ bps}$"),
            ("Example", "Bandwidth = 3000 Hz, $L = 2 \\implies \\text{Bit Rate} = 2 \\times 3000 \\times 1 = 6000 \\text{ bps}$"),
            ("Significance", "Upper bound determined strictly by bandwidth and modulation levels")
        ],
        "Shannon Capacity Theorem (Noisy Channel)", [
            ("Condition", "Real-world physical channel with Gaussian thermal noise"),
            ("Signal-to-Noise", "$\\text{SNR} = \\frac{\\text{Signal Power}}{\\text{Noise Power}}$ (Linear scale)"),
            ("Formula", "$\\text{Capacity } C = B \\times \\log_2(1 + \\text{SNR}) \\text{ bps}$"),
            ("Example", "$B = 3000\\text{ Hz}, \\text{SNR}_{\\text{dB}} = 30\\text{ dB} \\implies \\text{SNR} = 1000$ $\\implies C = 3000 \\times \\log_2(1001) \\approx 29,887\\text{ bps}$"),
            ("Significance", "Absolute theoretical upper bound regardless of signal levels $L$")
        ]
    )
    
    return prs

def build_m4_4(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.4", "Digital Transmission: Line Coding Techniques",
        "Baseband Transmission, Unipolar, Polar (NRZ-L, NRZ-I), Biphase (Manchester, Differential Manchester), Bipolar AMI & Block Codes",
        "Module 4"
    )
    
    create_comparison_slide(prs, "4.4.1 NRZ vs Biphase Manchester Line Coding", "M4.4 LINE CODING",
        "NRZ (Non-Return-to-Zero)", [
            ("NRZ-L (Level)", "Bit 0 = Positive voltage $+V$; Bit 1 = Negative voltage $-V$"),
            ("NRZ-I (Invert)", "Bit 1 = Transition at bit beginning; Bit 0 = No transition"),
            ("Drawback", "Significant DC component; baseline wander; loss of synchronization on consecutive 0s or 1s"),
            ("Bandwidth", "Low bandwidth ($B = N / 2$)")
        ],
        "Manchester & Differential Manchester (Self-Clocking)", [
            ("Manchester (IEEE 802.3)", "Bit 0 = High-to-Low mid-bit transition; Bit 1 = Low-to-High mid-bit transition"),
            ("Diff Manchester (802.5)", "Always mid-bit transition for clocking. Bit 0 = Transition at bit start; Bit 1 = No transition at start"),
            ("Advantage", "Guaranteed mid-bit transition gives perfect receiver clock synchronization and ZERO DC bias!"),
            ("Drawback", "Requires DOUBLE bandwidth ($B = N$)")
        ]
    )
    
    create_content_slide(prs, "4.4.2 Bipolar AMI, Block Coding & Scrambling", "M4.4 BIPOLAR & BLOCK CODES", [
        ("Bipolar AMI (Alternate Mark Inversion)", "Bit 0 = Zero volts ($0\\text{V}$). Bit 1 = Alternating positive ($+V$) and negative ($-V$) voltages. Eliminates DC component entirely; provides basic error detection (violating polarity rule = error)."),
        ("Loss of Sync on Zeros", "Long strings of consecutive 0s produce continuous $0\\text{V}$, causing receiver clock drift."),
        ("Scrambling (B8ZS & HDB3)", "B8ZS (North America T1): Replaces eight consecutive 0s with `000VB0VB` (where V=Bipolar Violation, B=Bipolar Rule). HDB3 (Europe E1): Replaces four consecutive 0s with `000V` or `B00V`."),
        ("Block Coding (4B/5B & 8B/10B)", "Converts 4-bit data nibbles into 5-bit codewords ensuring no more than three consecutive 0s ever occur, which are then transmitted using NRZ-I (Used in 100BASE-TX Fast Ethernet).")
    ], "Line Coding Summary", [
        "NRZ: Simple, DC bias issue",
        "Manchester: 802.3, self-clocking",
        "AMI: Alternates +V/-V on 1s",
        "B8ZS/HDB3: Scrambles long 0s",
        "4B/5B: Guarantees clock sync"
    ])
    
    return prs

def build_m4_5(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.5", "Analog Transmission & Bandwidth Utilization",
        "Digital-to-Analog Modulation (ASK, FSK, PSK, QAM), Multiplexing Techniques: FDM, WDM, Synchronous TDM & Statistical TDM",
        "Module 4"
    )
    
    create_comparison_slide(prs, "4.5.1 Digital-to-Analog Modulation Techniques", "M4.5 MODULATION METHODS",
        "Basic Shift Keying (ASK, FSK, PSK)", [
            ("ASK (Amplitude Shift Keying)", "Varies carrier amplitude: Bit 1 = High amplitude $A_1$; Bit 0 = Low amplitude $A_2$ (or 0 in OOK). Susceptible to noise"),
            ("FSK (Frequency Shift Keying)", "Varies carrier frequency: Bit 1 = Frequency $f_1$; Bit 0 = Frequency $f_2$"),
            ("BPSK (Binary Phase Shift Keying)", "Varies carrier phase: Bit 0 = $0^\\circ$ phase; Bit 1 = $180^\\circ$ phase. Highly robust against noise"),
            ("QPSK (Quadrature PSK)", "Uses 4 phase angles ($45^\\circ, 135^\\circ, 225^\\circ, 315^\\circ$) to transmit 2 bits per signal baud")
        ],
        "QAM (Quadrature Amplitude Modulation)", [
            ("Concept", "Combines Amplitude Shift Keying and Phase Shift Keying to pack multiple bits per baud"),
            ("16-QAM", "16 constellation points $\\implies 4 \\text{ bits per baud}$ ($2^4 = 16$)"),
            ("64-QAM / 256-QAM", "64 points (6 bits/baud) / 256 points (8 bits/baud); used in modern 4G/5G, Wi-Fi 6, and cable modems"),
            ("Bandwidth Efficiency", "Achieves massive bit rates over narrow RF channels")
        ]
    )
    
    create_content_slide(prs, "4.5.2 Multiplexing: FDM, WDM & Time Division Multiplexing", "M4.5 MULTIPLEXING", [
        ("Bandwidth Utilization Goal", "Combine multiple low-speed incoming data channels over a single high-capacity physical link."),
        ("Frequency Division Multiplexing (FDM)", "Analog technique. Divides total link bandwidth into separate non-overlapping frequency carrier bands separated by Guard Bands (Used in Radio, Cable TV, ADSL)."),
        ("Wavelength Division Multiplexing (WDM / DWDM)", "Optical multiplexing over fiber. Multiplexes multiple laser beams of different light wavelengths (colors) into a single fiber strand (Dense WDM carries $> 80$ channels of 100 Gbps each)."),
        ("Synchronous Time Division Multiplexing (TDM)", "Digital technique. Time divided into recurring frames; each frame contains fixed time slots pre-assigned to each input channel. Flaw: Wastes bandwidth if a channel has no data to send (idle slots)."),
        ("Statistical TDM (Asynchronous TDM)", "Time slots allocated dynamically on-demand only to active input channels carrying data. Eliminates wasted idle slots, dramatically increasing link utilization.")
    ], "Multiplexing Summary", [
        "FDM: Analog frequency bands",
        "WDM: Optical wavelengths in fiber",
        "Sync TDM: Fixed pre-assigned slots",
        "Stat TDM: Dynamic on-demand slots",
        "Guard Bands: Prevent interference"
    ])
    
    return prs

def build_m4_6(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "M4.6", "Transmission Media (Guided & Unguided)",
        "Guided Media (Twisted Pair UTP/STP, Coaxial, Optical Fiber Single/Multi-mode TIR), Unguided Wireless & Satellite Orbits",
        "Module 4"
    )
    
    create_comparison_slide(prs, "4.6.1 Guided Transmission Media: Copper vs Optical Fiber", "M4.6 GUIDED MEDIA",
        "Twisted Pair & Coaxial Cable (Copper)", [
            ("Unshielded Twisted Pair (UTP)", "Pairs twisted to cancel electromagnetic interference (EMI) and crosstalk. Cat 5e (1 Gbps / 100m), Cat 6/6A (10 Gbps / 55-100m). RJ-45 connector"),
            ("Shielded Twisted Pair (STP)", "Metal foil braid per pair for harsh industrial environments"),
            ("Coaxial Cable", "Central copper conductor surrounded by dielectric insulation, metallic braided shield, and jacket. 50$\\Omega$ Baseband / 75$\\Omega$ Broadband Cable TV")
        ],
        "Optical Fiber (Glass / Silica Core)", [
            ("Propagation Principle", "Total Internal Reflection (TIR) when light angle exceeds critical angle (Core refractive index $n_1 >$ Cladding $n_2$)"),
            ("Step-Index vs Graded-Index", "Step-Index: Constant core index. Graded-Index: Parabolic index profile reduces modal dispersion"),
            ("Single-Mode Fiber (SMF)", "Tiny core (8-10 $\\mu$m); zero modal dispersion; laser source; reach > 40 km"),
            ("Multi-Mode Fiber (MMF)", "Larger core (50-62.5 $\\mu$m); LED source; short reach (< 2 km) inside LANs/data centers"),
            ("Immense Advantages", "Immense bandwidth, zero electromagnetic interference (EMI), complete electrical isolation, low attenuation")
        ]
    )
    
    create_content_slide(prs, "4.6.2 Unguided Media (Wireless) & Satellite Orbits", "M4.6 UNGUIDED & SATELLITES", [
        ("Radio Waves (3 kHz to 1 GHz)", "Omnidirectional propagation (signals travel in all directions). Penetrates building walls easily. Used for AM/FM radio, cordless phones, and VHF television."),
        ("Microwaves (1 GHz to 300 GHz)", "Directional line-of-sight propagation using parabolic dish antennas. Cannot penetrate walls effectively; subject to rain attenuation (Used for terrestrial towers, radar, satellite)."),
        ("Infrared (300 GHz to 400 THz)", "High-frequency line-of-sight; cannot penetrate solid walls (prevents eavesdropping). Used for short-range TV remotes and wireless peripherals."),
        ("Geostationary Earth Orbit (GEO ~35,786 km)", "Orbital period matches Earth's rotation (24 hrs); fixed position above equator. High propagation delay (~250 ms one-way RTT $\\approx 500$ ms)."),
        ("Medium Earth Orbit (MEO ~2,000 to 20,000 km)", "Used by GPS constellations (24 satellites at ~20,200 km)."),
        ("Low Earth Orbit (LEO ~500 to 1,500 km)", "Low propagation delay (~20-40 ms RTT); requires mega-constellations of thousands of satellites (e.g. Starlink, OneWeb).")
    ], "Satellite Orbits", [
        "GEO: 35,786 km (High delay ~500ms)",
        "MEO: 20,200 km (GPS navigation)",
        "LEO: 500-1500 km (Low latency broadband)",
        "All KTU CO5 Topics Covered"
    ])
    
    return prs

def build_module_4_master(prs=None):
    if prs is None: prs = init_prs()
    create_title_slide(
        prs, "MODULE 4", "Network Management & Physical Layer Fundamentals",
        "Complete Lecture & Revision Master Deck (M4.1 to M4.6)",
        "Module 4 Complete"
    )
    build_m4_1(prs)
    build_m4_2(prs)
    build_m4_3(prs)
    build_m4_4(prs)
    build_m4_5(prs)
    build_m4_6(prs)
    return prs
