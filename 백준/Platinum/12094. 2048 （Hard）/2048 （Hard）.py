from sys import stdin
from math import log2
def move(grid, d):
    nex = [0]*(n*n)
    # d = 0, 1, 2, 3 -> 상, 좌, 하, 우
    if d & 1:
        for i in range(n):
            prev = 0
            nums = []
            for j in range(n*i, n*(i + 1)) if d==1 else range(n*(i + 1) - 1, n*i - 1, - 1):
                if grid[j] == 0: continue
                if not prev:
                    prev = grid[j]
                elif prev == grid[j]:
                    nums.append(prev << 1)
                    prev = 0
                else:
                    nums.append(prev)
                    prev = grid[j]
            if prev:
                nums.append(prev)
            k = len(nums)
            if d == 1:
                nex[i*n:i*n + k] = nums
            else:
                nex[(i + 1)*n - k:(i + 1)*n] = reversed(nums)
    else:
        for j in range(n):
            prev = 0
            nums = []
            for i in range(n) if not d else range(n - 1, -1, -1):
                num = grid[n*i + j]
                if not num: continue
                if not prev:
                    prev = num
                elif prev == num:
                    nums.append(prev << 1)
                    prev = 0
                else:
                    nums.append(prev)
                    prev = num
            if prev:
                nums.append(prev)
            k = len(nums)
            if d == 0:
                for i in range(n):
                    if i < k:
                        nex[i*n + j] = nums[i]
                    else:
                        break
            else:
                for i in range(n):
                    if i < k:
                        nex[(n - 1 - i)*n + j] = nums[i]
                    else:
                        break
    return nex


def dfs(depth, grid, maxval):
    global ans
    if maxval <= (ans >> (10 - depth)):
        return
    if depth == 10:
        ans = max(ans, maxval)
        if ans == possible_max:
            print(ans)
            exit()
        return
    for i in range(4):
        nex = move(grid, i)
        if grid == nex:
            continue
        dfs(depth + 1, nex, max(nex))


n = int(stdin.readline())
grid = []
for _ in range(n):
    grid.extend(map(int, stdin.readline().split()))
ans = maxval = max(grid)
possible_max = (1 << int(log2(sum(grid))))
dfs(0, grid, maxval)
print(ans)
