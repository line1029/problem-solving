from sys import stdin, stdout
n, k = map(int, stdin.read().splitlines())
grid = [[0]*n for _ in range(n)]
for s in range((n >> 1) + 1):
    num = (n - s*2)**2
    for i in range(s, n - s):
        if num == k:
            ans = f"\n{i + 1} {s + 1}"
        grid[i][s] = num
        num -= 1
    for j in range(s + 1, n - s):
        if num == k:
            ans = f"\n{n - s} {j + 1}"
        grid[n - s - 1][j] = num
        num -= 1
    for i in range(n - s - 2, s - 1, -1):
        if num == k:
            ans = f"\n{i + 1} {n - s}"
        grid[i][n - s - 1] = num
        num -= 1
    for j in range(n - s - 2, s, -1):
        if num == k:
            ans = f"\n{s + 1} {j + 1}"
        grid[s][j] = num
        num -= 1
stdout.write("\n".join(" ".join(map(str, row)) for row in grid))
stdout.write(ans)