from sys import stdin
from itertools import product, permutations
from collections import defaultdict
# from pprint import pprint
n, m, h = map(int, stdin.readline().split())
grid = [list(range(1, n + 1))]
edges = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
visited = [[0]*(n + 1) for _ in range(h + 1)]
for a, b in edges:
    visited[a][b] = 1
    while len(grid) <= a:
        grid.append(grid[-1][:])
    grid[-1][b - 1], grid[-1][b] = grid[-1][b], grid[-1][b - 1]
while len(grid) <= h:
    grid.append(grid[-1][:])
start, end = grid[0], grid[-1]

if start == end:
    print(0)
    exit()
ans = [4]
def brute_force_3_transposition(depth, start_row, start_col):
    if depth >= 3:
        return
    for col in range(start_col, n):
        if visited[start_row][col-1] == visited[start_row][col] == visited[start_row][col+1] == 0:
            candidate = grid[start_row][col-1], grid[start_row][col]
            swap_idxs = [(row_idx, i.index(candidate[0]), i.index(candidate[1])) for row_idx, i in enumerate(grid[start_row:], start_row)]
            # print(depth, start_row, start_col, col)
            for row_idx, pre, nex in swap_idxs:
                grid[row_idx][pre], grid[row_idx][nex] = grid[row_idx][nex], grid[row_idx][pre]
            # print("before_dfs: ", depth, grid)
            if start == end:
                ans[0] = min(ans[0], depth + 1)
                for row_idx, pre, nex in swap_idxs:
                    grid[row_idx][pre], grid[row_idx][nex] = grid[row_idx][nex], grid[row_idx][pre]
                return
            brute_force_3_transposition(depth + 1, start_row, col + 2)
            for row_idx, pre, nex in swap_idxs:
                grid[row_idx][pre], grid[row_idx][nex] = grid[row_idx][nex], grid[row_idx][pre]
            # print("after_dfs: ", depth, grid)
    
    for row, col in product(range(start_row + 1, h + 1), range(1, n)):
        if visited[row][col-1] == visited[row][col] == visited[row][col+1] == 0:
            candidate = grid[row][col-1], grid[row][col]
            swap_idxs = [(row_idx, i.index(candidate[0]), i.index(candidate[1])) for row_idx, i in enumerate(grid[row:], row)]
            # print(depth, start_row, start_col, row, col)
            for row_idx, pre, nex in swap_idxs:
                grid[row_idx][pre], grid[row_idx][nex] = grid[row_idx][nex], grid[row_idx][pre]
            # print("before_dfs: ", depth, grid)
            if start == end:
                ans[0] = min(ans[0], depth + 1)
                for row_idx, pre, nex in swap_idxs:
                    grid[row_idx][pre], grid[row_idx][nex] = grid[row_idx][nex], grid[row_idx][pre]
                return
            brute_force_3_transposition(depth + 1, row, col + 2)
            for row_idx, pre, nex in swap_idxs:
                grid[row_idx][pre], grid[row_idx][nex] = grid[row_idx][nex], grid[row_idx][pre]
            # print("after_dfs: ", depth, grid)

brute_force_3_transposition(0, 1, 1)
if ans[0] == 4:
    print(-1)
else:
    print(ans[0])