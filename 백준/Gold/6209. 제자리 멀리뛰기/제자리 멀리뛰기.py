import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
d, n, m = map(int, input().split())
if n == m:
    print(d)
    exit()
arr = [0]*n
for i in range(n):
    arr[i] = int(input())
arr.sort()
lo, hi = 0, d
while lo < hi:
    mid = (lo + hi + 1) >> 1
    cnt = 0
    prev = 0
    for i in arr:
        if i - prev >= mid:
            cnt += 1
            prev = i
        if cnt > n - m or (cnt == n - m and d - i >= mid):
            lo = mid
            break
    else:
        hi = mid - 1
print(lo)