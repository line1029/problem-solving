# note that every permutations can be decomposed into disjoint cycles.
# there are total 6 cases.
# if ans == 1, there is only one case, one 2-cycle
# if ans == 2, there are two cases, two 2-cycles or one 3-cycle
# if ans == 3, there are three cases, three 2-cycles, one 2-cycle & one 3-cycle, or one 4-cycle
# for 2-cycle, there is only one possible transposition representation
# for 3-cycle, there are three possible transposition representations
# for 4-cycle, there are sixteen possible transposition representations
### example
# let 4-cycle be (1, 2, 3, 4). then [1, 2, 3, 4] -> [2, 3, 4, 1]
# we need inverse of (1, 2, 3, 4), which is (4, 3, 2, 1)
# possible transposition representations of (4, 3, 2, 1) are
# [((1, 2), (1, 3), (1, 4)),
#  ((1, 2), (1, 4), (3, 4)),
#  ((1, 2), (3, 4), (1, 3)),
#  ((1, 3), (1, 4), (2, 3)),
#  ((1, 3), (2, 3), (1, 4)),
#  ((1, 4), (2, 3), (2, 4)),
#  ((1, 4), (2, 4), (3, 4)),
#  ((1, 4), (3, 4), (2, 3)),
#  ((2, 3), (1, 2), (1, 4)),
#  ((2, 3), (1, 4), (2, 4)),
#  ((2, 3), (2, 4), (1, 2)),
#  ((2, 4), (1, 2), (3, 4)),
#  ((2, 4), (3, 4), (1, 2)),
#  ((3, 4), (1, 2), (1, 3)),
#  ((3, 4), (1, 3), (2, 3)),
#  ((3, 4), (2, 3), (1, 2))]
#
# for example, let's see ((1, 2), (1, 3), (1, 4))
# transpositions are applied from right to left
# (1, 4) : [1, 2, 3, 4] -> [4, 2, 3, 1]
# (1, 3) : [4, 2, 3, 1] -> [4, 2, 1, 3]
# (1, 2) : [4, 2, 1, 3] -> [4, 1, 2, 3]
# so product of ((1, 2), (1, 3), (1, 4)) makes [1, 2, 3, 4] -> [4, 1, 2, 3], which is (4, 3, 2, 1) in cycle form.

from sys import stdin
from itertools import product, permutations
from collections import defaultdict
# from pprint import pprint
n, m, h = map(int, stdin.readline().split())
grid = [list(range(1, n + 1))]
edges = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
visited = [[0]*(n + 1) for _ in range(h + 1)]
# print(n, m, h)
# pprint(grid)
# pprint(edges)
for a, b in edges:
    visited[a][b] = 1
    while len(grid) <= a:
        grid.append(grid[-1][:])
    grid[-1][b - 1], grid[-1][b] = grid[-1][b], grid[-1][b - 1]
while len(grid) <= h:
    grid.append(grid[-1][:])
# pprint(grid)
# pprint(visited)
cycles = []
cycle_visited = set()
start, end = grid[0], grid[-1]
if start == end:
    print(0)
    exit()
for i in start:
    if i in cycle_visited:
        continue
    tmp = [i]
    nex = end[i - 1]
    cycle_visited.add(i)
    while nex != i:
        cycle_visited.add(nex)
        tmp.append(nex)
        nex = end[nex - 1]
    if len(tmp) > 1:
        cycles.append(tmp)
# print(cycles)
ans = sum(len(i) - 1 for i in cycles)
# print(ans)
if ans > 3:
    print(-1)
    exit()


path_idxs = (
    (((0, 1), ), ),
    (((0, 2), (0, 1)),
     ((1, 2), (0, 2)),
     ((0, 1), (1, 2))),
    (((0, 3), (0, 2), (0, 1)),
     ((2, 3), (0, 3), (0, 1)),
     ((0, 2), (2, 3), (0, 1)),
     ((1, 2), (0, 3), (0, 2)),
     ((0, 3), (1, 2), (0, 2)),
     ((1, 3), (1, 2), (0, 3)),
     ((2, 3), (1, 3), (0, 3)),
     ((1, 2), (2, 3), (0, 3)),
     ((0, 3), (0, 1), (1, 2)),
     ((1, 3), (0, 3), (1, 2)),
     ((0, 1), (1, 3), (1, 2)),
     ((2, 3), (0, 1), (1, 3)),
     ((0, 1), (2, 3), (1, 3)),
     ((0, 2), (0, 1), (2, 3)),
     ((1, 2), (0, 2), (2, 3)),
     ((0, 1), (1, 2), (2, 3)))
)
promising_paths = set()
promising_paths_for_cycle = []
for cycle in cycles:
    promising_paths_for_cycle.append(list(map(lambda x: tuple(map(lambda y: (cycle[y[0]], cycle[y[1]]) if cycle[y[0]] < cycle[y[1]] else (cycle[y[1]], cycle[y[0]]), x)), path_idxs[len(cycle) - 2])))
# print(promising_paths_for_cycle)
for paths in product(*promising_paths_for_cycle):
    # print(paths)
    
    perms_with_identical_elts = []
    for idx, val in enumerate(paths):
        perms_with_identical_elts += [idx]*len(val)
    # print(perms_with_identical_elts)
    perms_with_identical_elts = set(permutations(perms_with_identical_elts))

    # print(perms_with_identical_elts)
    promising_path = []
    for pattern in perms_with_identical_elts:
        paths_generator = [iter(i) for i in paths]
        promising_path.append(tuple(next(paths_generator[i]) for i in pattern))
    # print("path: ",path)
    promising_paths.update(promising_path)

# print(promising_paths)
promising_candidate = defaultdict(set)
for path in promising_paths:
    for idx, step in enumerate(path):
        promising_candidate[path[:idx]].add(step)
# print(promising_candidate)

def dfs(depth, start_row, start_col, path):
    # print(depth, start_row, start_col, path)
    # pprint(grid)
    # pprint(visited)
    for row, col in product(range(start_row, h + 1), range(1, n)):
        if row == start_row and col < start_col:
            continue
        if visited[row][col-1] == visited[row][col] == visited[row][col+1] == 0:
            candidate = (grid[row][col], grid[row][col-1]) if grid[row][col] < grid[row][col-1] else (grid[row][col-1], grid[row][col])
            if candidate in promising_candidate[path]:
                if depth + 1 == ans:
                    print(ans)
                    exit()
                swap_idxs = [(row_idx, i.index(candidate[0]), i.index(candidate[1])) for row_idx, i in enumerate(grid[row:], row)]
                for row_idx, pre, nex in swap_idxs:
                    grid[row_idx][pre], grid[row_idx][nex] = grid[row_idx][nex], grid[row_idx][pre]
                dfs(depth + 1, row, col + 2, path + (candidate, ))
                for row_idx, pre, nex in swap_idxs:
                    grid[row_idx][pre], grid[row_idx][nex] = grid[row_idx][nex], grid[row_idx][pre]
dfs(0, 1, 1, ())
print(-1)