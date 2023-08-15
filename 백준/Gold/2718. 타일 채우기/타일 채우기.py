from sys import stdin, stdout
def main():
    t = int(stdin.readline())
    arr = list(map(int, stdin.read().splitlines()))
    n = max(arr) + 1
    dp = [[0]*(n + 1) for _ in range(4)]
    dp[0][0] = dp[0][1] = dp[1][1] = dp[3][1] = 1
    for i in range(2, n + 1):
        dp[0][i] = dp[0][i - 1] + dp[0][i - 2] + dp[1][i - 1]*2 + dp[3][i - 1]
        dp[1][i] = dp[0][i - 1] + dp[1][i - 1]
        dp[2][i] = dp[3][i - 1]
        dp[3][i] = dp[0][i - 1] + dp[2][i - 1]
    stdout.write("\n".join(str(dp[0][i]) for i in arr))
main()