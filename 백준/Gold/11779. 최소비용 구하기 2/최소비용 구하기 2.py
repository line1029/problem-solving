from sys import stdin
from heapq import heappush, heappop
n = int(stdin.readline())
m = int(stdin.readline())
inf = int(1e9) + 1
graph = [[] for _ in range(n + 1)]
dist = [inf]*(n + 1)
path = [-1]*(n + 1)
edges = stdin.read().splitlines()
start, end = map(int, edges.pop().split())
dist[start] = 0
for a, b, w in map(lambda x: map(int, x.split()), edges):
    graph[a].append((b, w))
pq = [(0, start)]
while pq:
    d, cur = heappop(pq)
    if cur == end:
        break
    if d > dist[cur]:
        continue
    for nex, w in graph[cur]:
        if d + w < dist[nex]:
            dist[nex] = d + w
            path[nex] = cur
            heappush(pq, (d + w, nex))
print(dist[end])
ans = []
node = end
while node != -1:
    ans.append(node)
    node = path[node]
print(len(ans))
print(" ".join(map(str, reversed(ans))))