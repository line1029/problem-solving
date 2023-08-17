import io, os, __pypy__
from math import sqrt
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = int(input())
ans = __pypy__.builders.StringBuilder()
for i in range(t):
    # k*x*(x + 1)//2 <= n < k*(x + 1)*(x + 2)//2
    # kx^2 + kx - 2n <= 0
    # x = (-k +- sqrt(k^2 + 8kn))/2k
    n, k = map(int, input().split())
    n -= 1
    x = int((-k + sqrt(k*k + 8*k*n))/(2*k))
    if x&1:
        ans.append(f"{k*(x + 1)*(x + 1)//2 - n} L\n")
    else:
        ans.append(f"{n - k*x*(x + 2)//2} R\n")
os.write(1, ans.build().encode())