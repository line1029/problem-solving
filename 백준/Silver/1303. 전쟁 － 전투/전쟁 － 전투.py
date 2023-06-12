from sys import stdin
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
m, n = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
visited = [[0]*m for _ in range(n)]
ans = [0, 0]
for row in range(n):
    for col in range(m):
        if not visited[row][col]:
            cnt = 1
            standard = grid[row][col]
            stack = [(row, col)]
            visited[row][col] = 1
            while stack:
                i, j = stack.pop()
                for di, dj in D:
                    ni, nj = i + di, j + dj
                    if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and grid[ni][nj] == standard:
                        visited[ni][nj] = 1
                        cnt += 1
                        stack.append((ni, nj))
            if standard == "W":
                ans[0] += cnt*cnt
            else:
                ans[1] += cnt*cnt
print(*ans)