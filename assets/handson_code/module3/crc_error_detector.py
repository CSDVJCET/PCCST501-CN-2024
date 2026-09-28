"""
PCCST501 Computer Networks - Module 3 Hands-on
Cyclic Redundancy Check (CRC) Generator & Error Detector
Demonstrates Modulo-2 binary division, CRC-CCITT / CRC-8 generation, and error detection verification.
Author: Prof. Anju Markose | Dept. of CSE, VJCET
"""

def xor(a, b):
    # Perform XOR between two binary bit strings
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    # Number of bits to be XORed at a time
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    # For the last n bits
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp

def generate_crc(data_bits, generator_polynomial):
    l_key = len(generator_polynomial)
    # Append (l_key - 1) zeros to data bits
    appended_data = data_bits + '0' * (l_key - 1)
    remainder = mod2div(appended_data, generator_polynomial)
    codeword = data_bits + remainder
    return remainder, codeword

def verify_crc(received_codeword, generator_polynomial):
    remainder = mod2div(received_codeword, generator_polynomial)
    # If remainder is all zeros, data is intact
    is_valid = set(remainder) == {'0'} or remainder == ""
    return is_valid, remainder

def main():
    print("=====================================================")
    print("   Cyclic Redundancy Check (CRC) Generator & Verifier")
    print("=====================================================")

    data = "11010011101100" # Example Data Word
    generator = "1011"       # Example Generator Polynomial: x^3 + x + 1 (CRC-3)
    
    print(f"Original Data Bits (D)     : {data}")
    print(f"Generator Polynomial (G)   : {generator} (Degree = {len(generator)-1})")

    remainder, codeword = generate_crc(data, generator)
    print(f"Calculated CRC Checksum (R): {remainder}")
    print(f"Transmitted Codeword (T)   : {codeword}")

    print("\n--- Receiver Verification (No Transmission Error) ---")
    valid, rem = verify_crc(codeword, generator)
    print(f"Receiver Remainder         : {rem}")
    print(f"Data Accepted / Error-Free : {valid}")

    print("\n--- Receiver Verification (With 1-Bit Error Injected) ---")
    # Invert 4th bit
    corrupted_codeword = list(codeword)
    corrupted_codeword[3] = '1' if corrupted_codeword[3] == '0' else '0'
    corrupted_codeword = "".join(corrupted_codeword)
    print(f"Corrupted Codeword Received: {corrupted_codeword}")
    valid, rem = verify_crc(corrupted_codeword, generator)
    print(f"Receiver Remainder         : {rem}")
    print(f"Data Accepted / Error-Free : {valid} (ERROR DETECTED!)")

if __name__ == "__main__":
    main()
