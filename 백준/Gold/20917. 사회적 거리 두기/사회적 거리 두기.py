import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n, s = map(int, input().split())
    plugs = sorted(map(int, input().split()))
    lo, hi = 1, plugs[-1] - plugs[0]
    while lo < hi:
        mid = (lo + hi + 1) >> 1
        prev = plugs[0]
        cnt = 1
        for i in range(1, n):
            if plugs[i] - prev >= mid:
                cnt += 1
                prev = plugs[i]
            if cnt == s:
                lo = mid
                break
        else:
            hi = mid - 1
    print(lo)