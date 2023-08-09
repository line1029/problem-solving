from sys import stdin
from collections import deque
D = ((0, 1), (0, -1), (1, 0), (-1, 0))
INF = 1000001
n, m, k = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
visited = [0]*(m*n)
steps = [INF]*(m*n)
steps[0] = 0
q = deque([[0, 0, 0, 0]])
while q:
    i, j, step, eli = q.popleft()
    for di, dj in D:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            if grid[ni][nj] == "1":
                if eli == k or (visited[ni*m + nj] & ((1 << (eli + 2)) - 1)): continue
                visited[ni*m + nj] |= (1 << (eli + 1))
                if steps[ni*m + nj] == INF:
                    steps[ni*m + nj] = step + 1
                q.append([ni, nj, step + 1, eli + 1])
            else:
                if (visited[ni*m + nj] & ((1 << (eli + 1)) - 1)): continue
                visited[ni*m + nj] |= (1 << eli)
                if steps[ni*m + nj] == INF:
                    steps[ni*m + nj] = step + 1
                q.append([ni, nj, step + 1, eli])
if steps[-1] != INF:
    print(steps[-1] + 1)
else:
    print(-1)
