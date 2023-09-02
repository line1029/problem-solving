def solution(x):
    n = len(x)
    dp = [[0]*n for _ in range(n)]
    for j in range(1, n):
        for i in range(n - j):
            dp[i][i + j] = min(
                x[i][0]*x[i][1]*x[i + j][1] + dp[i + 1][i + j],
                x[i][0]*x[i + j][0]*x[i + j][1] + dp[i][i + j - 1]
            )
            for k in range(1, j - 1):
                dp[i][i + j] = min(
                    dp[i][i + j],
                    dp[i][i + k] + dp[i + k + 1][i + j] + x[i][0]*x[i + k][1]*x[i + j][1]
                )
    return dp[0][-1]