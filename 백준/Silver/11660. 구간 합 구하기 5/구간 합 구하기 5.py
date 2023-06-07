from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
grid = [list(map(int, stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(1, n):
        grid[i][j] += grid[i][j - 1]
for j in range(n):
    for i in range(1, n):
        grid[i][j] += grid[i - 1][j]
ans = []
for x1, y1, x2, y2 in map(lambda x: map(lambda y: int(y) - 1, x.split()), stdin.read().splitlines()):
    tmp = grid[x2][y2]
    if x1:
        tmp -= grid[x1 - 1][y2]
    if y1:
        tmp -= grid[x2][y1 - 1]
    if x1 and y1:
        tmp += grid[x1 - 1][y1 - 1]
    ans.append(tmp)
stdout.write("\n".join(map(str, ans)))