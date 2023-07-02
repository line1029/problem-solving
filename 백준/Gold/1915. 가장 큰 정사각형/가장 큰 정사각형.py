from sys import stdin
n, m = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x)), stdin.read().splitlines()))
for i in range(1, n):
    for j in range(1, m):
        if grid[i][j]:
            grid[i][j] = min(grid[i - 1][j - 1], grid[i - 1][j], grid[i][j - 1]) + 1
print(max(max(i) for i in grid)**2)