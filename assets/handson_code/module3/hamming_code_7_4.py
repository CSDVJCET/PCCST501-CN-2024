"""
PCCST501 Computer Networks - Module 3 Hands-on
Hamming (7,4) Error Detection and Correction Code
Demonstrates Parity bit calculation (Even Parity), syndrome calculation, and single-bit error auto-correction.
Author: Prof. Anju Markose | Dept. of CSE, VJCET
"""

def encode_hamming_7_4(data_bits_4):
    """
    Encodes a 4-bit data word (d3, d2, d1, d0) into a 7-bit Hamming codeword (p1, p2, d1, p3, d2, d3, d4).
    Positions:
    Bit 1 (P1), Bit 2 (P2), Bit 3 (D1), Bit 4 (P3), Bit 5 (D2), Bit 6 (D3), Bit 7 (D4)
    """
    assert len(data_bits_4) == 4, "Data must be exactly 4 bits"
    d = [int(b) for b in data_bits_4]
    d1, d2, d3, d4 = d[0], d[1], d[2], d[3]

    # Parity bit formulas (Even Parity):
    # P1 covers bits 1, 3, 5, 7 -> P1 ^ D1 ^ D2 ^ D4 = 0 => P1 = D1 ^ D2 ^ D4
    # P2 covers bits 2, 3, 6, 7 -> P2 ^ D1 ^ D3 ^ D4 = 0 => P2 = D1 ^ D3 ^ D4
    # P3 covers bits 4, 5, 6, 7 -> P3 ^ D2 ^ D3 ^ D4 = 0 => P3 = D2 ^ D3 ^ D4
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4

    codeword = [p1, p2, d1, p3, d2, d3, d4]
    return "".join(map(str, codeword))

def decode_and_correct(received_7_bits):
    """
    Calculates syndrome bits s1, s2, s3. If syndrome == 0 -> No error.
    Otherwise, syndrome value indicates the 1-indexed bit position of the single-bit error!
    """
    assert len(received_7_bits) == 7, "Received codeword must be 7 bits"
    r = [int(b) for b in received_7_bits]

    # Calculate Syndrome
    # S1 = r1 ^ r3 ^ r5 ^ r7
    # S2 = r2 ^ r3 ^ r6 ^ r7
    # S3 = r4 ^ r5 ^ r6 ^ r7
    s1 = r[0] ^ r[2] ^ r[4] ^ r[6]
    s2 = r[1] ^ r[2] ^ r[5] ^ r[6]
    s3 = r[3] ^ r[4] ^ r[5] ^ r[6]

    syndrome = (s3 << 2) | (s2 << 1) | s1
    corrected_bits = list(r)

    if syndrome == 0:
        status = "No Error Detected."
    else:
        status = f"Error detected at bit position #{syndrome} (1-indexed). Correcting..."
        # Invert corrupted bit
        error_idx = syndrome - 1
        corrected_bits[error_idx] = 1 - corrected_bits[error_idx]

    # Extract original 4 data bits: bits at positions 3, 5, 6, 7 (indices 2, 4, 5, 6)
    data_recovered = f"{corrected_bits[2]}{corrected_bits[4]}{corrected_bits[5]}{corrected_bits[6]}"
    return syndrome, "".join(map(str, corrected_bits)), data_recovered, status

def main():
    print("=====================================================")
    print("   Hamming (7,4) Single-Bit Error Correction Demo    ")
    print("=====================================================")

    data = "1011"
    encoded = encode_hamming_7_4(data)
    print(f"Original 4-bit Data Word: {data}")
    print(f"Encoded 7-bit Codeword  : {encoded}")

    print("\n--- Scenario 1: Clean Transmission ---")
    syn, corr, recovered, stat = decode_and_correct(encoded)
    print(f"Status                  : {stat}")
    print(f"Syndrome (Error Index)  : {syn}")
    print(f"Recovered Data Word     : {recovered}")

    print("\n--- Scenario 2: Bit 5 Corrupted in Transit ---")
    corrupted = list(encoded)
    corrupted[4] = '1' if corrupted[4] == '0' else '0' # Flip bit 5
    corrupted_str = "".join(corrupted)
    print(f"Corrupted Received Bits : {corrupted_str}")

    syn, corr, recovered, stat = decode_and_correct(corrupted_str)
    print(f"Status                  : {stat}")
    print(f"Syndrome (Error Index)  : Bit #{syn}")
    print(f"Corrected Codeword      : {corr}")
    print(f"Recovered Data Word     : {recovered} (Successfully Corrected!)")

if __name__ == "__main__":
    main()
