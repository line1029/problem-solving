from sys import stdin
n, k = map(int, stdin.read().splitlines())
lo, hi = 1, k
while lo < hi:
    mid = (lo + hi) >> 1
    sqmid = int(mid**.5)
    x = 0
    for i in range(1, sqmid + 1):
        x += min(n, mid//i)
    x <<= 1
    x -= sqmid**2
    if x >= k:
        hi = mid
    else:
        lo = mid + 1
print(lo)