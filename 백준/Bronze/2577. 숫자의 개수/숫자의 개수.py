import sys
from collections import Counter
n = 1
for _ in range(3):
    n *= int(sys.stdin.readline())
a = Counter(str(n))
for i in range(10):
    print(a[str(i)])
