from sys import stdin
n, m = map(int, stdin.readline().split())
grid = [[0] for _ in range(n + 1)]
grid[0] = [0]*(m + 1)
for i in range(1, n + 1):
    grid[i].extend(map(int, stdin.readline().split()))
    for j in range(1, m + 1):
        grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
print(grid[n][m])
