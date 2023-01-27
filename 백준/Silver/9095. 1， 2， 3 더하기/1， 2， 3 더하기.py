dp = [1, 1, 2, 4] + [0]*7
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
from sys import stdin
stdin.readline()
nums = list(map(lambda x: dp[int(x)], stdin.readlines()))
print("\n".join(map(str, nums)))
    