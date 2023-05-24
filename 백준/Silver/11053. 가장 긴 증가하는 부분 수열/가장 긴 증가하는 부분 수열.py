# dp with O(n^2)
from sys import stdin
from itertools import islice
n = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))
dp = [1] * n
total_max = 1
for cur_idx, cur_num in enumerate(seq):
    for prev_idx, prev_lis in enumerate(islice(dp, cur_idx)):
        if cur_num > seq[prev_idx] and dp[cur_idx] < prev_lis + 1:
            dp[cur_idx] = prev_lis + 1
            total_max = max(prev_lis + 1, total_max)

print(total_max)