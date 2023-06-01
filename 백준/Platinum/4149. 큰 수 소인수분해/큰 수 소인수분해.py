from sys import stdin
from collections import defaultdict
from math import gcd, sqrt
from random import randint


def miller_rabin(n, a):
    if n % a == 0:
        return False
    
    k = n - 1
    while True:
        tmp = pow(a, k, n)
        if tmp == n - 1:
            return True
        if k&1:
            return tmp == 1 or tmp == n - 1
        k >>= 1


def is_prime(n):
    if n <= 1:
        return False
    if n in [2, 3, 5, 7, 11, 13]:
        return True
    if n % 2 == 0:
        return False
    if n < 10000:
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n%i==0:
                return False
        return True
    if n < (1 << 32):
        base = [2, 7, 61]
    else:
        base = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    for a in base:
        if not miller_rabin(n, a):
            return False
    return True


def pollard_rho(n, factor):
    for prime in factor:
        while n % prime == 0:
            n //= prime
            factor[prime] += 1
    if is_prime(n):
        factor[n] += 1
        return
    if n <= 1:
        return
    if n % 2 == 0:
        while n % 2 == 0:
            n >>= 1
            factor[2] += 1
        pollard_rho(n, factor)
        return
    x = y = randint(2, n - 1)
    c = randint(1, n - 1)
    d = 1
    while d == 1:
        x = ((x*x)%n + c)%n
        y = ((y*y)%n + c)%n
        y = ((y*y)%n + c)%n
        d = gcd(abs(x - y), n)
        if d == n:
            pollard_rho(n, factor)
            return
    if is_prime(d):
        while n % d == 0:
            n //= d
            factor[d] += 1
        pollard_rho(n, factor)
        return
    else:
        pollard_rho(d, factor)
        pollard_rho(n//d, factor)
        return



n = int(stdin.readline())
factor = defaultdict(int)
pollard_rho(n, factor)
for prime, val in sorted(factor.items()):
    print("\n".join(map(str, [prime]*val)))