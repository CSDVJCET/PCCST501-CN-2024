"""
PCCST501 Computer Networks - Module 4 Hands-on
Digital Line Coding Techniques Visualizer
Generates signal waveforms for NRZ-L, NRZ-I, Manchester, Differential Manchester, and AMI.
Author: Prof. Anju Markose | Dept. of CSE, VJCET
"""

def generate_nrz_l(bits):
    # NRZ-L: 0 = +V, 1 = -V (or 0 = Low, 1 = High depending on convention)
    # Standard: 0 -> High (+1), 1 -> Low (-1)
    levels = []
    for b in bits:
        levels.append("+V" if b == '0' else "-V")
    return levels

def generate_nrz_i(bits):
    # NRZ-I: Inversion on bit 1, no transition on bit 0
    current = "+V"
    levels = []
    for b in bits:
        if b == '1':
            current = "-V" if current == "+V" else "+V"
        levels.append(current)
    return levels

def generate_manchester(bits):
    # Manchester (IEEE 802.3): 0 = High-to-Low (+V, -V), 1 = Low-to-High (-V, +V)
    transitions = []
    for b in bits:
        if b == '0':
            transitions.append("+V -> -V")
        else:
            transitions.append("-V -> +V")
    return transitions

def generate_diff_manchester(bits):
    # Diff Manchester: Bit 0 = Transition at start, Bit 1 = No transition at start (always mid-bit transition)
    transitions = []
    current_start = "-V"
    for b in bits:
        if b == '0':
            current_start = "+V" if current_start == "-V" else "-V"
        mid = "-V" if current_start == "+V" else "+V"
        transitions.append(f"{current_start} -> {mid}")
        current_start = mid # next start depends on ending
    return transitions

def generate_ami(bits):
    # AMI (Alternate Mark Inversion): 0 = 0V, 1 = alternating +V and -V
    levels = []
    last_mark = "-V"
    for b in bits:
        if b == '0':
            levels.append(" 0V")
        else:
            last_mark = "+V" if last_mark == "-V" else "-V"
            levels.append(last_mark)
    return levels

def print_ascii_waveform(bits):
    print("=================================================================")
    print(f"      Digital Line Coding Waveforms for Bit Sequence: {bits}")
    print("=================================================================\n")

    print(f"Input Bit Stream          : {'   '.join(list(bits))}")
    print("-" * 65)

    nrz_l = generate_nrz_l(bits)
    print(f"NRZ-L (Level)             : {' | '.join(nrz_l)}")

    nrz_i = generate_nrz_i(bits)
    print(f"NRZ-I (Invert on 1)       : {' | '.join(nrz_i)}")

    ami = generate_ami(bits)
    print(f"AMI (Bipolar Alternate)   : {' | '.join(ami)}")

    manchester = generate_manchester(bits)
    print(f"Manchester (802.3)        : {' | '.join(manchester)}")

    diff_man = generate_diff_manchester(bits)
    print(f"Diff. Manchester          : {' | '.join(diff_man)}")
    print("=" * 65)

def main():
    test_stream = "01001110"
    print_ascii_waveform(test_stream)

if __name__ == "__main__":
    main()
