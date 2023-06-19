from sys import stdin
from collections import Counter
from itertools import combinations
# O(n^2 + m^2)
t = int(stdin.readline())
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))
pa = [0]*(n + 1)
pb = [0]*(m + 1)
for i, num in enumerate(a, 1):
    pa[i] += pa[i - 1] + num
for i, num in enumerate(b, 1):
    pb[i] += pb[i - 1] + num
ca = Counter(pa[j] - pa[i] for i, j in combinations(range(n + 1), 2))
cb = Counter(pb[j] - pb[i] for i, j in combinations(range(m + 1), 2))
ans = 0
if len(ca) > len(cb):
    ca, cb = cb, ca
for k, v in ca.items():
    if t - k in cb:
        ans += v*cb[t - k]
print(ans)