from sys import stdin, stdout
def main():
    r, c, q = map(int, stdin.readline().split())
    grid = [[0] for _ in range(r + 1)]
    for i in range(r):
        grid[i + 1].extend(map(int, stdin.readline().split()))
    grid[0] = [0]*(c + 1)
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            grid[i][j] += grid[i][j - 1]
        for j in range(1, c + 1):
            grid[i][j] += grid[i - 1][j]
    ans = [0]*q
    for i in range(q):
        r1, c1, r2, c2 = map(int, stdin.readline().split())
        ans[i] = (grid[r2][c2] - grid[r1 - 1][c2] - grid[r2][c1 - 1] + grid[r1 - 1][c1 - 1])
        ans[i] //= (r2 - r1 + 1)*(c2 - c1 + 1)
    stdout.write("\n".join(map(str, ans)))

main()