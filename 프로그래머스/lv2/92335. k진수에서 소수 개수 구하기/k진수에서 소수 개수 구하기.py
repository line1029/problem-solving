def solution(n, k):
    if n == 1:
        return 0
    n_base_k = []
    while n:
        n_base_k.append(n%k)
        n //= k
    n_base_k = "".join(map(str, n_base_k[::-1])).split("0")
    n_base_k = [int(i) for i in n_base_k if i]
    if not n_base_k:
        return 0
    n_base_k.sort()
    # n_base_k2 = []
    # while n_base_k and n_base_k[-1] > 10000:
    #     n_base_k2.append(n_base_k.pop())
    def check_prime_byarr(n_base_k):
        max_candidate = n_base_k[-1]
        if max_candidate == 1:
            return 0
        prime_arr = [False, True]*(max_candidate//2 + 1)
        prime_arr[1] = False
        prime_arr[2] = True
        for i in range(3, int(max_candidate**(0.5)) + 1, 2):
            prime_arr[i*i::2*i] = [False]*len(prime_arr[i*i::2*i])
        ans = [prime_arr[i] for i in n_base_k]
        if ans:
            return sum(ans)
        return 0
    
    def check_prime_bydiv(num):
        if num == 1:
            return 0
        if num == 2:
            return 1
        if num%2 == 0:
            return 0
        for i in range(3, int(num**(0.5)) + 1, 2):
            if num%i == 0:
                return 0
        return 1
    
    return sum(check_prime_bydiv(i) for i in n_base_k)
