# kruskal with union-find
from sys import stdin
import heapq
n = int(stdin.readline())
m = int(stdin.readline())
edges = list(map(lambda x: list(map(int, x.split()))[::-1], stdin.read().splitlines()))
heapq.heapify(edges)

parent = list(range(n+1))
rank = [0]*(n+1)
# using path-compression
def _find(x):
    if parent[x] != x:
        parent[x] = _find(parent[x])
        return parent[x]
    return x

# union by rank
def _union(x, y):
    x, y = _find(x), _find(y)
    if x == y:
        return False
    
    if rank[x] < rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[x] += 1
    parent[y] = x
    return True


ans = 0
while edges:
    c, b, a = heapq.heappop(edges)
    if _union(a, b):
        ans += c
print(ans)