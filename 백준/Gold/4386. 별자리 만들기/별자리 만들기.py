from sys import stdin
def get_dist(a, b):
    a, b = stars[a], stars[b]
    res = sum((i - j)**2 for i, j in zip(a, b))
    return res**.5
n = int(stdin.readline())
stars = list(map(lambda x: list(map(float, x.split())), stdin.read().splitlines()))
edges = []
for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((get_dist(i, j), i, j))
edges.sort()
parent = list(range(n))
rank = [0]*n
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return False
    if rank[x] < rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[x] += 1
    parent[y] = x
    return True

ans = 0.
for e, a, b in edges:
    if union(a, b):
        ans += e
print(ans)