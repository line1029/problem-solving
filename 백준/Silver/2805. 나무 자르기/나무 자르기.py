from sys import stdin
from collections import Counter
input = stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
tt = Counter(trees)
lo, hi = 0, 10**9
def is_good(num, tt, m):
    res = 0
    for h, cnt in tt.items():
        if h > num:
            res += (h - num)*cnt
        if res >= m:
            return True
    return False
while lo <= hi:
    mi = (lo + hi)//2
    if is_good(mi, tt, m):
        lo = mi + 1
    else:
        hi = mi - 1
print(hi)