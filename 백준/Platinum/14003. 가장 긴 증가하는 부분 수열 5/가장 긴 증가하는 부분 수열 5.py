from sys import stdin, stdout
from bisect import bisect_left

n = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))
dp = []
dp_idx = []
path = [0]*n
for idx, num in enumerate(seq):
    k = bisect_left(dp, num)
    if k == len(dp):
        dp.append(num)
        dp_idx.append(idx)
    else:
        dp[k] = num
        dp_idx[k] = idx
    path[idx] = dp_idx[k-1]
lis = [dp[-1]]
cur = dp_idx[-1]
for _ in range(len(dp)-1):
    cur = path[cur]
    lis.append(seq[cur])
print(len(dp))
stdout.write(" ".join(map(str, reversed(lis))))