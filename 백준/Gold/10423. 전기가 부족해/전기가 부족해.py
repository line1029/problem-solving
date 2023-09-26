# kruskal
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, m, k = map(int, input().split())
parent = list(range(n + 1))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return False
    if x < y:
        x, y = y, x
    parent[x] = y
    return True

ans = 0
for i in map(int, input().split()):
    parent[i] = 0
for u, v, w in sorted((list(map(int, input().split())) for _ in range(m)), key=lambda x: x[2]):
    if union(u, v):
        ans += w
print(ans)
