from sys import stdin
from heapq import heappush, heappop
n, m, x = map(int, stdin.readline().split())
edges = map(lambda x: map(int, x.split()), stdin.read().splitlines())
graph = [list() for _ in range(n+1)]
graph_rev = [list() for _ in range(n+1)]
for node1, node2, dist in edges:
    graph[node1].append((node2, dist))
    graph_rev[node2].append((node1, dist))

def dijkstra(start, graph):
    dist = [10000001]*(n+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_cost, cur_node = heappop(pq)
        if cur_cost > dist[cur_node]:
            continue
        for nex_node, weight in graph[cur_node]:
            nex_cost = cur_cost + weight
            if nex_cost < dist[nex_node]:
                heappush(pq, (nex_cost, nex_node))
                dist[nex_node] = nex_cost
    return dist

dist, dist_rev = dijkstra(x, graph), dijkstra(x, graph_rev)
dist[0], dist_rev[0] = 0, 0
print(max(i+j for i, j in zip(dist, dist_rev)))