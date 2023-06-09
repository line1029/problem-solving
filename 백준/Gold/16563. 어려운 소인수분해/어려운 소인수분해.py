import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
nums = list(map(int, input().split()))
m = max(nums)
linear_sieve = [0]*(m + 1)
primes = [2]
linear_sieve[2::2] = [2]*len(linear_sieve[2::2])
for i in range(3, m + 1, 2):
    if not linear_sieve[i]:
        primes.append(i)
        linear_sieve[i] = i
    for j in primes:
        if j * i > m:
            break
        linear_sieve[j * i] = j
        if i % j == 0:
            break
ans = __pypy__.builders.StringBuilder()
for num in nums:
    while num != 1:
        ans.append(f"{linear_sieve[num]} ")
        num //= linear_sieve[num]
    ans.append("\n")
os.write(1, ans.build().encode())