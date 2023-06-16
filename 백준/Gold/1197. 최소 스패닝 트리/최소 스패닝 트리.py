from sys import stdin, setrecursionlimit
v, e = map(int, stdin.readline().split())
if v > 1000:
    setrecursionlimit(v + 2)
parent = list(range(v + 1))
rank = [0] * (v + 1)
def _find(x):
    if x != parent[x]:
        parent[x] = _find(parent[x])
    return parent[x]


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


edges = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()), key=lambda x: x[2])
ans = 0
for x, y, c in edges:
    if _union(x, y):
        ans += c

print(ans)
