from sys import stdin
def main():
    D = ((0, 1), (0, -1), (1, 0), (-1, 0))
    n, m = map(int, stdin.readline().split())
    grid = stdin.read().splitlines()
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                st = [(i, j, i, j)]
                color = grid[i][j]
                visited[i][j] = 1
                while st:
                    pi, pj, ci, cj = st.pop()
                    for di, dj in D:
                        ni, nj = ci + di, cj + dj
                        if ni == pi and nj == pj : continue
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == color:
                            if visited[ni][nj]:
                                print("Yes")
                                exit()
                            visited[ni][nj] = 1
                            st.append((ci, cj, ni, nj))
    print("No")
main()