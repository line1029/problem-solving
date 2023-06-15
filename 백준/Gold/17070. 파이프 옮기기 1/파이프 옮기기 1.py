from sys import stdin
n = int(stdin.readline())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
D = {0:((0, 1, 0), (1, 1, 2)), 1:((1, 0, 1), (1, 1, 2)), 2:((1, 0, 1), (1, 1, 2), (0, 1, 0))}
ans = 0
stack = [(0, 1, 0)]
while stack:
    i, j, d = stack.pop()
    if i == j == n - 1:
        ans += 1
    for di, dj, d_nex in D[d]:
        ni, nj = i + di, j + dj
        if 0<=ni<n and 0<=nj<n and not grid[ni][nj]:
            if d_nex == 2 and (grid[ni - 1][nj] or grid[ni][nj - 1]):
                continue
            stack.append((ni, nj, d_nex))
print(ans)