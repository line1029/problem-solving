import sys

n = 123456
s = [False, True] * (n + 1)
s[1] = False
s[2] = True
rootn = int((2*n)**(0.5)) + 1
for i in range(3, rootn + 1):
    if s[i]:
        s[i*i::2*i] = [False]*len(s[i*i::2*i])
ss = [i for i in range(2*n+1) if s[i]]
def bs(prime, n):
    l,r = 0, len(prime)-1
    while l<=r:
        m=(l+r)//2

        if prime[m] > n:
            r = m-1
        else:
            l = m+1
    return l

k = int(sys.stdin.readline())
while k:
    print(bs(ss, 2*k) - bs(ss, k))
    k = int(sys.stdin.readline())