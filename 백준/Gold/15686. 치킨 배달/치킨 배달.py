from sys import stdin
from itertools import combinations
from collections import deque
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, m = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
c = [(i, j) for j in range(n) for i in range(n) if grid[i][j] == 2]
h = [(i, j) for j in range(n) for i in range(n) if grid[i][j] == 1]
ans = 10000
for p in combinations(c, m):
    q = deque(p)
    dist = [[0]*n for _ in range(n)]
    t = 1
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in D:
                ni, nj = i + di, j + dj
                if 0<=ni<n and 0<=nj<n and not dist[ni][nj]:
                    dist[ni][nj] = t
                    q.append((ni, nj))
        t += 1
    ans = min(ans, sum(dist[i][j] for i , j in h))
print(ans)
