from sys import stdin
from collections import deque
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, m = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
for i, row in enumerate(grid):
    for j, s in enumerate(row):
        if s == "I":
            start = (i, j)
            break
    else:
        continue
    break
q = deque([start])
visited = [[0]*m for _ in range(n)]
visited[i][j] = 1
ans = 0
while q:
    i, j = q.popleft()
    for di, dj in D:
        ni, nj = i + di, j + dj
        if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and grid[ni][nj] != "X":
            visited[ni][nj] = 1
            q.append((ni, nj))
            if grid[ni][nj] == "P":
                ans += 1
if ans:
    print(ans)
else:
    print("TT")