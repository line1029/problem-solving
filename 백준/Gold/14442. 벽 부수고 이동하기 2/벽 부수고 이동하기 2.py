from sys import stdin
from collections import deque
D = ((0, 1), (0, -1), (1, 0), (-1, 0))
INF = 1000001
n, m, k = map(int, stdin.readline().split())
if n == m == 1:
    print(1)
    exit()
grid = []
for _ in range(n):
    grid.extend(map(int, stdin.readline().strip()))
visited = [k + 1]*(m*n)
q = deque([[0, 0, 0]])
for step in range(m*n + 1):
    if not q:
        break
    for _ in range(len(q)):
        i, j, eli = q.popleft()
        for di, dj in D:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if eli + grid[ni*m + nj] > k: continue
                if visited[ni*m + nj] > eli + grid[ni*m + nj]:
                    if ni == n - 1 and nj == m - 1:
                        print(step + 2)
                        exit()
                    visited[ni*m + nj] = eli + grid[ni*m + nj]
                    q.append((ni, nj, eli + grid[ni*m + nj]))
print(-1)