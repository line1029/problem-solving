n = int(input())
if n == 1:
    print(0)
    exit()
sieve = [False, True]*((n>>1) + 1)
if not n & 1:
    sieve.pop()
sieve[1] = False
sieve[2] = True
sieve[4::2] = [False]*((n>>1) - 1)
sieve[9::3] = [False]*(n//3 - 2)
for i in range(6, int(n**.5) + 1, 6):
    if sieve[i - 1]:
        sieve[(i - 1)*(i - 1)::i - 1] = [False]*(n//(i - 1) - i + 2)
    if sieve[i + 1]:
        sieve[(i + 1)*(i + 1)::i + 1] = [False]*(n//(i + 1) - i)
primes = [i for i in range(2, n + 1) if sieve[i]]
k = len(primes)
ans = 0
i = 0
j = 1
s = 2
while i < k:
    while j < k and s < n:
        s += primes[j]
        j += 1
    if s == n:
        ans += 1
        if j >= k:
            break
        s += primes[j]
        j += 1
    else:
        while s > n:
            s -= primes[i]
            i += 1
        if s == n:
            ans += 1
            if j >= k:
                break
            s += primes[j]
            j += 1
        else:
            if j >= k:
                break
print(ans)
