from sys import stdin
from collections import Counter
def prime_sieve(n):
    s = [False, True]*int((n//2 + 1)**.5 + 1)
    s[1] = False
    s[2] = True
    for i in range(3, int(n**.5) + 1):
        if s[i]:
            s[i*i::i*2] = [False]*(len(s[i*i::i*2]))
    return [i for i in range(len(s)) if s[i]]
N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
n = max(nums)
fs = prime_sieve(n)
def factorization(n):
    res = set()
    for i in fs:
        while n%i == 0:
            res.add(i)
            n //= i
    if n != 1:
        res.add(n)
    return res
c = Counter()
for i in nums:
    c.update(factorization(i))
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