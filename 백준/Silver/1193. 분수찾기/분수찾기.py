import sys
from math import sqrt
x = int(sys.stdin.readline())
# ak = k
# sk = k(k+1)/2
# x = k(k+1)/2 -> k^2 + k - 2x = 0
k = int((-1 + sqrt(1 + 8*x))/2)
while k*(k+1)//2 < x:
    k += 1
step1 = k*(k+1)//2 - x + 1
step2 = k - step1 + 1
s = f"{step1}/{step2}" if k%2 else f"{step2}/{step1}"
print(s)