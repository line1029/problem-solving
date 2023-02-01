from sys import stdin, stdout
from collections import Counter
a = Counter(range(-4000, 4001))
n = int(stdin.readline())
b = Counter(map(int, stdin.read().split()))
d = a.copy()
a += b
a -= d
keys = list(a.keys())
arr = list(a.elements())
avg = round(sum(arr)/n)
print(avg)
med = arr[n//2]
print(med)
mc = a.most_common()
if len(mc) >= 2 and mc[0][1] == mc[1][1]:
    mf = mc[1][0]
else:
    mf = mc[0][0]
print(mf)
r = keys[-1] - keys[0]
print(r)

    
