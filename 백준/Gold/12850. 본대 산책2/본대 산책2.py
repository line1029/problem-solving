from sys import stdin, stdout
def matmul(A, B, mod):
    row, col, inter = len(A), len(B[0]), len(A[0])
    C = [[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            for k in range(inter):
                C[i][j] += A[i][k]*B[k][j]
                C[i][j] %= mod
    return C

def main():
    d = int(stdin.readline())
    ans = [[0]*8 for _ in range(8)]
    for i in range(8):
        ans[i][i] = 1
    # 정, 전, 미, 신, 한, 진, 형, 학
    q = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0]
    ]
    mod = 1_000_000_007
    while d:
        if d & 1:
            ans = matmul(ans, q, mod)
        q = matmul(q, q, mod)
        d >>= 1
    print(ans[0][0])
main()