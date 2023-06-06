from sys import stdin
n = int(stdin.readline())
major_diagonal = [0]*(2*n - 1)
minor_diagonal = [0]*(2*n - 1)
col = [0] * n
ans = 0
def dfs(i):
    if i == n:
        global ans
        ans += 1
        return
    for j in range(n):
        if not col[j] and not major_diagonal[j - i] and not minor_diagonal[j + i]:
            col[j] = 1
            major_diagonal[j - i] = 1
            minor_diagonal[j + i] = 1
            dfs(i + 1)
            col[j] = 0
            major_diagonal[j - i] = 0
            minor_diagonal[j + i] = 0
dfs(0)
print(ans)