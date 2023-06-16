from sys import stdin
n, s = map(int, stdin.readline().split())
nums = sorted(map(int, stdin.readline().split()))
if 0 < s > nums[-1]*n or 0 > s < nums[0]*n:
    print(0)
    exit()
dp = [0]*(n + 1)*(max(abs(nums[0]), abs(nums[-1])) + 1)
cur_min = cur_max = 0
for num in nums:
    if num < 0:
        cur_min += num
        for i in range(cur_min, cur_max + 1):
            dp[i] += dp[i - num]
        dp[num] += 1
    else:
        cur_max += num
        for i in range(cur_max, cur_min - 1, -1):
            dp[i] += dp[i - num]
        dp[num] += 1
print(dp[s])