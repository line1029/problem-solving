from sys import stdin
n, m = map(int, stdin.readline().split())
edges = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()), key=lambda x: x[2])
parent = list(range(n + 1))
rank = [0]*(n + 1)
def _find(x):
    if parent[x] != x:
        parent[x] = _find(parent[x])
    return parent[x]


def _union(x, y):
    x, y = _find(x), _find(y)
    if x == y:
        return False
    if x < y:
        x, y = y, x
    if x == y:
        rank[x] += 1
    parent[y] = x
    return True

cnt = 1
ans = 0
for a, b, c in edges:
    if _union(a, b):
        cnt += 1
        if cnt == n:
            break
        ans += c
print(ans)