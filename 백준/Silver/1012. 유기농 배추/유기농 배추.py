from collections import deque
from sys import stdin
def nums_of_baechu_island(n, m, grid):
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if (i, j) in grid:
                cnt += 1
                grid.discard((i, j))
                q = deque([(i, j)])
                while q:
                    y, x = q.popleft()
                    for dy, dx in directions:
                        row, col = y+dy, x+dx
                        if 0<=row<n and 0<=col<m and (row, col) in grid:
                            grid.discard((row, col))
                            q.append((row, col))
    return cnt

for _ in range(int(stdin.readline())):
    n, m, k = map(int, stdin.readline().split())
    grid = set()
    for _ in range(k):
        grid.add(tuple(map(int, stdin.readline().split())))
    print(nums_of_baechu_island(n, m, grid))