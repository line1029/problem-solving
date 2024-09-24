from sys import stdin


def main():
    D = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
    grid, direc = [], []
    for _ in range(4):
        arr = stdin.readline().split()
        grid.extend(map(int, arr[::2]))
        direc.extend(map(lambda x: int(x) - 1, arr[1::2]))
    res = [grid[0]]
    sp = grid[0] = 0

    def dfs(initial_grid: list, initial_direc: list, sp: int, cur_sum: int):
        grid = initial_grid[:]
        direc = initial_direc[:]

        # move fish
        for fish_num in range(1, 17):
            try:
                i = grid.index(fish_num)
            except ValueError:
                continue
            cur_d = direc[i]
            for nex_d in range(cur_d, cur_d + 8):
                nex_d %= 8
                x, y = i // 4, i % 4
                dx, dy = D[nex_d]
                nx, ny = x + dx, y + dy
                j = 4 * nx + ny
                if 0 <= nx < 4 and 0 <= ny < 4 and grid[j]:
                    direc[i] = nex_d
                    grid[i], grid[j] = grid[j], grid[i]
                    direc[i], direc[j] = direc[j], direc[i]
                    break

        # check shark can eat
        cur_d = direc[sp]
        x, y = sp // 4, sp % 4
        dx, dy = D[cur_d]
        for i in range(1, 4):
            nx, ny = x + i * dx, y + i * dy
            nex_sp = 4 * nx + ny
            if 0 <= nx < 4 and 0 <= ny < 4 and grid[nex_sp] != -1:
                cur_sum += grid[nex_sp]
                res[0] = max(res[0], cur_sum)
                grid[sp], grid[nex_sp] = grid[nex_sp], grid[sp]
                grid[sp], tmp = -1, grid[sp]
                dfs(grid, direc, nex_sp, cur_sum)
                grid[sp] = tmp
                grid[sp], grid[nex_sp] = grid[nex_sp], grid[sp]
                cur_sum -= grid[nex_sp]

    dfs(grid, direc, sp, res[0])
    print(res[0])


main()
