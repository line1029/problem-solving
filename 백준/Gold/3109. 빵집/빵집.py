from sys import stdin
r, c = map(int, stdin.readline().split())
grid = list(map(list, stdin.read().splitlines()))
ans = 0
for row in range(r):
    if grid[row][0] == ".":
        stack = [(row, 0)]
        while stack:
            i, j = stack.pop()
            grid[i][j] = "x"
            if j == c - 1:
                ans += 1
                break
            if i < r - 1 and grid[i + 1][j + 1] == ".":
                stack.append((i + 1, j + 1))
            if grid[i][j + 1] == ".":
                stack.append((i, j + 1))
            if i and grid[i - 1][j + 1] == ".":
                stack.append((i - 1, j + 1))

print(ans)