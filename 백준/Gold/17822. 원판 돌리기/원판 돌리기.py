from sys import stdin
from collections import deque
n, m, t = map(int, stdin.readline().split())
direc = ((1, 0), (0, 1), (-1, 0), (0, -1))
circles = []
visited = [[0]*m for _ in range(n)]
for _ in range(n):
    circles.append(deque(map(int, stdin.readline().split())))
rotates = map(lambda x:map(int, x.split()), stdin.read().splitlines())
for x, d, k in rotates:
    for i in range(x-1, n, x):
        circles[i].rotate((-2*d + 1)*k)
    for row in range(n):
        for col in range(m):
            if visited[row][col]:
                continue
            if not circles[row][col]:
                continue
            q = deque([(row, col)])
            num = circles[row][col]
            while q:
                i, j = q.popleft()
                for di, dj in direc:
                    ni, nj = i + di, (j + dj)%m
                    if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and circles[ni][nj] == num:
                        visited[ni][nj] = 1
                        q.append((ni, nj))
    if sum(sum(i) for i in visited):
        for row in range(n):
            for col in range(m):
                if visited[row][col]:
                    circles[row][col] = 0
                    visited[row][col] = 0
    else:
        cnt = n*m - sum(i.count(0) for i in circles)
        if not cnt:
            continue
        avg = sum(sum(i) for i in circles) / cnt
        for row in range(n):
            for col in range(m):
                if circles[row][col]:
                    if circles[row][col] > avg:
                        circles[row][col] -= 1
                    elif circles[row][col] < avg:
                        circles[row][col] += 1
print(sum(sum(i) for i in circles))