# dfs
from sys import stdin
w, h = map(int, stdin.readline().split())
direc = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
while w and h:
    grid = []
    visited = [[0]*w for _ in range(h)]
    nums_of_island = 0
    for _ in range(h):
        grid.append(list(map(int, stdin.readline().split())))
    for row in range(h):
        for col in range(w):
            if grid[row][col] and not visited[row][col]:
                stack = [(row, col)]
                visited[row][col] = 1
                while stack:
                    i, j = stack.pop()
                    for di, dj in direc:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] and not visited[ni][nj]:
                            stack.append((ni, nj))
                            visited[ni][nj] = 1
                nums_of_island += 1
    print(nums_of_island)
    w, h = map(int, stdin.readline().split())