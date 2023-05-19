# kruskal with union-find
from sys import stdin
import heapq
from collections import defaultdict
n = int(stdin.readline())
m = int(stdin.readline())
edges = list(map(lambda x: list(map(int, x.split()))[::-1], stdin.read().splitlines()))
heapq.heapify(edges)

parent = dict()
rank = defaultdict(int)
# using path-splitting
def _find(x):
    if parent[x] != x:
        parent[x] = _find(parent[x])
        return parent[x]
    return x


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
    if b not in parent:
        parent[b] = b
    if a not in parent:
        parent[a] = a
    if _union(a, b):
        ans += c
print(ans)