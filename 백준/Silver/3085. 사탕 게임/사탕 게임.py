from sys import stdin
input = stdin.readline

n = int(input())
grid = list(map(list, stdin.read().splitlines()))

def longest_candy(idx, is_row=True):
    res = 1
    standard = grid[idx][0] if is_row else grid[0][idx]
    cur = 1
    if is_row:
        for i in range(1, n):
            if grid[idx][i] == standard:
                cur += 1
                res = max(res, cur)
            else:
                standard = grid[idx][i]
                cur = 1
    else:
        for i in range(1, n):
            if grid[i][idx] == standard:
                cur += 1
                res = max(res, cur)
            else:
                standard = grid[i][idx]
                cur = 1
    return res

ans = 1
for i in range(n):
    ans = max(ans, longest_candy(i), longest_candy(i, False))

for i in range(n):
    for j in range(n - 1):
        grid[i][j], grid[i][j + 1] = grid[i][j + 1], grid[i][j]
        ans = max(ans, longest_candy(i), longest_candy(j, False), longest_candy(j + 1, False))
        grid[i][j], grid[i][j + 1] = grid[i][j + 1], grid[i][j]

        grid[j][i], grid[j + 1][i] = grid[j + 1][i], grid[j][i]
        ans = max(ans, longest_candy(i, False), longest_candy(j), longest_candy(j + 1))
        grid[j][i], grid[j + 1][i] = grid[j + 1][i], grid[j][i]

print(ans)