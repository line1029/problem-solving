from sys import stdin
n, m = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
visited = [[0]*m for _ in range(n)]
# can be checked by 4-depthed dfs check excopt ㅗㅜㅓㅏ
ans = 0
direc = ((0, 1), (0, -1), (1, 0), (-1, 0))
def dfs(i, j, depth, value):
    if depth == 4:
        global ans
        ans = max(ans, value)
        return
    for di, dj in direc:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj, depth + 1, value + grid[ni][nj])
            visited[ni][nj] = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, grid[i][j])
        visited[i][j] = 0
        if i + 2 < n:
            if j < m - 1:
                ans = max(ans, grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+1][j+1])
            if 0 < j:
                ans = max(ans, grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+1][j-1])
        if j + 2 < m:
            if i < n - 1:
                ans = max(ans, grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1])
            if 0 < i:
                ans = max(ans, grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i-1][j+1])
print(ans)