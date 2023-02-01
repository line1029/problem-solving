from sys import stdin
from itertools import islice
n, m = map(int, stdin.readline().split())
truth = set(islice(map(int, stdin.readline().split()), 1, None))
parent = [-1]*(n+1)
rank = [0]*(n+1)
visited = [0]*(n+1)

def _find(x):
    if x != parent[x]:
        parent[x] = _find(parent[x])
    return parent[x]


def _union(x, y):
    x, y = _find(x), _find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[x] += 1
    parent[y] = x
    return

party = []
for _ in range(m):
    _, first, *others = map(int, stdin.readline().split())
    party.append(first)
    if not visited[first]:
        parent[first] = first
        visited[first] = 1
    for another in others:
        if not visited[another]:
            parent[another] = first
            visited[another] = 1
        _union(first, another)


cant = set()
for i in range(1, n+1):
    if visited[i] and i in truth:
        cant.add(_find(i))
ans = 0
for i in party:
    if _find(i) not in cant:
        ans += 1
print(ans)


