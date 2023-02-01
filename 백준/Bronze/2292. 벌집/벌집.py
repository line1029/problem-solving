n = int(input())
from math import sqrt
k = int((3 + sqrt(12*n-3))/6) + 1
if 3*k**2 - 9*k + 7 < n:
    print(k)
else:
    print(k-1)