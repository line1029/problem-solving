from sys import stdin
def main():
    n, m, k = map(int, stdin.readline().split())
    n += 1
    m += 1
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    grid = [[0]*m for _ in range(n)]
    for i, j in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
        grid[i][j] = 1
    ans = 0
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j]:
                grid[i][j] = 0
                st = [(i, j)]
                cnt = 1
                while st:
                    i, j = st.pop()
                    for di, dj in D:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj]:
                            grid[ni][nj] = 0
                            st.append((ni, nj))
                            cnt += 1
                ans = max(ans, cnt)
    print(ans)
main()