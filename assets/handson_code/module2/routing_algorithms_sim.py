"""
PCCST501 Computer Networks - Module 2 Hands-on
Dijkstra Link-State (OSPF) & Bellman-Ford Distance Vector (RIP) Routing Algorithms
Demonstrates shortest path computation and routing table convergence.
Author: Prof. Anju Markose | Dept. of CSE, VJCET
"""

import heapq

def dijkstra_link_state(graph, source_node):
    print(f"\n=======================================================")
    print(f"   Dijkstra's Link-State (OSPF) Shortest Path Tree    ")
    print(f"   Source Node: {source_node}                         ")
    print(f"=======================================================")
    
    distances = {node: float('inf') for node in graph}
    distances[source_node] = 0
    previous = {node: None for node in graph}
    priority_queue = [(0, source_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    print(f"{'Destination':15} | {'Cost (Metric)':15} | {'Full Path':25}")
    print("-" * 60)
    for destination in sorted(graph.keys()):
        # reconstruct path
        path = []
        curr = destination
        while curr is not None:
            path.append(curr)
            curr = previous[curr]
        path.reverse()
        path_str = " -> ".join(path)
        print(f"{destination:15} | {distances[destination]:<15} | {path_str:25}")

def bellman_ford_distance_vector(nodes, edges, source_node):
    print(f"\n=======================================================")
    print(f"   Bellman-Ford Distance Vector (RIP) Routing Table    ")
    print(f"   Source Node: {source_node}                         ")
    print(f"=======================================================")
    
    distance = {node: float('inf') for node in nodes}
    distance[source_node] = 0
    next_hop = {node: None for node in nodes}

    # Relax edges |V| - 1 times
    for _ in range(len(nodes) - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                next_hop[v] = u if next_hop[u] is None and u != source_node else (next_hop[u] or v)
            if distance[v] != float('inf') and distance[v] + w < distance[u]:
                distance[u] = distance[v] + w
                next_hop[u] = v if next_hop[v] is None and v != source_node else (next_hop[v] or u)

    print(f"{'Destination':15} | {'Cost (Hops)':15} | {'Next Hop':15}")
    print("-" * 50)
    for n in sorted(nodes):
        hop = next_hop[n] if n != source_node else "Direct (Local)"
        print(f"{n:15} | {distance[n]:<15} | {str(hop):15}")

def main():
    # Network Topology Graph
    network_graph = {
        'Router-A': {'Router-B': 2, 'Router-C': 5, 'Router-D': 1},
        'Router-B': {'Router-A': 2, 'Router-C': 3, 'Router-E': 2},
        'Router-C': {'Router-A': 5, 'Router-B': 3, 'Router-D': 3, 'Router-E': 1, 'Router-F': 5},
        'Router-D': {'Router-A': 1, 'Router-C': 3, 'Router-F': 8},
        'Router-E': {'Router-B': 2, 'Router-C': 1, 'Router-F': 2},
        'Router-F': {'Router-C': 5, 'Router-D': 8, 'Router-E': 2}
    }

    dijkstra_link_state(network_graph, 'Router-A')

    # Edge list for Distance Vector
    nodes = list(network_graph.keys())
    edges = []
    for u in network_graph:
        for v, w in network_graph[u].items():
            if (v, u, w) not in edges:
                edges.append((u, v, w))

    bellman_ford_distance_vector(nodes, edges, 'Router-A')

if __name__ == "__main__":
    main()
