from sys import stdin
D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n, l, r = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
visited = [[-1]*n for _ in range(n)]
for ans in range(2001):
    populations = [0]*(n*n)
    nations = [0]*(n*n)
    for row in range(n):
        for col in range(n):
            if visited[row][col] == -1:
                marker = row*n + col
                total = grid[row][col]
                cnt = 1
                visited[row][col] = marker
                stack = [[row, col]]
                for _ in range(n*n + 1):
                    if not stack: break
                    i, j = stack.pop()
                    for di, dj in D:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == -1 and l <= abs(grid[i][j] - grid[ni][nj]) <= r:
                            visited[ni][nj] = marker
                            stack.append([ni, nj])
                            total += grid[ni][nj]
                            cnt += 1
                populations[marker] = total
                nations[marker] = cnt
    if max(nations) == 1:
        print(ans)
        exit()
    for row in range(n):
        for col in range(n):
            if nations[row*n + col] > 1:
                altered_pop = populations[row*n + col]//nations[row*n + col]
                marker = visited[row][col]
                stack = [[row, col]]
                grid[row][col] = altered_pop
                visited[row][col] = -1
                for _ in range(n*n + 1):
                    if not stack: break
                    i, j = stack.pop()
                    for di, dj in D:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == marker:
                            visited[ni][nj] = -1
                            grid[ni][nj] = altered_pop
                            stack.append([ni, nj])
            else:
                visited[row][col] = -1