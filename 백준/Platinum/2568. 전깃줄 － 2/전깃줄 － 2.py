from sys import stdin, stdout
from bisect import bisect_left
n = int(stdin.readline())
arr = sorted(list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines())), key=lambda x: x[1])
wires = [i[0] for i in arr]
path = [-1]*n
dp = []
dp_idx = []
for idx, num in enumerate(wires):
    k = bisect_left(dp, num)
    if k == len(dp):
        dp.append(num)
        dp_idx.append(idx)
    else:
        dp[k] = num
        dp_idx[k] = idx
    if k:
        path[idx] = dp_idx[k - 1]
idx = dp_idx[-1]
tmp = set(wires)
while idx != -1:
    tmp.discard(wires[idx])
    idx = path[idx]
print(len(tmp))
stdout.write("\n".join(map(str, sorted(tmp))))