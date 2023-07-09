from sys import stdin, setrecursionlimit
setrecursionlimit(2501)
def main():
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    n, m = map(int, stdin.readline().split())
    grid = list(map(lambda x: list(map(lambda y: int(y) if y.isdigit() else y, x)), stdin.read().splitlines()))
    memo = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    def dfs(i, j):
        if memo[i][j]:
            return memo[i][j]
        if visited[i][j]:
            print(-1)
            exit()
        visited[i][j] = 1
        tmp = 0
        for di, dj in D:
            ni, nj = i + grid[i][j]*di, j + grid[i][j]*dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != "H":
                tmp = max(tmp, dfs(ni, nj) + 1)
            else:
                tmp = max(tmp, 1)
        visited[i][j] = 0
        memo[i][j] = tmp
        return tmp

    print(dfs(0, 0))

main()