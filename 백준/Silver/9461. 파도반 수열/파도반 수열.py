from sys import stdin
dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
t = int(stdin.readline())
nums = list(map(int, stdin.readlines()))
n = max(nums)
for i in range(11, n + 1):
    dp.append(dp[i-1] + dp[i-5])
print("\n".join(map(lambda x: str(dp[x]), nums)))