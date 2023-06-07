from sys import stdin, stdout
def matmul(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= 1000
    return C


def matpow(A, B):
    n = len(A)
    ans = [[0]*n for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1
    while B:
        if B & 1:
            ans = matmul(A, ans)
        B >>= 1
        A = matmul(A, A)
    return ans


N, B = map(int, stdin.readline().split())
A = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
stdout.write("\n".join(" ".join(map(str, i)) for i in matpow(A, B)))