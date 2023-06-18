from sys import stdin
n, *arr = stdin.read().splitlines()
n = int(n)
arr = list(map(lambda x: list(map(int, x.split())), arr))
dp = [[0]*n for _ in range(n)]
for j in range(1, n):
    for i in range(n - j):
        dp[i][i + j] = min(arr[i][0]*arr[i][1]*arr[i + j][1] + dp[i + 1][i + j],
                           arr[i][0]*arr[i + j][0]*arr[i + j][1] + dp[i][i + j - 1])
        for k in range(i + 1, i + j):
            dp[i][i + j] = min(dp[i][i + j],
                               dp[i][k] + dp[k + 1][i + j] + arr[i][0]*arr[k][1]*arr[i + j][1])
print(dp[0][-1])