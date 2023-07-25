from sys import stdin
def main():
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    n, m, k = map(int, stdin.readline().split())
    grid = [[0]*n for _ in range(m)]
    for _ in range(k):
        i1, j1, i2, j2 = map(int, stdin.readline().split())
        for i in range(i1, i2):
            for j in range(j1, j2):
                grid[i][j] = 1
    ans = []
    for row in range(m):
        for col in range(n):
            if not grid[row][col]:
                cnt = 1
                grid[row][col] = 1
                st = [(row, col)]
                while st:
                    i, j = st.pop()
                    for di, dj in D:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and not grid[ni][nj]:
                            grid[ni][nj] = 1
                            st.append((ni, nj))
                            cnt += 1
                ans.append(cnt)
    ans.sort()
    print(len(ans))
    print(" ".join(map(str, ans)))    
main()