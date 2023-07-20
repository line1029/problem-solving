from sys import stdin
n, m, k = map(int, stdin.readline().split())
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
grid = []
for _ in range(n):
    grid.append(stdin.readline().strip())
word = stdin.readline().strip()
l = len(word)
memo = [[[-1]*l for _ in range(m)] for _ in range(n)]
def dfs(depth, row, col):
    if memo[row][col][depth] != -1:
        return memo[row][col][depth]
    if depth == l - 1:
        return 1
    cnt = 0
    for dr, dc in D:
        for multiplier in range(1, k + 1):
            nr, nc = row + dr*multiplier, col + dc*multiplier
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == word[depth + 1]:
                cnt += dfs(depth + 1, nr, nc)
    memo[row][col][depth] = cnt
    return cnt
ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == word[0]:
            ans += dfs(0, i, j)
print(ans)
