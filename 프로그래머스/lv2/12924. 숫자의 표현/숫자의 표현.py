def solution(n):
    # k must divide n
    # k*(k+1)//2 <= n
    # k**2 + k - 2*n <= 0
    # k = (-1 +- sqrt(1 + 8*n))//2
    from math import sqrt
    ans = 0
    for i in range(1, int((-1 + sqrt(1 + 8*n))//2) + 1):
        s = n - i*(i+1)//2
        if s >= 0 and s%i == 0:
            ans += 1
    return ans