n = int(input())
if n <= 2:
    print(n)
    exit()
m = 1_000_000_000
dp = [1]*(n + 2)
for i in range(2, n + 1, 2):
    dp[i] = dp[i + 1] = (dp[i - 1] + dp[i >> 1])%m
print(dp[n])