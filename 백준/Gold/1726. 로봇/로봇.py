from sys import stdin
from collections import deque
def main():
    D = ((0, 1), (0, -1), (1, 0), (-1, 0))
    turn = ((2, 3), (3, 2), (1, 0), (0, 1))
    m, n = map(int, stdin.readline().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, stdin.readline().split())))
    start = list(map(lambda x: int(x) - 1, stdin.readline().split()))
    end = list(map(lambda x: int(x) - 1, stdin.readline().split()))
    if start == end:
        print(0)
        exit()
    visited = [[[0]*4 for _ in range(n)] for _ in range(m)]
    ans = 0
    q = deque([start])
    visited[start[0]][start[1]][start[2]] = 1
    while q:
        for _ in range(len(q)):
            i, j, d = q.popleft()
            di, dj = D[d]
            for k in range(1, 4):
                ni, nj = i + di*k, j + dj*k
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj]:
                        break
                    if not visited[ni][nj][d]:
                        visited[ni][nj][d] = 1
                        q.append((ni, nj, d))
                        if end == [ni, nj, d]:
                            print(ans + 1)
                            exit()
            for nd in turn[d]:
                if not visited[i][j][nd]:
                    visited[i][j][nd] = 1
                    q.append((i, j, nd))
                    if end == [i, j, nd]:
                        print(ans + 1)
                        exit()
        ans += 1

main()