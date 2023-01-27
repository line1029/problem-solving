from sys import stdin
from collections import Counter
n = int(stdin.readline())
mat = []
for _ in range(n):
    mat.append(list(map(int, stdin.readline().split())))
def rec(n, mat):
    c = Counter()
    for row in mat:
        c += Counter(row)
    ans = [0, 0, 0]
    if len(c) == 1:
        ans[0] += -1 in c
        ans[1] += 0 in c
        ans[2] += 1 in c
        return ans
    else:
        n_nex = n//3
        for i in range(9):
            r, c = i//3, i%3
            mat_nex = [mat[i][c*n_nex:(c+1)*n_nex] for i in range(r*n_nex, (r+1)*n_nex)]
            ans_i = rec(n_nex, mat_nex)
            ans[0] += ans_i[0]
            ans[1] += ans_i[1]
            ans[2] += ans_i[2]
        return ans
            
print("\n".join(map(str, rec(n, mat))))