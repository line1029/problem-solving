from sys import stdin
from collections import deque
D = ((0, 1), (0, -1), (1, 0), (-1, 0))
INF = 1000001
n, m, k = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
visited = [[[INF, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 0
q = deque([[0, 0, 0, 0]])
while q:
    i, j, step, eli = q.popleft()
    for di, dj in D:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            if grid[ni][nj] == "1":
                if eli == k or (visited[ni][nj][1] & ((1 << (eli + 2)) - 1)): continue
                visited[ni][nj][1] |= (1 << (eli + 1))
                if visited[ni][nj][0] == INF:
                    visited[ni][nj][0] = step + 1
                q.append([ni, nj, step + 1, eli + 1])
            else:
                if (visited[ni][nj][1] & ((1 << (eli + 1)) - 1)): continue
                visited[ni][nj][1] |= (1 << eli)
                if visited[ni][nj][0] == INF:
                    visited[ni][nj][0] = step + 1
                q.append([ni, nj, step + 1, eli])
if visited[-1][-1][0] != INF:
    print(visited[-1][-1][0] + 1)
else:
    print(-1)
