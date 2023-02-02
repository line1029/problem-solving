from sys import stdin
n = int(stdin.readline())
min_grid = list(map(int, stdin.readline().split()))
max_grid = min_grid[:]
for _ in range(n - 1):
    a, b, c = map(int, stdin.readline().split())
    min_grid = [min(min_grid[0], min_grid[1]) + a,
                min(min_grid[0], min_grid[1], min_grid[2]) + b,
                min(min_grid[1], min_grid[2]) + c]
    max_grid = [max(max_grid[0], max_grid[1]) + a,
                max(max_grid[0], max_grid[1], max_grid[2]) + b,
                max(max_grid[1], max_grid[2]) + c]
print(max(max_grid), min(min_grid))