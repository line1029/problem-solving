from sys import stdin
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
lo, hi = sum(arr)//m, sum(arr)
while lo < hi:
    mid = (lo + hi) >> 1
    cnt = cur = 0
    for i in arr:
        if i > mid:
            lo = mid + 1
            break
        if cur + i > mid:
            cnt += 1
            cur = i
            if cnt >= m:
                lo = mid + 1
                break
        else:
            cur += i
    else:
        hi = mid
print(lo)