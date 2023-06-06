from sys import stdin
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
r, c = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
letters = 1 << (ord(grid[0][0]) - 65)
ans = 1
def dfs(depth, i, j):
    if depth == 26:
        print(26)
        exit()
    global ans, letters
    ans = max(ans, depth)
    for di, dj in D:
        ni, nj = i + di, j + dj
        if 0<=ni<r and 0<=nj<c:
            idx = ord(grid[ni][nj]) - 65
            if not (letters & (1 << idx)):
                letters |= (1 << idx)
                dfs(depth + 1, ni, nj)
                letters &= ~(1 << idx)
dfs(1, 0, 0)
print(ans)