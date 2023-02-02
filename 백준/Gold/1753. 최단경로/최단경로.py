from sys import stdin, stdout
from itertools import islice
from heapq import heappush, heappop
v, e = map(int, stdin.readline().split())
k = int(stdin.readline())
graph = [list() for _ in range(v+1)]
edges = map(lambda x: map(int, x.split()), stdin.read().splitlines())
for a, b, w in edges:
    graph[a].append((b, w))

def dijkstra(start, graph):
    dist = [float("inf")]*(v+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_cost, cur_node = heappop(pq)
        if dist[cur_node] < cur_cost:
            continue
        for nex_node, weight in graph[cur_node]:
            nex_cost = weight + cur_cost
            if nex_cost < dist[nex_node]:
                dist[nex_node] = nex_cost
                heappush(pq, (nex_cost, nex_node))
    return dist

dist = dijkstra(k, graph)
for i in islice(dist, 1, None):
    if isinstance(i, int):
        stdout.write(f"{i}\n")
    else:
        stdout.write("INF\n")