from sys import stdin
from itertools import product
UD = ((-1, 0), (0, -1))
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, m = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
parent, rank = {x:x for x in product(range(n), range(m))}, {x:0 for x in product(range(n), range(m))}
def _find(x):
    if parent[x] != x:
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

candidates = set()
for i, row in enumerate(grid):
    for j, num in enumerate(row):
        if num:
            candidates.add((i, j))
        else:
            for di, dj in UD:
                ni, nj = i + di, j + dj
                if 0<=ni and 0<=nj and not grid[ni][nj]:
                    _union((ni, nj), (i, j))
ans = 0
while candidates:
    ans += 1
    tmp = []
    root = _find((0, 0))
    for i, j in list(candidates):
        tmp_cnt = 0
        for di, dj in D:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<m and grid[ni][nj]==0 and _find((ni, nj))==root:
                tmp_cnt += 1
                if tmp_cnt >= 2:
                    tmp.append((i, j))
                    break
    for i, j in tmp:
        grid[i][j] = 0
        for di, dj in D:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<m and grid[ni][nj]==0:
                _union((ni, nj), (i, j))
        candidates.discard((i, j))
print(ans)
    