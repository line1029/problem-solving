from sys import stdin
from collections import defaultdict
n = int(stdin.readline())
grid = list(map(lambda x: list(x.strip()), stdin.readlines()))
parent = dict()
rank = defaultdict(int)
def _union(x, y):
    xi, xj = x
    yi, yj = y
    if grid[xi][xj] != grid[yi][yj]:
        return 0
    x, y = _find(x), _find(y)
    if x == y:
        return 0
    if rank[x] < rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[x] += 1
    parent[y] = x
    return 1
def _find(x):
    if x != parent[x]:
        parent[x] = _find(parent[x])
    return parent[x]
direc = ((0, -1), (-1, 0))
cnt = 0
for i in range(n):
    for j in range(n):
        parent[(i, j)] = (i, j)
        cnt += 1
        for di, dj in direc:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n:
                cnt -= _union((i, j), (ni, nj))
print(cnt)
parent.clear()
rank.clear()
cnt = 0
for i in range(n):
    for j in range(n):
        parent[(i, j)] = (i, j)
        cnt += 1
        if grid[i][j] == "G":
            grid[i][j] = "R"
        for di, dj in direc:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n:
                cnt -= _union((i, j), (ni, nj))
print(cnt)