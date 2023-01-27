from sys import stdin
n, m = map(int, stdin.readline().split())
mat = [[float("inf")]*n for _ in range(n)]
for i in range(n):
    mat[i][i] = 0
for _ in range(m):
    i, j = map(lambda x: int(x) - 1, stdin.readline().split())
    mat[i][j] = mat[j][i] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if mat[i][j] > mat[i][k] + mat[k][j]:
                mat[i][j] = mat[j][i] = mat[i][k] + mat[k][j]
kevin = [sum(row) for row in mat]
min_num = kevin[0]
min_idx = 0
for idx, num in enumerate(kevin):
    if num < min_num:
        min_num = num
        min_idx = idx
print(min_idx + 1)