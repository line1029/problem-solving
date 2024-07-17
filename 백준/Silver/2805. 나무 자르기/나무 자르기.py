from sys import stdin
from collections import Counter
n, m = map(int, stdin.readline().split())
trees = Counter(map(int, stdin.readline().split()))

lo, hi = 0, max(1_000_000_000, max(trees))
while lo < hi:
    mid = (lo + hi + 1) >> 1
    if sum((i - mid) * v for i, v in trees.items() if mid < i) >= m:
        lo = mid
    else:
        hi = mid - 1
print(lo)
