# prime factor
# sqrtn or pollard rho
# sqrtn
from math import sqrt
from itertools import combinations
N = n = int(input())
factor = []
if not n&1:
    while not n&1:
        n >>= 1
    factor.append(2)
for i in range(3, int(sqrt(n)) + 1, 2):
    if i > n: break
    if not n%i:
        while not n%i:
            n //= i
        factor.append(i)
if n > 1:
    factor.append(n)
# inclusion-exclusion
ans = 0
for i in range(1, len(factor) + 1):
    for pat in combinations(factor, i):
        x = 1
        for j in pat:
            x *= j
        if i&1:
            ans += N//x
        else:
            ans -= N//x
print(N - ans)
