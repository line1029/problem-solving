def solution(n, k):
    if n == 1:
        return 0
    n_base_k = []
    while n:
        n_base_k.append(n%k)
        n //= k
    candidates = "".join(map(str, reversed(n_base_k))).split("0")
    candidates = [int(i) for i in candidates if i]
    if not candidates:
        return 0
    
    def power(a, b, mod):
        res = 1
        while b:
            if b&1:
                res = (res * a) % mod
            b >>= 1
            a = (a * a) % mod
        return res


    def miller_rabin(n, a):
        if n % a == 0:
            return True

        k = n - 1
        tmp = power(a, k, n)
        if tmp != 1:
            return False
        while not k&1:
            k >>= 1
            if tmp == n - 1:
                return True
            elif tmp != 1:
                return False
        return tmp == 1 or tmp == n - 1


    def is_prime(n):
        if n <= 1:
            return False
        if any([n == 2, n == 3, n == 5, n == 7]):
            return True
        if any([n % 2 == 0, n % 3 == 0, n % 5 == 0, n % 7 == 0]):
            return False
        if n < 1 << 32:
            base = [2, 7, 61]
        else:
            base = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
        for a in base:
            if not miller_rabin(n, a):
                return False
        return True
    
    return sum(is_prime(i) for i in candidates)