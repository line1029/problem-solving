import io, os
from sys import setrecursionlimit
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
if n > 34:
    setrecursionlimit(n*n + 1)
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
memo = [[-1]*n for _ in range(n)]
D = ((0, 1), (1, 0), (-1, 0), (0, -1))
def dfs(i, j):
    if memo[i][j] != -1:
        return memo[i][j]
    for di, dj in D:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and grid[i][j] < grid[ni][nj]:
            memo[i][j] = max(memo[i][j], dfs(ni, nj) + 1)
    if memo[i][j] == -1:
        memo[i][j] = 1
    return memo[i][j]
ans = 0
for i in range(n):
    for j in range(n):
        if memo[i][j] == -1:
            ans = max(ans, dfs(i, j))
print(ans)