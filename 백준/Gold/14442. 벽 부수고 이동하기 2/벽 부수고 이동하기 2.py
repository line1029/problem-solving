from sys import stdin
from collections import deque
D = ((0, 1), (0, -1), (1, 0), (-1, 0))
INF = 1000001
n, m, k = map(int, stdin.readline().split())
if n == m == 1:
    print(1)
    exit()
m += 2
grid = [2]*m
visited = [k + 1]*(m*(n + 2))
visited[:m] = [-1]*m
visited[-m:] = [-1]*m
for i in range(n):
    grid.append(2)
    grid.extend(map(int, stdin.readline().strip()))
    grid.append(2)
    visited[m*(i + 1)] = visited[m*(i + 2) - 1] = -1
grid += [2]*m
q = deque([[m + 1, 0]])
end = m*(n + 1) - 2
for step in range(m*n + 1):
    if not q:
        break
    for _ in range(len(q)):
        cur, eli = q.popleft()
        if cur == end:
            print(step + 1)
            exit()
        if visited[cur - 1] > eli + grid[cur - 1]:
            visited[cur - 1] = eli + grid[cur - 1]
            q.append((cur - 1, eli + grid[cur - 1]))
        if visited[cur + 1] > eli + grid[cur + 1]:
            visited[cur + 1] = eli + grid[cur + 1]
            q.append((cur + 1, eli + grid[cur + 1]))
        if visited[cur + m] > eli + grid[cur + m]:
            visited[cur + m] = eli + grid[cur + m]
            q.append((cur + m, eli + grid[cur + m]))
        if visited[cur - m] > eli + grid[cur - m]:
            visited[cur - m] = eli + grid[cur - m]
            q.append((cur - m, eli + grid[cur - m]))
print(-1)