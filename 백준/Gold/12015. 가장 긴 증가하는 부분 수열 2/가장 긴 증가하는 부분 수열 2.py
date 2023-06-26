from sys import stdin
from bisect import bisect_left
n = int(stdin.readline())
seq = map(int, stdin.readline().split())
dp = []
for num in seq:
    k = bisect_left(dp, num)
    if k == len(dp):
        dp.append(num)
    else:
        dp[k] = num
print(len(dp))