from sys import stdin
def main():
    n = int(stdin.readline())
    grid = stdin.read().splitlines()
    k = int(grid.pop())
    if k == 2:
        for i in range(n):
            grid[i] = grid[i][::-1]
    elif k == 3:
        grid = grid[::-1]
    print("\n".join(grid))
main()
