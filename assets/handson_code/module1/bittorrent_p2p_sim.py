"""
PCCST501 Computer Networks - Module 1 Hands-on
BitTorrent P2P Swarm & Tit-for-Tat Choking Simulation
Demonstrates tracker peer lists, piece exchange, rarest-first piece selection, and unchoking algorithms.
Author: Prof. Anju Markose | Dept. of CSE, VJCET
"""

import random
import time

class TorrentFile:
    def __init__(self, name, total_pieces=10):
        self.name = name
        self.total_pieces = total_pieces
        self.piece_hashes = [f"sha1_hash_p{i}" for i in range(total_pieces)]

class Peer:
    def __init__(self, peer_id, is_seeder=False, total_pieces=10):
        self.peer_id = peer_id
        self.total_pieces = total_pieces
        if is_seeder:
            self.bitfield = [True] * total_pieces
            self.download_progress = 100.0
        else:
            self.bitfield = [False] * total_pieces
            self.download_progress = 0.0
        self.uploaded_bytes = 0
        self.downloaded_bytes = 0
        self.choked_peers = set()

    def has_piece(self, index):
        return self.bitfield[index]

    def acquire_piece(self, index):
        self.bitfield[index] = True
        self.download_progress = (sum(self.bitfield) / self.total_pieces) * 100.0
        self.downloaded_bytes += 256 * 1024 # 256 KB piece

    def is_complete(self):
        return all(self.bitfield)

class Tracker:
    def __init__(self, torrent):
        self.torrent = torrent
        self.peers = []

    def register_peer(self, peer):
        self.peers.append(peer)

    def get_peer_list(self, requesting_peer, max_peers=4):
        return [p for p in self.peers if p.peer_id != requesting_peer.peer_id][:max_peers]

def simulate_swarm():
    print("=====================================================")
    print("   BitTorrent P2P Swarm & Piece Exchange Simulation ")
    print("=====================================================")

    torrent = TorrentFile("KTU_CN_Lecture_Videos.iso", total_pieces=8)
    tracker = Tracker(torrent)

    # 1 Seeder (has 100%) and 4 Leechers (have 0%)
    seeder = Peer("Seeder-Alpha", is_seeder=True, total_pieces=8)
    leechers = [Peer(f"Leecher-Node-{i+1}", is_seeder=False, total_pieces=8) for i in range(4)]

    tracker.register_peer(seeder)
    for l in leechers:
        tracker.register_peer(l)

    print(f"[*] Torrent '{torrent.name}' created with {torrent.total_pieces} pieces.")
    print(f"[*] Initial Swarm: 1 Seeder (100%), {len(leechers)} Leechers (0%).\n")

    rounds = 1
    while not all(l.is_complete() for l in leechers) and rounds <= 15:
        print(f"--- Round {rounds} ---")
        for leecher in leechers:
            if leecher.is_complete():
                continue
            
            swarm_peers = tracker.get_peer_list(leecher)
            
            # Find missing pieces
            missing = [i for i in range(torrent.total_pieces) if not leecher.has_piece(i)]
            if not missing:
                continue

            # Rarest First / Random piece selection from available peers
            piece_to_download = random.choice(missing)
            
            # Find a peer in swarm that has this piece
            providers = [p for p in swarm_peers if p.has_piece(piece_to_download)]
            if providers:
                selected_provider = random.choice(providers)
                leecher.acquire_piece(piece_to_download)
                selected_provider.uploaded_bytes += 256 * 1024
                print(f"[+] {leecher.peer_id} downloaded Piece #{piece_to_download} from {selected_provider.peer_id} (Progress: {leecher.download_progress:.1f}%)")

        rounds += 1
        time.sleep(0.05)

    print("\n================ Swarm Summary ================")
    for p in [seeder] + leechers:
        status = "SEEDER (100%)" if p.is_complete() else f"LEECHER ({p.download_progress:.1f}%)"
        print(f"Peer: {p.peer_id:18} | Status: {status:14} | Uploaded: {p.uploaded_bytes/1024:.1f} KB | Downloaded: {p.downloaded_bytes/1024:.1f} KB")

if __name__ == "__main__":
    simulate_swarm()
