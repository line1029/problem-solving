from sys import stdin
def move(grid, d):
    n = len(grid)
    grid = [i[:] for i in grid]
    # d = 0, 1, 2, 3 -> 상, 좌, 하, 우
    if d & 1:
        for i in range(n):
            prev = 0
            nums = []
            for num in grid[i] if d==1 else reversed(grid[i]):
                if num:
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
            if d == 1:
                grid[i][:k] = nums
                grid[i][k:] = [0]*(n - k)
            else:
                grid[i][-k:] = reversed(nums)
                grid[i][:-k] = [0]*(n - k)
    else:
        for j in range(n):
            prev = 0
            nums = []
            for i in range(n) if not d else range(n - 1, -1, -1):
                num = grid[i][j]
                if num:
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
                        grid[i][j] = nums[i]
                    else:
                        grid[i][j] = 0
            else:
                for i in range(n):
                    if i < k:
                        grid[-1-i][j] = nums[i]
                    else:
                        grid[-1-i][j] = 0
    return grid


def dfs(depth, grid):
    if depth == 5:
        return max(max(i) for i in grid)
    ans = []
    for i in range(4):
        ans.append(dfs(depth + 1, move(grid, i)))
    return max(ans)


def main():
    n = int(stdin.readline())
    grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
    print(dfs(0, grid))

main()
