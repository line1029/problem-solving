from sys import stdin
n = int(stdin.readline())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
dp0 = [[0]*n for _ in range(n)]
dp1 = [[0]*n for _ in range(n)]
dp2 = [[0]*n for _ in range(n)]
for i in range(1, n):
    if not grid[0][i]:
        dp0[0][i] = 1
    else:
        break
for i in range(1, n):
    for j in range(2, n):
        if not grid[i][j]:
            dp0[i][j] += dp0[i][j - 1] + dp2[i][j - 1]
            dp1[i][j] += dp1[i - 1][j] + dp2[i - 1][j]
            if grid[i - 1][j] or grid[i][j - 1]:
                continue
            dp2[i][j] += dp0[i - 1][j - 1] + dp1[i - 1][j - 1] + dp2[i - 1][j - 1]
print(dp0[-1][-1] + dp1[-1][-1] + dp2[-1][-1])