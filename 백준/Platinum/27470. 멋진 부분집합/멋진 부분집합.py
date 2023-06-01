from sys import stdin, setrecursionlimit
from collections import Counter
from math import gcd
from random import randint
setrecursionlimit(1000000)

def power(a, b, mod):
    res = 1
    while b:
        if b&1:
            res = (res * a) % mod
        b >>= 1
        a = (a * a) % mod
    return res


def miller_rabin(n, a):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n == a:
        return True
    
    k = n - 1
    while True:
        tmp = power(a, k, n)
        if tmp == n - 1:
            return True
        if k&1:
            return tmp == 1 or tmp == n - 1
        k >>= 1


def is_prime(n):
    base = [2, 7, 61]
    for a in base:
        if not miller_rabin(n, a):
            return False
    return True


def pollard_rho(n):
    if is_prime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    x = y = randint(2, n - 1)
    c = randint(1, n - 1)
    d = 1
    while d == 1:
        x = ((x*x)%n + c)%n
        y = ((y*y)%n + c)%n
        y = ((y*y)%n + c)%n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)
    if is_prime(d):
        return d
    else:
        return pollard_rho(d)

def factors(n):
    res = set()
    while n > 1:
        divisor = pollard_rho(n)
        res.add(divisor)
        while n % divisor == 0:
            n //= divisor
    return res

N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
c = Counter()
for i in nums:
    c.update(factors(i))
prime, cnt = c.most_common()[0]
wanted_length = N//2 + N%2
if cnt < wanted_length:
    print("NO")
    exit()
print("YES")
ans = []
for i in range(N):
    if nums[i]%prime == 0:
        ans.append(nums[i])
    if len(ans) == wanted_length:
        break
print(" ".join(map(str, ans)))