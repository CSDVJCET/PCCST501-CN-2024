"""
PCCST501 Computer Networks - Module 4 Hands-on
Channel Capacity & Data Rate Calculator (Nyquist & Shannon Theorems)
Demonstrates Noiseless Nyquist Bit Rate vs Noisy Shannon Channel Capacity calculations.
Author: Prof. Anju Markose | Dept. of CSE, VJCET
"""

import math

def nyquist_bit_rate(bandwidth_hz, signal_levels):
    """
    Nyquist Formula for Noiseless Channel:
    BitRate = 2 * B * log2(L) bps
    """
    bit_rate = 2 * bandwidth_hz * math.log2(signal_levels)
    return bit_rate

def shannon_capacity_from_snr_linear(bandwidth_hz, snr_linear):
    """
    Shannon Capacity for Noisy Channel:
    Capacity (C) = B * log2(1 + SNR) bps
    """
    capacity = bandwidth_hz * math.log2(1 + snr_linear)
    return capacity

def shannon_capacity_from_snr_db(bandwidth_hz, snr_db):
    """
    SNR_linear = 10 ^ (SNR_dB / 10)
    """
    snr_linear = 10 ** (snr_db / 10.0)
    capacity = shannon_capacity_from_snr_linear(bandwidth_hz, snr_linear)
    return capacity, snr_linear

def main():
    print("================================================================")
    print("   Nyquist & Shannon Channel Capacity Analysis Utility          ")
    print("================================================================\n")

    # Example 1: Standard Telephone Channel (Bandwidth = 3000 Hz, SNR = 3162 (approx 35 dB))
    bw_voice = 3000
    snr_db_voice = 30
    cap_voice, snr_lin = shannon_capacity_from_snr_db(bw_voice, snr_db_voice)
    print(f"--- Example 1: Voice-grade Telephone Line ---")
    print(f"Bandwidth (B)             : {bw_voice} Hz (3 kHz)")
    print(f"Signal-to-Noise Ratio     : {snr_db_voice} dB (Linear: {snr_lin:.1f})")
    print(f"Theoretical Max Capacity  : {cap_voice:.2f} bps ({cap_voice/1000:.2f} kbps)")

    # Example 2: Noiseless Channel with Multilevel Signaling
    bw = 1000000 # 1 MHz
    levels = [2, 4, 8, 16, 64, 256]
    print(f"\n--- Example 2: Noiseless 1 MHz Channel (Nyquist Rate) ---")
    print(f"{'Signal Levels (L)':20} | {'Bits / Signal Element':25} | {'Nyquist Max Bit Rate':20}")
    print("-" * 70)
    for L in levels:
        bits_per_element = int(math.log2(L))
        rate = nyquist_bit_rate(bw, L)
        print(f"{L:<20} | {bits_per_element:<25} | {rate/1e6:.2f} Mbps")

if __name__ == "__main__":
    main()
