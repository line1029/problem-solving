from sys import stdin
def main():
    n = int(input())
    dp = [[0]*n for _ in range(3)]
    dp[0][0] = dp[1][0] = dp[2][0] = 1
    for i in range(1, n):
        dp[0][i] = (dp[0][i - 1] + dp[1][i - 1] + dp[2][i - 1])%9901
        dp[1][i] = (dp[0][i - 1] + dp[2][i - 1])%9901
        dp[2][i] = (dp[1][i - 1] + dp[0][i - 1])%9901
    print(sum(dp[i][n - 1] for i in range(3))%9901)
main()