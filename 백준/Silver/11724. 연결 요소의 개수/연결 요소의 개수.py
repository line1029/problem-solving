from sys import stdin
n, m = map(int, stdin.readline().split())
edges = map(lambda x: tuple(map(int, x.split())), stdin.read().splitlines())
parent = list(range(n+1))
rank = [0]*(n+1)
def _union(x, y):
    x, y = _find(x), _find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[x] += 1
    parent[y] = x
def _find(x):
    if x != parent[x]:
        parent[x] = _find(parent[x])
    return parent[x]
for n1, n2 in edges:
    _union(n1, n2)

for i in range(1, n+1):
    _find(i)
print(len(set(parent)) - 1)