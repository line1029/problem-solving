from sys import stdin
import heapq
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
def dijkstra(n, grid):
    dist = [[1000000]*n for _ in range(n)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    while pq:
        cur, i, j = heapq.heappop(pq)
        if cur > dist[i][j]:
            continue
        if i == j == n - 1:
            return dist[i][j]
        for di, dj in D:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<n and dist[ni][nj] > cur + grid[ni][nj]:
                dist[ni][nj] = cur + grid[ni][nj]
                heapq.heappush(pq, (dist[ni][nj], ni, nj))
ans = []
p = 1
while True:
    n = int(stdin.readline())
    if not n:
        break
    grid = [list(map(int, stdin.readline().split())) for _ in range(n)]
    ans.append(f"Problem {p}: {dijkstra(n, grid)}")
    p += 1
print("\n".join(ans))