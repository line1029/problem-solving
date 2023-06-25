from sys import stdin
from collections import deque
# * -> 42, $ -> 36, . -> 46, A~Z -> 65~90, a~z -> 97~122
D = ((0, 1), (1, 0), (-1, 0), (0, -1))
def bfs(grid, h, w, keys):
    ans = 0
    locked_doors = [[] for _ in range(26)]
    visited = [[0]*w for _ in range(h)]
    q = deque([(0, 0)])
    visited[0][0] = 1
    while q:
        i, j = q.popleft()
        for di, dj in D:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and grid[ni][nj] != 42:
                if grid[ni][nj] == 36:
                    grid[ni][nj] = 46
                    ans += 1
                if 65 <= grid[ni][nj] <= 90:
                    if keys & (1 << (grid[ni][nj] - 65)):
                        grid[ni][nj] = 46
                    else:
                        locked_doors[grid[ni][nj] - 65].append((ni, nj))
                        continue
                if 97 <= grid[ni][nj] <= 122:
                    if keys & (1 << (grid[ni][nj] - 97)):
                        grid[ni][nj] = 46
                    else:
                        keys |= (1 << (grid[ni][nj] - 97))
                        q.extend(locked_doors[grid[ni][nj] - 97])
                        for x, y in locked_doors[grid[ni][nj] - 97]:
                            visited[x][y] = 1
                        grid[ni][nj] = 46
                q.append((ni, nj))
                visited[ni][nj] = 1
    return ans

def main():
    h, w = map(int, stdin.readline().split())
    grid = [[46]*(w + 2)]
    grid.extend([46] for _ in range(h))
    grid.append([46]*(w + 2))
    for i in range(1, h + 1):
        grid[i].extend(map(ord, stdin.readline().strip()))
        grid[i].append(46)
    keys = 0
    for char in stdin.readline().strip():
        if char == "0":
            break
        keys |= (1 << (ord(char) - 97))
    return bfs(grid, h + 2, w + 2, keys)

for _ in range(int(stdin.readline())):
    print(main())