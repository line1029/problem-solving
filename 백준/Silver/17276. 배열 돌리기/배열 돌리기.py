from sys import stdin, stdout
from collections import deque


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, d = map(int, stdin.readline().split())
        grid = list(map(lambda x: list(map(int, x.split())), (stdin.readline() for __ in range(n))))
        d %= 360
        if d > 180:
            d -= 360
        rotation = abs(d) // 45
        digonals = deque(
            [
                [grid[i][i] for i in range(n)],
                [grid[i][n >> 1] for i in range(n)],
                [grid[i][n - i - 1] for i in range(n)],
                [grid[n >> 1][n - i - 1] for i in range(n)],
            ]
        )
        for _ in range(rotation):
            if d > 0:
                digonals.rotate(1)
                digonals[0] = list(reversed(digonals[0]))
            else:
                digonals.rotate(-1)
                digonals[-1] = list(reversed(digonals[-1]))
        for i in range(n):
            grid[i][i] = digonals[0][i]
            grid[i][n >> 1] = digonals[1][i]
            grid[i][n - i - 1] = digonals[2][i]
            grid[n >> 1][n - i - 1] = digonals[3][i]
        stdout.write("\n".join(" ".join(map(str, row)) for row in grid))
        stdout.write("\n")


main()