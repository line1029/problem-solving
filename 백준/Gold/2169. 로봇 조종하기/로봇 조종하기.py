from sys import stdin
n, m = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
dp = [[0]*m for _ in range(n)]
right = [0]*m
dp[0] = grid[0][:]
for i in range(1, m):
    dp[0][i] += dp[0][i - 1]
for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, m):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
    right = [0] * m
    right[-1] = dp[i - 1][-1] + grid[i][-1]
    for j in range(m - 2, -1, -1):
        right[j] = max(right[j + 1], dp[i - 1][j]) + grid[i][j]
    dp[i] = [max(dp[i][j], right[j]) for j in range(m)]
print(dp[n - 1][m - 1])