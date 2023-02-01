import sys

n = 10000
s = [False, True] * (n//2 + 1)
s[1] = False
s[2] = True
rootn = int(n**(0.5)) + 1
for i in range(3, rootn + 1):
    if s[i]:
        s[i*i::2*i] = [False]*len(s[i*i::2*i])
ss = [i for i in range(n+1) if s[i]]
ss2 = set(ss)
def bs(prime, n):
    l,r = 0, len(prime)-1
    while l<=r:
        m=(l+r)//2

        if prime[m] > n:
            r = m-1
        else:
            l = m+1
    return r

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    p_idx = bs(ss, n//2)
    while n - ss[p_idx] not in ss2:
        p_idx -= 1
    print(ss[p_idx], n - ss[p_idx])
    