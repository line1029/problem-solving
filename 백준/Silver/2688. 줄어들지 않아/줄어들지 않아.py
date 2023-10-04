from sys import stdin
from math import comb
t = int(stdin.readline())
ans = [0]*t
for idx, i in enumerate(map(int, stdin.read().splitlines())):
    ans[idx] = comb(9 + i, i)
print("\n".join(map(str, ans)))