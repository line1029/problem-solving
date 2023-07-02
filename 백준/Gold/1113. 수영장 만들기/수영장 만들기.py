from sys import stdin
from collections import deque
def main():
    D = ((0, 1), (0, -1), (1, 0), (-1, 0))
    n, m = map(int, stdin.readline().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, stdin.readline().strip())))
    ans = 0
    for num in range(2, 10):
        visited = [[0]*m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if not visited[row][col] and grid[row][col] < num:
                    area = 0
                    q = deque([(row, col)])
                    flag = True
                    visited[row][col] = 1
                    while q:
                        i, j = q.popleft()
                        area += 1
                        if not i or not j or i == n - 1 or j == m - 1:
                            flag = False
                        for di, dj in D:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and grid[ni][nj] < num:
                                visited[ni][nj] = 1
                                q.append((ni, nj))
                    if flag:
                        ans += area
    print(ans)

main()