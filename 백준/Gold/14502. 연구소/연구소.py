from sys import stdin
from itertools import combinations
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, m = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
zeros = set((i, j) for i in range(n) for j in range(m) if not grid[i][j])
twos = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 2]
ans = 0
for (a1, a2), (b1, b2), (c1, c2) in combinations(zeros, 3):
    grid[a1][a2] = grid[b1][b2] = grid[c1][c2] = 1
    virus = set()
    for coor in twos:
        if coor not in virus:
            virus.add(coor)
            stack = [coor]
            while stack:
                i, j = stack.pop()
                for di, dj in D:
                    nex = (ni, nj) = i + di, j + dj
                    if 0<=ni<n and 0<=nj<m and grid[ni][nj] != 1 and nex not in virus:
                        virus.add(nex)
                        stack.append(nex)
    ans = max(ans, len(zeros) - len(virus) + len(twos) - 3)
    grid[a1][a2] = grid[b1][b2] = grid[c1][c2] = 0
print(ans)
