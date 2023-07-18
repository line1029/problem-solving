def main():
    n = int(input())
    m = 1_000_000_000
    n >>= 1
    dp = [1]*(n + 1)
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] + dp[i >> 1])
        if dp[i] >= m:
            dp[i] -= m
    print(dp[n])
main()