from sys import stdin
n, m = map(int, stdin.readline().split())
mat = list(map(lambda x: list(map(int, x.strip())), stdin.readlines()))
from collections import deque
di = ((1, 0), (0, 1), (-1, 0), (0, -1))
q = deque([(0, 0)])
while q:
    y, x = q.popleft()
    for dy, dx in di:
        row, col = y+dy, x+dx
        if 0<=row<n and 0<=col<m and mat[row][col] == 1:
            mat[row][col] += mat[y][x]
            q.append((row, col))
print(mat[-1][-1])