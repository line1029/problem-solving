from sys import stdin
def main():
    n, k = map(int, stdin.read().splitlines())
    lo, hi = 1, k
    while lo < hi:
        mid = (lo + hi) >> 1
        sqmid = int(mid**.5)
        if sum(2*min(n, mid//i) for i in range(1, sqmid + 1)) - sqmid*sqmid >= k:
            hi = mid
        else:
            lo = mid + 1
    print(lo)
main()