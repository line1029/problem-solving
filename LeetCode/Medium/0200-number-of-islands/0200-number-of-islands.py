class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and not visited[row][col]:
                    ans += 1
                    stack = [[row, col]]
                    visited[row][col] = 1
                    while stack:
                        i, j = stack.pop()
                        for di, dj in d:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] == "1":
                                visited[ni][nj] = 1
                                stack.append([ni, nj])
        return ans