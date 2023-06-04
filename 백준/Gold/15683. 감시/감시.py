from sys import stdin
from itertools import product
n, m = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
cctvs = sorted(((grid[i][j], i, j) for j in range(m) for i in range(n) if 0 < grid[i][j] < 6), reverse=True)
direc = ((-1, 0), (0, -1), (1, 0), (0, 1))
cctv_kind_map = {
    1:[[0], [1], [2], [3]],
    2:[[0, 2], [1, 3]],
    3:[[0, 1], [1, 2], [2, 3], [3, 0]],
    4:[[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5:[0, 1, 2, 3]
}


def mark_view(grid, i, j, direc_idx):
    coor = set()
    for idx in direc_idx:
        di, dj = direc[idx]
        ni, nj = i + di, j + dj
        while 0 <= ni < n and 0 <= nj < m:
            if grid[ni][nj] == 6:
                break
            if not grid[ni][nj]:
                coor.add((ni, nj))
            ni += di
            nj += dj
    return coor


total_zeros = sum(i.count(0) for i in grid)
if not cctvs:
    print(total_zeros)
    exit()
for five_idx, (cctv_kind, i, j) in enumerate(cctvs):
    if cctv_kind != 5:
        break
    for ni, nj in mark_view(grid, i, j, cctv_kind_map[5]):
        total_zeros -= 1
        grid[ni][nj] = -1
else:
    print(total_zeros)
    exit()
ans = total_zeros
candidates = []
for idx in range(five_idx, len(cctvs)):
    cctv_kind, i, j = cctvs[idx]
    tmp = []
    for pattern in cctv_kind_map[cctv_kind]:
        tmp.append(mark_view(grid, i, j, pattern))
    candidates.append(tmp)
for candidate in product(*candidates):
    ans = min(ans, total_zeros - len(set().union(*candidate)))
print(ans)
