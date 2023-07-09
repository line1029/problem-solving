from sys import stdin, stdout
def main():
    n, m = map(int, stdin.readline().split())
    grid = [[0] for _ in range(n + 1)]
    grid[0] = [0]*(m + 1)
    for i in range(1, n + 1):
        grid[i].extend(map(int, stdin.readline().split()))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            grid[i][j] += grid[i][j - 1]
        for j in range(1, m + 1):
            grid[i][j] += grid[i - 1][j]
    k = int(stdin.readline())
    ans = [0]*k
    for i in range(k):
        x1, y1, x2, y2 = map(int, stdin.readline().split())
        ans[i] = grid[x2][y2] - grid[x1 - 1][y2] - grid[x2][y1 - 1] + grid[x1 - 1][y1 - 1]
    stdout.write("\n".join(map(str, ans)))

main()