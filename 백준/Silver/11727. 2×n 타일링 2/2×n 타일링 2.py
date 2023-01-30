n = int(input())
dp = [1, 1, 3, 5] + [0]*(n-3)
for i in range(4, n+1):
    dp[i] += (dp[i-1] + 2*dp[i-2])%10007
print(dp[n])