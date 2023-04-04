n = int(input())
op = input()
m = n*2 + 1
grid = [["#"]*m for _ in range(m)]
x = y = min_x = min_y = max_x = max_y = n
direc = ((1, 0), (0, -1), (-1, 0), (0, 1))
direc_idx = 0
grid[n][n] = "."
for char in op:
    if char == "L":
        direc_idx = (direc_idx - 1)%4
    elif char == "R":
        direc_idx = (direc_idx + 1)%4
    else:
        dy, dx = direc[direc_idx]
        y += dy
        x += dx
        grid[y][x] = "."
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)
print("\n".join("".join(row[min_x:max_x + 1]) for row in grid[min_y:max_y + 1]))