from sys import stdin, stdout


def main(n, k):
    d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    grid = [[0] * n for _ in range(n)]
    x = y = n >> 1
    grid[x][y] = cur = 1
    ans = [x + 1, y + 1]
    idx = 0
    for level in range(1, n + 1):
        dx, dy = d[idx]
        for i in range(level):
            x += dx
            y += dy
            cur += 1
            grid[x][y] = cur
            if k == cur:
                ans = [x + 1, y + 1]
            if cur == n * n and n == i + 2:
                stdout.write("\n".join(" ".join(map(str, row)) for row in grid))
                stdout.write(f"\n{ans[0]} {ans[1]}")
                return
        idx = (idx + 1) % 4
        dx, dy = d[idx]
        for i in range(level):
            x += dx
            y += dy
            cur += 1
            grid[x][y] = cur
            if k == cur:
                ans = [x + 1, y + 1]
        idx = (idx + 1) % 4


if __name__ == "__main__":
    main(*map(int, stdin.readlines()))
