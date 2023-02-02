from sys import stdin
from heapq import heappush, heappop
n, e = map(int, stdin.readline().split())
graph = [list() for _ in range(n+1)]
edges = list(map(lambda x: map(int, x.split()), stdin.read().splitlines()))
v1, v2 = edges.pop()
for a, b, w in edges:
    graph[a].append((b, w))
    graph[b].append((a, w))

def dijkstra(start, graph):
    dist = [float("inf")]*(n+1)
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

if v1 == 1 and v2 == n:
    dist = dijkstra(1, graph)
    ans = dist[n]
elif v1 == 1:
    dist1, dist2 = dijkstra(1, graph), dijkstra(v2, graph)
    ans = dist1[v2] + dist2[n]
elif v2 == n:
    dist1, dist2 = dijkstra(1, graph), dijkstra(v1, graph)
    ans = dist1[v1] + dist2[n]
else:
    dist1, dist2, dist3 = dijkstra(1, graph), dijkstra(v1, graph), dijkstra(v2, graph)
    ans = min(dist1[v1] + dist2[v2] + dist3[n], dist1[v2] + dist2[n] + dist3[v1])
if ans == float("inf"):
    print(-1)
else:
    print(ans)