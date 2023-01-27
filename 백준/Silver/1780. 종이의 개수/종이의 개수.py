from sys import stdin
from collections import Counter
n = int(stdin.readline())
mat = []
for _ in range(n):
    mat.append(list(map(int, stdin.readline().split())))
ans = [0, 0, 0]
def rec(n, mat):
    if n == 1:
        ans[mat[0][0]] += 1
        return
    standard = mat[0][0]
    for i in range(n):
        for j in range(n):
            if mat[i][j] != standard:
                for k in range(3):
                    for l in range(3):
                        rec(n//3, [row[l*n//3:(l+1)*n//3] for row in mat[k*n//3:(k+1)*n//3]])
                return
    ans[standard] += 1
    return
rec(n, mat)
ans = ans[-1:] + ans[:-1]
print("\n".join(map(str, ans)))