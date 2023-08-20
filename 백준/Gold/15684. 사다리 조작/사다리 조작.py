"""
note that every permutations can be decomposed into disjoint cycles.
there are total 6 cases.
if ans == 1, there is only one case, one 2-cycle
if ans == 2, there are two cases, two 2-cycles or one 3-cycle
if ans == 3, there are four cases, three 2-cycles, one 2-cycle & one 3-cycle, one 4-cycle, or one 2-cycle with non-adjacent elt
for 2-cycle, there is only one possible transposition representation
for 3-cycle, there are three possible transposition representations
for 4-cycle, there are sixteen possible transposition representations
# example
let 4-cycle be (1, 2, 3, 4). then [1, 2, 3, 4] -> [2, 3, 4, 1]
we need inverse of (1, 2, 3, 4), which is (4, 3, 2, 1)
possible transposition representations of (4, 3, 2, 1) are
[((1, 2), (1, 3), (1, 4)),
 ((1, 2), (1, 4), (3, 4)),
 ((1, 2), (3, 4), (1, 3)),
 ((1, 3), (1, 4), (2, 3)),
 ((1, 3), (2, 3), (1, 4)),
 ((1, 4), (2, 3), (2, 4)),
 ((1, 4), (2, 4), (3, 4)),
 ((1, 4), (3, 4), (2, 3)),
 ((2, 3), (1, 2), (1, 4)),
 ((2, 3), (1, 4), (2, 4)),
 ((2, 3), (2, 4), (1, 2)),
 ((2, 4), (1, 2), (3, 4)),
 ((2, 4), (3, 4), (1, 2)),
 ((3, 4), (1, 2), (1, 3)),
 ((3, 4), (1, 3), (2, 3)),
 ((3, 4), (2, 3), (1, 2))]

for example, let's see ((1, 2), (1, 3), (1, 4))
transpositions are applied from right to left
(1, 4) : [1, 2, 3, 4] -> [4, 2, 3, 1]
(1, 3) : [4, 2, 3, 1] -> [4, 2, 1, 3]
(1, 2) : [4, 2, 1, 3] -> [4, 1, 2, 3]
so product of ((1, 2), (1, 3), (1, 4)) makes [1, 2, 3, 4] -> [4, 1, 2, 3], which is (4, 3, 2, 1) in cycle form.
"""

from sys import stdin
from itertools import product, permutations
from collections import defaultdict
n, m, h = map(int, stdin.readline().split())
res = list(range(1, n + 1))
idxs_grid = [list(range(-1, n))]
edges = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
visited = [[0]*(n + 1) for _ in range(h + 1)]
for a, b in edges:
    visited[a][b] = 1
    while len(idxs_grid) <= a:
        idxs_grid.append(idxs_grid[-1][:])
    res[b - 1], res[b] = res[b], res[b - 1]
    idxs_grid[-1][res[b - 1]], idxs_grid[-1][res[b]] = idxs_grid[-1][res[b]], idxs_grid[-1][res[b - 1]]
cycles = []
cycle_visited = set()
if idxs_grid[0] == idxs_grid[-1]:
    print(0)
    exit()
for i in range(1, n + 1):
    if i in cycle_visited:
        continue
    tmp = [i]
    nex = res[i - 1]
    cycle_visited.add(i)
    while nex != i:
        cycle_visited.add(nex)
        tmp.append(nex)
        nex = res[nex - 1]
    if len(tmp) > 1:
        cycles.append(tmp)
ans = sum(len(i) - 1 for i in cycles)
if ans > 3:
    print(-1)
    exit()
idxs_grid.extend(idxs_grid[-1][:] for _ in range(h + 1 - len(idxs_grid)))
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
promising_paths_for_cycle = []
promising_candidate = defaultdict(list)
for cycle in cycles:
    promising_paths_for_cycle.append(list(map(lambda x: tuple(map(lambda y: (cycle[y[0]], cycle[y[1]]) if cycle[y[0]] < cycle[y[1]] else (cycle[y[1]], cycle[y[0]]), x)), path_idxs[len(cycle) - 2])))
for paths in product(*promising_paths_for_cycle):
    
    perms_with_identical_elts = []
    for idx, val in enumerate(paths):
        perms_with_identical_elts += [idx]*len(val)
    perms_with_identical_elts = set(permutations(perms_with_identical_elts))

    for pattern in perms_with_identical_elts:
        paths_generator = [iter(i) for i in paths]
        path = tuple(next(paths_generator[i]) for i in pattern)
        for idx, step in enumerate(path):
            promising_candidate[path[:idx]].append(step)


def dfs(depth, start_row, start_col, path, idx_arr):
    for a, b in promising_candidate[path]:
        na, nb = idx_arr[a], idx_arr[b]
        for row in range(start_row, h + 1):
            if abs(idxs_grid[row][na] - idxs_grid[row][nb]) == 1:
                col = max(idxs_grid[row][na], idxs_grid[row][nb])
                if row == start_row and col < start_col:
                    continue
                if visited[row][col-1] == visited[row][col] == visited[row][col+1] == 0:
                    if depth + 1 == ans:
                        print(ans)
                        exit()
                    idx_arr[a], idx_arr[b] = idx_arr[b], idx_arr[a]
                    dfs(depth + 1, row, col + 2, path + ((a, b), ), idx_arr)
                    idx_arr[a], idx_arr[b] = idx_arr[b], idx_arr[a]

dfs(0, 1, 1, (), list(range(n + 1)))
# edge case for ans == 1 but need 3 transpositions(note that there are no 2-transpositions cases, since sign of permutation must be same)
if ans == 1:
    origin = list(range(1, n + 1))
    def brute_force(depth, start_row, start_col, idx_arr):
        global ans
        if depth >= 3:
            return
        for row, col in product(range(start_row, h + 1), range(1, n)):
            if row == start_row and col < start_col:
                continue
            if visited[row][col-1] == visited[row][col] == visited[row][col+1] == 0:
                a, b = idxs_grid[row].index(col - 1), idxs_grid[row].index(col)
                idx_arr[b], idx_arr[a] = idx_arr[a], idx_arr[b]
                if origin == [idx_arr[i] for i in res]:
                    print(3)
                    exit()
                brute_force(depth + 1, row, col + 2, idx_arr)
                idx_arr[b], idx_arr[a] = idx_arr[a], idx_arr[b]

    brute_force(0, 1, 1, list(range(n + 1)))
print(-1)