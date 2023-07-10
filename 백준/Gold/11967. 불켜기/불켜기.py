from sys import stdin
def main():
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    n, m = map(int, stdin.readline().split())
    grid = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    grid[0][0] = visited[0][0] = 1
    graph = [[[] for _ in range(n)] for _ in range(n)]
    for x, y, a, b in map(lambda z: map(lambda w: int(w) - 1, z.split()), stdin.read().splitlines()):
        graph[x][y].append((a, b))
    q =[(0, 0)]
    while q:
        i, j = q.pop()
        for a, b in graph[i][j]:
            if grid[a][b]: continue
            grid[a][b] = 1
            for da, db in D:
                na, nb = a + da, b + db
                if 0 <= na < n and 0 <= nb < n and visited[na][nb]:
                    visited[a][b] = 1
                    q.append((a, b))
                    break
        for di, dj in D:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))
    print(sum(map(sum, grid)))
main()