from sys import stdin, stdout

h, w, x, y = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.readlines()))
for i in range(x, h):
    for j in range(y, w):
        grid[i][j] -= grid[i - x][j - y]
stdout.write("\n".join(" ".join(map(str, row[:w])) for row in grid[:h]))
