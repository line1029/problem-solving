from sys import stdin
n, l = map(int, stdin.readline().split())
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
x = []
ans = 0
for i in range(n):
    used = [0]*n
    for j, val in enumerate(grid[i]):
        if not j: continue
        if abs(val - grid[i][j - 1]) > 1:
            break
        elif val > grid[i][j - 1]:
            if j - l < 0: break
            for k in range(j - l, j):
                if used[k] or grid[i][j - 1] != grid[i][k]:
                    break
                used[k] = 1
            else:
                continue
            break
        elif val < grid[i][j - 1]:
            if j + l > n: break
            for k in range(j, j + l):
                if used[k] or grid[i][j] != grid[i][k]:
                    break
                used[k] = 1
            else:
                continue
            break
    else:
        ans += 1
    used = [0]*n
    for j in range(n):
        if not j: continue
        if abs(grid[j][i] - grid[j - 1][i]) > 1:
            break
        elif grid[j][i] > grid[j - 1][i]:
            if j - l < 0: break
            for k in range(j - l, j):
                if used[k] or grid[j - 1][i] != grid[k][i]:
                    break
                used[k] = 1
            else:
                continue
            break
        elif grid[j][i] < grid[j - 1][i]:
            if j + l > n: break
            for k in range(j, j + l):
                if used[k] or grid[j][i] != grid[k][i]:
                    break
                used[k] = 1
            else:
                continue
            break
    else:
        ans += 1
print(ans)
