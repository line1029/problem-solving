from sys import stdin
from bisect import bisect_left
n = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))
dp_inc = []
dp_dec = []
len_inc = [0]*n
len_dec = [0]*n

for i, num in enumerate(seq):
    k = bisect_left(dp_inc, num)
    if k == len(dp_inc):
        dp_inc.append(num)
    else:
        dp_inc[k] = num
    len_inc[i] = k
for i in range(n-1, -1, -1):
    k = bisect_left(dp_dec, seq[i])
    if k == len(dp_dec):
        dp_dec.append(seq[i])
    else:
        dp_dec[k] = seq[i]
    len_dec[i] = k
print(max(i + j for i, j in zip(len_dec, len_inc)) + 1)