from sys import stdin
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
n= int(stdin.readline())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
ans = 0
for rain in range(max(map(max, grid))):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for row in range(n):
        for col in range(n):
            if not visited[row][col] and grid[row][col] > rain:
                stack = [(row, col)]
                visited[row][col] = 1
                cnt += 1
                while stack:
                    i, j = stack.pop()
                    for di, dj in D:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] > rain:
                            visited[ni][nj] = 1
                            stack.append((ni, nj))
    ans = max(ans, cnt)
print(ans)
                    
            