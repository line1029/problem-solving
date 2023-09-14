from sys import stdin
from itertools import product
def main():
    dice = list(map(int, stdin.readline().split()))
    grid = [0]*200
    grid[0:21] = [-1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
    grid[26:33] = [13, 16, 19, 25, 30, 35, 40]
    grid[51:57] = [22, 24, 25, 30, 35, 40]
    grid[76:83] = [28, 27, 26, 25, 30, 35, 40]
    turns_blue = [5, 10, 15]
    turns_25 = [29, 53]
    turns_30 = [30, 54]
    turns_35 = [31, 55]
    turns_40 = [20, 32, 56]
    ans = 0
    for pat in product(range(4), repeat=10):
        score = 0
        positions = [0]*4
        for idx, horse in enumerate(pat):
            if not grid[positions[horse]]:
                break
            if positions[horse] in turns_blue:
                positions[horse] = positions[horse]*5
            if grid[positions[horse] + dice[idx]] and positions[horse] + dice[idx] in positions:
                break
            positions[horse] += dice[idx]
            score += grid[positions[horse]]
            if positions[horse] in turns_25:
                if 79 in positions:
                    break
                positions[horse] = 79
            if positions[horse] in turns_30:
                if 80 in positions:
                    break
                positions[horse] = 80
            if positions[horse] in turns_35:
                if 81 in positions:
                    break
                positions[horse] = 81
            if positions[horse] in turns_40:
                if 82 in positions:
                    break
                positions[horse] = 82
        else:
            ans = max(ans, score)
    print(ans)
main()