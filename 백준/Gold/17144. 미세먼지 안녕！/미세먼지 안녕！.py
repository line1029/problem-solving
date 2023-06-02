from sys import stdin
from itertools import product
R, C, T = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
subgrid = [[0]*C for _ in range(R)]
for i, row in enumerate(grid):
    if row[0] == -1:
        air_cleaner = i
        break
border = set((-1, i) for i in range(C))
border.update((i, -1) for i in range(-1, R + 1))
border.update((i, C) for i in range(-1, R + 1))
border.update((R, i) for i in range(C))
border.update(((air_cleaner, 0), (air_cleaner+1, 0)))
direc = ((-1, 0), (1, 0), (0, 1), (0, -1))
total_dust = sum(sum(i) for i in grid) + 2
for _ in range(T):
    for i, j in product(range(R), range(C)):
        dust = grid[i][j] // 5
        if dust <= 0:
            continue
        for di, dj in direc:
            ni, nj = i + di, j + dj
            if (ni, nj) not in border:
                subgrid[ni][nj] += dust
                grid[i][j] -= dust
    for i, j in product(range(R), range(C)):
        grid[i][j] += subgrid[i][j]
        subgrid[i][j] = 0
    
    tmp, grid[air_cleaner][1] = grid[air_cleaner][1], 0
    for j in range(2, C):
        tmp, grid[air_cleaner][j] = grid[air_cleaner][j], tmp
    for i in range(air_cleaner - 1, -1, -1):
        tmp, grid[i][-1] = grid[i][-1], tmp
    for j in range(C - 2, -1, -1):
        tmp, grid[0][j] = grid[0][j], tmp
    for i in range(1, air_cleaner):
        tmp, grid[i][0] = grid[i][0], tmp
    total_dust -= tmp
    tmp, grid[air_cleaner + 1][1] = grid[air_cleaner + 1][1], 0
    for j in range(2, C):
        tmp, grid[air_cleaner + 1][j] = grid[air_cleaner + 1][j], tmp
    for i in range(air_cleaner + 2, R):
        tmp, grid[i][-1] = grid[i][-1], tmp
    for j in range(C - 2, -1, -1):
        tmp, grid[-1][j] = grid[-1][j], tmp
    for i in range(R - 2, air_cleaner + 1, -1):
        tmp, grid[i][0] = grid[i][0], tmp
    total_dust -= tmp
print(total_dust)