def matmul22(A, B, mod):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= mod
    return C
mod = 1000000
period = 1500000
n = int(input())
n %= period

def find_fibo_num(num, mod):
    if not num:
        return 0
    q = [[1, 1], [1, 0]]
    ans = [[1, 0], [0, 1]]
    while num:
        r = num & 1
        if r:
            ans = matmul22(ans, q, mod)
        num >>= 1
        q = matmul22(q, q, mod)
    return ans[1][0]


print(find_fibo_num(n, mod))