from sys import stdin
s = [0]*27
def check(num, i, j):
    if s[i] & (1 << num):
        return False
    if s[9 + j] & (1 << num):
        return False
    if s[18 + i//3*3 + j//3] & (1 << num):
        return False
    return True

sudoku = list(map(lambda x: list(map(int, x)), stdin.read().splitlines()))
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j]:
            s[i] |= 1 << sudoku[i][j]
            s[9 + j] |= 1 << sudoku[i][j]
            s[18 + i//3*3 + j//3] |= 1 << sudoku[i][j]
        else:
            blank.append((i, j))
n = len(blank) - 1

def dfs(depth):
    i, j = blank[depth]
    for num in range(1, 10):
        if check(num, i, j):
            sudoku[i][j] = num
            if depth == n:
                print("\n".join("".join(map(str, row)) for row in sudoku))
                exit()
            s[i] |= 1 << num
            s[9 + j] |= 1 << num
            s[18 + i//3*3 + j//3] |= 1 << num
            dfs(depth + 1)
            s[i] &= ~(1 << num)
            s[9 + j] &= ~(1 << num)
            s[18 + i//3*3 + j//3] &= ~(1 << num)
            sudoku[i][j] = 0

dfs(0)
