from sys import stdin
def delete_row(grid, row_idx):
    grid.pop(row_idx)
    grid.insert(0, [0, 0, 0, 0])


def down(grid, t, col):
    ground = 6
    for i in range(6):
        if grid[i][col]:
            ground = i
            break
    if t == 2:
        for i in range(6):
            if grid[i][col + 1]:
                ground = min(ground, i)
                break
    grid[ground - 1][col] = 1
    if t == 2:
        grid[ground - 1][col + 1] = 1
    if t == 3:
        grid[ground - 2][col] = 1


def get_complete_row(grid):
    for i in range(2, 6):
        if sum(grid[i]) == 4:
            return i


def is_overflow(grid):
    return sum(grid[1])


green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]
score = 0

n = int(stdin.readline())
blocks = map(lambda x: map(int, x.split()), stdin.read().splitlines())
for t, x, y in blocks:
    down(green, t, y)
    if t != 1:
        t = 4 * t % 5
    down(blue, t, x)
    for _ in range(2):
        row_idx_green = get_complete_row(green)
        if row_idx_green is not None:
            score += 1
            delete_row(green, row_idx_green)
        row_idx_blue = get_complete_row(blue)
        if row_idx_blue is not None:
            score += 1
            delete_row(blue, row_idx_blue)
    while is_overflow(green):
        delete_row(green, -1)
    while is_overflow(blue):
        delete_row(blue, -1)
print(score)
print(sum(sum(i) for i in green) + sum(sum(i) for i in blue))