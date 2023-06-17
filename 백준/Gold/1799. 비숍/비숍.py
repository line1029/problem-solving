from sys import stdin
n = int(stdin.readline())
n2 = 2*n
grid = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
minor_diagonal = [0]*(n2 - 1)
ans = [0, 0]
def dfs(depth, row, parity):
    ans[parity] = max(ans[parity], depth)
    for i in range(row, n2 - 1, 2):
        if i <= n - 1:
            r = range(n - 1 - i, n + i, 2)
        else:
            r = range(i - n + 1, n2 - i - 2 + n, 2)
        for j in r:
            if grid[(i+j-n+1)//2][(i-j+n-1)//2] and not minor_diagonal[j]:
                minor_diagonal[j] = 1
                dfs(depth + 1, i + 2, parity)
                minor_diagonal[j] = 0
        
dfs(0, 0, 0)
dfs(0, 1, 1)
print(sum(ans))