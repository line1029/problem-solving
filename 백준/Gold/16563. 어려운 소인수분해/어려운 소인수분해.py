import os, io, __pypy__
from math import sqrt
import struct
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
nums = list(map(int, input().split()))
m = max(nums)
linear_sieve = list(range(m + 1))
linear_sieve[4::2] = [2]*len(linear_sieve[4::2])
for i in range(3, int(sqrt(m)) + 1, 2):
    if linear_sieve[i] == i:
        for j in range(i*i, m + 1, 2*i):
            if linear_sieve[j] == j:
                linear_sieve[j] = i
ans = __pypy__.builders.StringBuilder()
for num in nums:
    while num != 1:
        ans.append(f"{linear_sieve[num]} ")
        num //= linear_sieve[num]
    ans.append("\n")
os.write(1, ans.build().encode())