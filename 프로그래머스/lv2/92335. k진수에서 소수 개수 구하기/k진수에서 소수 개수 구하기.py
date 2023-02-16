def solution(n, k):
    if n == 1:
        return 0
    n_base_k = []
    while n:
        n_base_k.append(n % k)
        n //= k
    candidates = "".join(map(str, reversed(n_base_k))).split("0")
    candidates = [int(i) for i in candidates if i]
    if not candidates:
        return 0

    def miller_rabin(n, a):
        if n % a == 0:
            return True

        k = n - 1
        while not k & 1:
            tmp = pow(a, k, n)
            if tmp == n - 1:
                return True
            elif tmp != 1:
                return False
            k >>= 1
        return tmp == 1 or tmp == n - 1


    def is_prime(n):
        if n <= 1:
            return False
        if any([n == 2, n == 3, n == 5, n == 7]):
            return True
        if any([n % 2 == 0, n % 3 == 0, n % 5 == 0, n % 7 == 0]):
            return False
        base = [2, 7, 61]
        for a in base:
            if not miller_rabin(n, a):
                return False
        return True
    
    return sum(is_prime(i) for i in candidates)