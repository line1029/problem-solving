from sys import stdin
from math import gcd, lcm
def get_year(m, n, x, y):
    # let answer be k
    # k == x mod m
    # k == y mod n
    # so if (x - y) % gcd(m, n) != 0, then no answer
    g = gcd(m, n)
    if (x - y) % g != 0:
        print(-1)
        return
    # get k with extended euclid algorithm
    # let s * m + t * n = g
    # we want to get s, t
    def extended_euclid(a, b):
        x0, x1, y0, y1 = 1, 0, 0, 1
    
        while b != 0:
            n, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - n * x1
            y0, y1 = y1, y0 - n * y1
        
        return x0, y0
    s, t = extended_euclid(m, n)
    s *= (y - x)//g
    k = (s*m + x)%lcm(m, n)
    if not k:
        k = lcm(m, n)
    print(k)
    return
    


for _ in range(int(stdin.readline())):
    m, n, x, y = map(int, stdin.readline().split())
    get_year(m, n, x, y)