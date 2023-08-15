from sys import stdin
n, m = map(int, stdin.readline().split())
grid = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, stdin.readline().split())
    grid[a][b] = 1
    grid[b][a] = -1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if grid[i][k] == grid[k][j] != 0:
                grid[i][j] = grid[i][k]
print(sum(i.count(0) == 1 for i in grid))