from sys import stdin
from collections import deque
def main():
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    n, m, t = map(int, stdin.readline().split())
    grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
    ans = gram = t + 1
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    q = deque([(0, 0)])
    for step in range(1, ans + 1):
        if not q:
            break
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in D:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and grid[ni][nj] != 1:
                    visited[ni][nj] = 1
                    if grid[ni][nj] == 2:
                        gram = step + n - ni + m - nj - 2
                    if ni == (n - 1) and nj == (m - 1):
                        ans = step
                    q.append((ni, nj))
    ans = min(ans, gram)
    if ans <= t:
        print(ans)
    else:
        print("Fail")
main()
