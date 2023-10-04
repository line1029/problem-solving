import io, os
from collections import deque
def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    e = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 48:
                si, sj = i, j
            if grid[i][j] == 49:
                e.add((i, j))
    visited = [[[0]*64 for _ in range(m)] for _ in range(n)]
    visited[si][sj][0] = 1
    q = deque([[si, sj, 0]])
    for step in range(100000):
        if not q: break
        for _ in range(len(q)):
            i, j, k = q.popleft()
            for di, dj in D:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if visited[ni][nj][k] or grid[ni][nj] == 35 or (65 <= grid[ni][nj] <= 70 and not k&(1 << (grid[ni][nj] - 65))):
                        continue
                    if (ni, nj) in e:
                        print(step + 1)
                        exit()
                    nk = k
                    if 97 <= grid[ni][nj] <= 102:
                        nk |= (1 << (grid[ni][nj] - 97))
                    visited[ni][nj][k] = visited[ni][nj][nk] = 1
                    q.append([ni, nj, nk])
    print(-1)
main()