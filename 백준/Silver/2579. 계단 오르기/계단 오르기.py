from sys import stdin
n = int(stdin.readline())
stairs = list(map(int, stdin.readlines()))
dp = [0]*n
dp[0] = stairs[0]
if n >= 2:
    dp[1] = stairs[1] + stairs[0]
if n >= 3:
    dp[2] = max(stairs[0], stairs[1]) + stairs[2]
for i in range(3, n):
    dp[i] = max(stairs[i-1] + dp[i-3], dp[i-2]) + stairs[i]
print(dp[n-1])
