from sys import stdin
D = [[1, 0], [0, 1], [1, 1], [-1, 1], [1, -1], [-1, -1], [-1, 0], [0, -1]]
n, m, k = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
grid = [[[0]*(k + 12) for _ in range(n)] for _ in range(n)]
tmp_grid = [[[0]*(k + 12) for _ in range(n)] for _ in range(n)]
food = [[5]*n for _ in range(n)]
for x, y, z in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    grid[x - 1][y - 1][z] += 1
    grid[x - 1][y - 1][0] = z + 1
for _ in range(k):
    dead_trees = [[0]*n for _ in range(n)]
    # spring
    for i in range(n):
        for j in range(n):
            tmp_k = grid[i][j][0]
            for k in range(1, tmp_k):
                if grid[i][j][k] and grid[i][j][k]*k <= food[i][j]:
                    tmp_grid[i][j][k + 1] += grid[i][j][k]
                    food[i][j] -= grid[i][j][k]*k
                    grid[i][j][0] = k + 2
                elif grid[i][j][k]:
                    can_survive = food[i][j]//k
                    tmp_grid[i][j][k + 1] += can_survive
                    food[i][j] -= can_survive*k
                    dead_trees[i][j] += (grid[i][j][k] - can_survive)*(k//2)
                    if can_survive:
                        grid[i][j][0] = k + 2
                grid[i][j][k] = 0
            for k in range(1, grid[i][j][0]):
                grid[i][j][k] += tmp_grid[i][j][k]
                tmp_grid[i][j][k] = 0
    
    # summer
    for i in range(n):
        for j in range(n):
            food[i][j] += dead_trees[i][j]
    
    # fall
    for i in range(n):
        for j in range(n):
            for k in range(5, grid[i][j][0], 5):
                if grid[i][j][k]:
                    for di, dj in D:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            grid[ni][nj][1] += grid[i][j][k]
                            if not grid[ni][nj][0]:
                                grid[ni][nj][0] = 2
    
    # winter
    for i in range(n):
        for j in range(n):
            food[i][j] += a[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += sum(grid[i][j]) - grid[i][j][0]
print(ans)