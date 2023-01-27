from sys import stdin
n = int(stdin.readline())
mat = list(map(lambda x: list(map(int, x.split())), stdin.readlines()))
ans = [0, 0]
def dfs(n, mat):
    if n == 1:
        ans[mat[0][0]] += 1
        return
    standard = mat[0][0]
    for i in range(n):
        for j in range(n):
            if standard != mat[i][j]:
                for k in range(2):
                    for l in range(2):
                        dfs(n//2, [row[l*n//2:(l+1)*n//2] for row in mat[k*n//2:(k+1)*n//2]])
                return
    ans[standard] += 1
dfs(n, mat)
print(ans[0])
print(ans[1])