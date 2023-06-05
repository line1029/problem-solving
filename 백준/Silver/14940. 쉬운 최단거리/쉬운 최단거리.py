from sys import stdin, stdout
from collections import deque
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, m = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
for i, row in enumerate(grid):
    for j, num in enumerate(row):
        if num == 2:
            start = (i, j)
            break
    else:
        continue
    break
visited = [[0]*m for _ in range(n)]
visited[i][j] = 1
grid[i][j] = 0
q = deque([(i, j)])
while q:
    i, j = q.popleft()
    for di, dj in D:
        ni, nj = i + di, j + dj
        if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and grid[ni][nj]:
            visited[ni][nj] = 1
            grid[ni][nj] += grid[i][j]
            q.append((ni, nj))
for i, row in enumerate(grid):
    for j, num in enumerate(row):
        if num == 1 and visited[i][j] == 0:
            grid[i][j] = -1
stdout.write("\n".join(" ".join(map(str, row)) for row in grid))