from sys import stdin, stdout

n, c = map(int, stdin.readline().split())
houses = sorted(map(int, stdin.readlines()))
lo, hi = 1, (houses[-1] - houses[0]) // (c - 1)
while lo < hi:
    mid = (lo + hi + 1) >> 1
    cnt, prev = 1, houses[0]
    for i in range(1, n):
        if houses[i] - prev >= mid:
            prev = houses[i]
            cnt += 1
        if cnt == c:
            lo = mid
            break
    else:
        hi = mid - 1
stdout.write(str(lo))