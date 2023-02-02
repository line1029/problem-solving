from sys import stdin
from heapq import heappop, heappush
n = int(stdin.readline())
m = int(stdin.readline())
edges = list(map(lambda x: map(int, x.split()), stdin.read().splitlines()))
a, b = edges.pop()
graph = [[] for _ in range(n+1)]
for s, e, w in edges:
    graph[s].append((e, w))

def dijkstra(start, end, graph):
    dist = [float("inf")]*len(graph)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_cost, cur_node = heappop(pq)
        if dist[cur_node] < cur_cost:
            continue
        for nex_node, weight in graph[cur_node]:
            nex_cost = cur_cost + weight
            if nex_cost < dist[nex_node]:
                dist[nex_node] = nex_cost
                heappush(pq, (nex_cost, nex_node))
    return dist[end]

print(dijkstra(a, b, graph))
