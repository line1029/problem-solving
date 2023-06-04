from sys import stdin
from collections import deque
n, m, t = map(int, stdin.readline().split())
direc = ((1, 0), (0, 1), (-1, 0), (0, -1))
circles = []
visited = set()
for _ in range(n):
    circles.append(list(map(int, stdin.readline().split())))
_sum = sum(sum(i) for i in circles)
_cnt = n*m
rotates = map(lambda x:map(int, x.split()), stdin.read().splitlines())
for x, d, k in rotates:
    for i in range(x-1, n, x):
        r = (2*d - 1)*k
        circles[i] = circles[i][r:] + circles[i][:r]
    for row in range(n):
        for col in range(m):
            if (row, col) in visited:
                continue
            if not circles[row][col]:
                continue
            q = deque([(row, col)])
            num = circles[row][col]
            while q:
                i, j = q.popleft()
                for di, dj in direc:
                    ni, nj = i + di, (j + dj)%m
                    if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited and circles[ni][nj] == num:
                        visited.add((ni, nj))
                        q.append((ni, nj))
    if visited:
        for row, col in visited:
            _sum -= circles[row][col]
            _cnt -= 1
            circles[row][col] = 0
        visited.clear()
    else:
        if not _cnt:
            continue
        avg = _sum / _cnt
        for row in range(n):
            for col in range(m):
                if circles[row][col]:
                    if circles[row][col] > avg:
                        _sum -= 1
                        circles[row][col] -= 1
                    elif circles[row][col] < avg:
                        _sum += 1
                        circles[row][col] += 1
print(_sum)