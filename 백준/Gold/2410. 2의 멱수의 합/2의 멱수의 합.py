n = int(input())
dp = [1]*(n + 1)
m = 1_000_000_000
k = 2
while k <= n:
    for i in range(k, n + 1):
        dp[i] += dp[i - k]
        dp[i] %= m
    k <<= 1
print(dp[n])