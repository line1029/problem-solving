from sys import stdin
n, k = map(int, stdin.readline().split())
grid = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(lambda x: int(x) - 1, stdin.readline().split())
    grid[a][b] = 1
    grid[b][a] = -1
s = int(stdin.readline())
for k in range(n):
    for i in range(n):
        for j in range(n):
            if grid[i][k] == grid[k][j] == 1:
                grid[i][j] = 1
                grid[j][i] = -1
ans = [0]*s
for i, (a, b) in enumerate(map(lambda x: map(lambda y: int(y) - 1, x.split()), stdin.read().splitlines())):
    ans[i] = grid[b][a]
print("\n".join(map(str, ans)))