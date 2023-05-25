# Quad Tree
from sys import stdin, stdout
from itertools import islice
n = int(stdin.readline())
data = stdin.read().splitlines()
ans = []
def rec(row, col, m):
    if m == 1:
        ans.append(data[row][col])
        return
    standard = data[row][col]
    for i in range(row, row + m):
        for j in range(col, col + m):
            if data[i][j] != standard:
                ans.append("(")
                for k in range(2):
                    for l in range(2):
                        rec(row + k*m//2, col + l*m//2, m//2)
                ans.append(")")
                return
    ans.append(standard)
rec(0, 0, n)
print("".join(ans))