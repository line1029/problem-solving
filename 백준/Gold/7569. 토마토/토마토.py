from sys import stdin
from collections import defaultdict, deque
m, n, h = map(int, stdin.readline().split())
tomatos = []
immature = 0
q = deque()
for k in range(h):
    tmp = []
    for j in range(n):
        row = list(map(int, stdin.readline().split()))
        for i in range(m):
            if row[i] == 1:
                q.append((k, j, i))
            elif row[i] == 0:
                immature += 1
        tmp.append(row)
    tomatos.append(tmp)
if not immature:
    print(0)
    exit()
direc = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
ans = 0
while q:
    z, y, x = q.popleft()
    for dz, dy, dx in direc:
        nz, ny, nx = (z+dz, y+dy, x+dx)
        if 0<=nz<h and 0<=ny<n and 0<=nx<m and tomatos[nz][ny][nx] == 0:
            tomatos[nz][ny][nx] = tomatos[z][y][x] + 1
            immature -= 1
            ans = tomatos[nz][ny][nx]
            q.append((nz, ny, nx))
            
if immature:
    print(-1)
else:
    print(ans - 1)
            