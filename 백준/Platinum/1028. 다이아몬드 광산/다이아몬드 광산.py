from sys import stdin
r, c = map(int, stdin.readline().split())
grid = [stdin.readline().rstrip() for _ in range(r)]
down_right = [[0]*c for _ in range(r)]
down_left = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if grid[i][j] == "0":
            continue
        if i and j:
            down_right[i][j] = down_right[i - 1][j - 1] + 1
        else:
            down_right[i][j] = 1
        if i and j < c - 1:
            down_left[i][j] = down_left[i - 1][j + 1] + 1
        else:
            down_left[i][j] = 1
max_size = (min(r, c) + 1) >> 1
ans = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == "0":
            continue
        _size = min(down_left[i][j], down_right[i][j])
        if _size <= ans:
            continue
        for k in range(_size, 0, -1):
            if min(down_left[i - k + 1][j - k + 1], down_right[i - k + 1][j + k - 1]) >= k:
                ans = max(ans, k)
                break
            if k <= ans:
                break
print(ans)