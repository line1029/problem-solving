import sys
t = int(sys.stdin.readline())
for _ in range(t):
    k, n = int(sys.stdin.readline()), int(sys.stdin.readline())
    mat = [[0]*(n+1) for _ in range(k+1)]
    mat[0] = list(range(n+1))
    for i in range(1, k+1):
        for j in range(1, n+1):
            mat[i][j] = mat[i][j-1] + mat[i-1][j]
    print(mat[-1][-1])