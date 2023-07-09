from sys import stdin, stdout
from collections import deque
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, m = map(int, stdin.readline().split())
visited = [[0]*m for _ in range(n)]
area = [0]*(m*n+1)
grid = list(map(lambda x: list(map(int, x)), stdin.read().splitlines()))
k = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j] and not grid[i][j]:
            visited[i][j] = k
            q = deque([(i, j)])
            cnt = 0
            while q:
                x, y = q.popleft()
                cnt += 1
                for dx, dy in D:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and not grid[nx][ny]:
                        visited[nx][ny] = k
                        q.append((nx, ny))
            area[k] = cnt
            k += 1
res = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not grid[i][j]: continue
        res[i][j] = 1
        s = []
        for di, dj in D:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not grid[ni][nj]:
                if visited[ni][nj] in s: continue
                res[i][j] += area[visited[ni][nj]]
                s.append(visited[ni][nj])
        res[i][j] %= 10
stdout.write("\n".join("".join(map(str, i)) for i in res))