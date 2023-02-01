import sys
n, m = map(int, sys.stdin.readline().split())
mat = [[0]*m for _ in range(n)]
for i in range(n):
    row = map(int, sys.stdin.readline().split())
    for j, num in enumerate(row):
        mat[i][j] += num
for i in range(n):
    row = map(int, sys.stdin.readline().split())
    for j, num in enumerate(row):
        mat[i][j] += num
for row in mat:
    print(" ".join(map(str, row)))