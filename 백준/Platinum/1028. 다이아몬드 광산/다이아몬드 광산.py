from sys import stdin
r, c = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x)), stdin.read().splitlines()))
if not max(max(i) for i in grid):
    print(0)
    exit()
down_right = [i[:] for i in grid]
down_left = [i[:] for i in grid]
for i in range(1, r):
    for j in range(c):
        if grid[i][j]:
            if j:
                down_right[i][j] = down_right[i - 1][j - 1] + 1
            if j < c - 1:
                down_left[i][j] = down_left[i - 1][j + 1] + 1
max_size = (min(r, c) + 1) >> 1
ans = 1
for i in range(r):
    for j in range(c):
        _size = min(down_left[i][j], down_right[i][j])
        if _size <= ans:
            continue
        for k in range(_size - 1, 0, -1):
            if min(down_left[i - k][j - k], down_right[i - k][j + k]) >= k + 1:
                ans = max(ans, k + 1)
                break
            if k < ans:
                break
print(ans)