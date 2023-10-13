from sys import stdin
n = int(stdin.readline())
dragons = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
G = max(i[3] for i in dragons)
D = ((0, 1), (-1, 0), (0, -1), (1, 0))
curve_direction = [0]
for i in range(G):
    curve_direction += list(map(lambda x: (x + 1)%4, curve_direction[::-1]))
grid = [[0]*101 for _ in range(101)]
for x, y, d, g in dragons:
    grid[y][x] = 1
    for i in range(1 << g):
        dy, dx = D[(d + curve_direction[i])%4]
        x, y = x + dx, y + dy
        grid[y][x] = 1
ans = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == grid[i + 1][j] == grid[i][j + 1] == grid[i + 1][j + 1] == 1:
            ans += 1
print(ans)