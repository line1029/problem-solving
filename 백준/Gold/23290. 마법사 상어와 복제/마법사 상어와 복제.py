from sys import stdin
from itertools import product
direc_fish = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
direc_shark = ((-1, 0), (0, -1), (1, 0), (0, 1))
path_shark = tuple(product(direc_shark, repeat=3))
grid = [[list() for _ in range(4)] for __ in range(4)]
smell_grid = [[0]*4 for _ in range(4)]
m, s = map(int, stdin.readline().split())
for _ in range(m):
    x, y, d = map(lambda x: int(x)-1, stdin.readline().split())
    grid[x][y].append(d)
sx, sy = map(lambda x: int(x)-1, stdin.readline().split())
total_fish = m
for _ in range(s):
    new_grid = [[list() for _ in range(4)] for __ in range(4)]
    for i, j in product(range(4), repeat=2):
        for fish_direc_idx in grid[i][j]:
            for d in range(fish_direc_idx, fish_direc_idx-8, -1):
                d %= 8
                di, dj = direc_fish[d]
                ni, nj = i + di, j + dj
                if 0 <= ni < 4 and 0 <= nj < 4 and (ni != sx or nj != sy) and not smell_grid[ni][nj]:
                    new_grid[ni][nj].append(d)
                    break
            else:
                new_grid[i][j].append(fish_direc_idx)
    deleted_fish = -1
    for path in path_shark:
        cur_x, cur_y = sx, sy
        for di, dj in path:
            cur_x += di
            cur_y += dj
            if 0 > cur_x or cur_x >= 4 or 0 > cur_y or cur_y >= 4:
                break
        else:
            cur_x, cur_y = sx, sy
            cnt = 0
            visited = set()
            for di, dj in path:
                cur_x += di
                cur_y += dj
                if (cur_x, cur_y) not in visited:
                    cnt += len(new_grid[cur_x][cur_y])
                    visited.add((cur_x, cur_y))
            if deleted_fish < cnt:
                deleted_fish = cnt
                best_path = path
    for di, dj in best_path:
        sx += di
        sy += dj
        if new_grid[sx][sy]:
            smell_grid[sx][sy] = 3
        new_grid[sx][sy].clear()
    total_fish *= 2
    total_fish -= deleted_fish
    for i, j in product(range(4), repeat=2):
        new_grid[i][j].extend(grid[i][j])
        if smell_grid[i][j]:
            smell_grid[i][j] -= 1
    grid = new_grid
print(total_fish)