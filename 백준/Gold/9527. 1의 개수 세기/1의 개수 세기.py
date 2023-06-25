from sys import stdin
def f(x):
    ones = bin(x).count("1")
    ans = k = 0
    if x & 1:
        ones -= 1
        ans += ones + 1
        x >>= 1
        k += 1
    while x:
        if x & 1:
            ones -= 1
            ans += ones*(1 << k) + k*(1 << k - 1) + 1
        x >>= 1
        k += 1
    return ans

a, b = map(int, stdin.readline().split())
print(f(b) - f(a - 1))