from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
visited = [[[0, 0] for _ in range(m)] for __ in range(n)]
visited[0][0] = [1, 1]
direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
q = deque([(0, 0, 0)])
while q:
    i, j, broke = q.popleft()
    for di, dj in direction:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj][broke] == 0:
            if not broke and grid[ni][nj] == "0":
                visited[ni][nj][0] = visited[i][j][0] + 1
                if not visited[ni][nj][1]:
                    visited[ni][nj][1] = visited[i][j][0] + 1
                q.append((ni, nj, 0))
            elif not broke and grid[ni][nj] == "1":
                visited[ni][nj][1] = visited[i][j][0] + 1
                q.append((ni, nj, 1))
            elif broke and grid[ni][nj] == "0":
                visited[ni][nj][1] = visited[i][j][1] + 1
                q.append((ni, nj, 1))
if visited[-1][-1][1] == 0:
    print(-1)
else:
    print(visited[-1][-1][1])