from sys import stdin, stdout
h, w = map(int, stdin.readline().split())
sky = stdin.read().splitlines()
grid = [[-1]*w for _ in range(h)]
for i in range(h):
    if sky[i][0] == "c":
        grid[i][0] = 0
    for j in range(1, w):
        if sky[i][j] == "c":
            grid[i][j] = 0
            continue
        if grid[i][j - 1] == -1:
            continue
        grid[i][j] = grid[i][j - 1] + 1
stdout.write("\n".join(" ".join(map(str, row)) for row in grid))
