from sys import stdin
from itertools import product
N, M, K = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
R_e, C_e = map(lambda x: int(x) - 1, grid.pop().split())
R_s, C_s = map(lambda x: int(x) - 1, grid.pop().split())
def bfs(cur, grid):
    nex = [[[0]*8 for __ in range(M)] for _ in range(N)]
    limit = max(N, M)
    for i, j in product(range(N), range(M)):
        if grid[i][j] == "#":
            continue
        for d in range(1, limit):
            row, col = i - d, j
            if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
                break
            for k in range(8):
                if k == 0:
                    continue
                nex[i][j][0] += cur[row][col][k]
                nex[i][j][0] %= 998244353
        for d in range(1, limit):
            row, col = i + d, j
            if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
                break
            for k in range(8):
                if k == 1:
                    continue
                nex[i][j][1] += cur[row][col][k]
                nex[i][j][1] %= 998244353
        for d in range(1, limit):
            row, col = i - d, j - d
            if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
                break
            for k in range(8):
                if k == 2:
                    continue
                nex[i][j][2] += cur[row][col][k]
                nex[i][j][2] %= 998244353
        for d in range(1, limit):
            row, col = i - d, j + d
            if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
                break
            for k in range(8):
                if k == 3:
                    continue
                nex[i][j][3] += cur[row][col][k]
                nex[i][j][3] %= 998244353
        for d in range(1, limit):
            row, col = i + d, j - d
            if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
                break
            for k in range(8):
                if k == 4:
                    continue
                nex[i][j][4] += cur[row][col][k]
                nex[i][j][4] %= 998244353
        for d in range(1, limit):
            row, col = i + d, j + d
            if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
                break
            for k in range(8):
                if k == 5:
                    continue
                nex[i][j][5] += cur[row][col][k]
                nex[i][j][5] %= 998244353
        for d in range(1, limit):
            row, col = i, j - d
            if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
                break
            for k in range(8):
                if k == 6:
                    continue
                nex[i][j][6] += cur[row][col][k]
                nex[i][j][6] %= 998244353
        for d in range(1, limit):
            row, col = i, j + d
            if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
                break
            for k in range(8):
                if k == 7:
                    continue
                nex[i][j][7] += cur[row][col][k]
                nex[i][j][7] %= 998244353
    return nex
cur = [[[0]*8 for __ in range(M)] for _ in range(N)]
limit = max(M, N)
for d in range(1, limit):
    row, col = R_s - d, C_s
    if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
        break
    cur[row][col][1] = 1
for d in range(1, limit):
    row, col = R_s + d, C_s
    if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
        break
    cur[row][col][0] = 1
for d in range(1, limit):
    row, col = R_s - d, C_s - d
    if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
        break
    cur[row][col][5] = 1
for d in range(1, limit):
    row, col = R_s - d, C_s + d
    if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
        break
    cur[row][col][4] = 1
for d in range(1, limit):
    row, col = R_s + d, C_s - d
    if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
        break
    cur[row][col][3] = 1
for d in range(1, limit):
    row, col = R_s + d, C_s + d
    if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
        break
    cur[row][col][2] = 1
for d in range(1, limit):
    row, col = R_s, C_s - d
    if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
        break
    cur[row][col][7] = 1
for d in range(1, limit):
    row, col = R_s, C_s + d
    if any([0 > row, N <= row, 0 > col, M <= col]) or grid[row][col] == "#":
        break
    cur[row][col][6] = 1
for _ in range(K - 1):
    cur = bfs(cur, grid)
print(sum(cur[R_e][C_e]))