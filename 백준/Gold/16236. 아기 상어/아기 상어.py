from sys import stdin
from collections import deque
direc = ((-1, 0), (0, -1), (0, 1), (1, 0))
def bfs(baby_shark, grid, n, size):
    visited = [[int(val > size) for val in row] for row in grid]
    q = deque([baby_shark])
    depth = 0
    candidates = []
    while q:
        depth += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in direc:
                ni, nj = i+di, j+dj
                if 0<=ni<n and 0<=nj<n and not visited[ni][nj]:
                    if 0 < grid[ni][nj] < min(7, size):
                        candidates.append((ni, nj))
                    elif grid[ni][nj] == 0 or grid[ni][nj] == size:
                        q.append((ni, nj))
                    visited[ni][nj] = 1
        if candidates:
            candidates.sort()
            return candidates[0], depth
    return (0, 0), 0

n = int(stdin.readline())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            cur_baby = (i, j)
            break
    else:
        continue
    break
ans = 0
size = 2
ate = 0
depth = 1
while True:
    prev_baby = cur_baby
    cur_baby, depth = bfs(cur_baby, grid, n, size)
    if not depth:
        break
    grid[prev_baby[0]][prev_baby[1]] = 0
    grid[cur_baby[0]][cur_baby[1]] = 9
    ate += 1
    if ate == size:
        size += 1
        ate = 0
    ans += depth

print(ans)