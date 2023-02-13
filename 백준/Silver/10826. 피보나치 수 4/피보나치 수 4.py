n = int(input())

def matmul22(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k]*b[k][j]
    return c

ans = [[1, 0], [0, 1]]
po = [[1, 1], [1, 0]]

while n:
    if n&1:
        ans = matmul22(ans, po)
    po = matmul22(po, po)
    n >>= 1

print(ans[1][0])