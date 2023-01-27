from sys import stdin
from collections import deque
m, n = map(int, stdin.readline().split())
tomatos = list(map(lambda x: list(map(int, x.split())), stdin.readlines()))
q = deque()
immature = 0
for i, row in enumerate(tomatos):
    for j, tom in enumerate(row):
        if tom == 0:
            immature += 1
        elif tom == 1:
            q.append((i, j))
if not immature:
    print(0)
    exit()
direc = ((1, 0), (-1, 0), (0, 1), (0, -1))
while q:
    y, x = q.popleft()
    for dy, dx in direc:
        row, col = y+dy, x+dx
        if 0<=row<n and 0<=col<m and tomatos[row][col] == 0:
            tomatos[row][col] = tomatos[y][x] + 1
            ans = tomatos[row][col]
            q.append((row, col))
            immature -= 1
if immature:
    print(-1)
else:
    print(ans - 1)