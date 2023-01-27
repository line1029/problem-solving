def matrix_multiplication(a, b, mod):
    return [[(a[0][0] * b[0][0] % mod + a[0][1] * b[1][0] % mod) % mod,
             (a[0][0] * b[0][1] % mod + a[0][1] * b[1][1] % mod) % mod],
            [(a[1][0] * b[0][0] % mod + a[1][1] * b[1][0] % mod) % mod,
             (a[1][0] * b[0][1] % mod + a[1][1] * b[1][1] % mod) % mod]]


def find_fibonacci_num(n, mod):
    if not n:
        return 0
    ans = [[1, 0], [0, 1]]
    q = [[1, 1], [1, 0]]
    while n > 0:
        if n % 2:
            ans = matrix_multiplication(q, ans, mod)
        q = matrix_multiplication(q, q, mod)
        n //= 2
    return ans[1][0]


n = int(input())
print(find_fibonacci_num(n, 10**9 + 7))