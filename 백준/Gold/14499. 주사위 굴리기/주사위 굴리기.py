from sys import stdin
def main():
    n, m, x, y, k = map(int, stdin.readline().split())
    grid = [stdin.readline().split() for _ in range(n)]
    D = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dice = ["0"]*6
    dice_idx = [
        [2, 4, 3, 1], [2, 0, 3, 5], [5, 4, 0, 1],
        [0, 4, 5, 1], [2, 5, 3, 0], [2, 1, 3, 4]
    ]
    dice_top = [5, 4, 3, 2, 1, 0]
    dd = [0, 0, 2, 3, 1]
    cur_bottom = 5
    cur_east = 0
    ans = []
    for d_idx in map(lambda x: dd[int(x)], stdin.readline().split()):
        dx, dy = D[d_idx]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            nex_bottom = dice_idx[cur_bottom][(cur_east + d_idx)%4]
            cur_east = (dice_idx[nex_bottom].index(cur_bottom) - (d_idx + 2))%4
            cur_bottom = nex_bottom
            if grid[nx][ny] != "0":
                dice[cur_bottom] = grid[nx][ny]
                grid[nx][ny] = "0"
            else:
                grid[nx][ny] = dice[cur_bottom]
            x = nx
            y = ny
            ans.append(dice[dice_top[cur_bottom]])
    print("\n".join(ans))
main()