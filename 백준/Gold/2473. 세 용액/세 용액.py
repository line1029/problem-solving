from sys import stdin
from bisect import bisect_left
stdin.readline()
plus = []
minus = []
for i in map(int, stdin.readline().split()):
    if i >= 0:
        plus.append(i)
    else:
        minus.append(i)
plus.sort()
minus.sort()
if len(plus) >= 3 and plus[2] == 0:
    print(0, 0, 0)
    exit()
elif not minus:
    print(*plus[:3])
    exit()
elif not plus:
    print(*minus[-3:])
    exit()


n = len(plus)
m = len(minus)
val = 3_000_000_000
ans = [0, 0, 0]
if n >= 3 and  sum(plus[:3]) < val:
    val = sum(plus[:3])
    ans = plus[:3]
if m >= 3 and - sum(minus[-3:]) < val:
    val = - sum(minus[-3:])
    ans = minus[-3:]
for i in range(n - 1):
    for j in range(i + 1, n):
        k = bisect_left(minus, - plus[i] - plus[j])
        if k < m and abs(plus[i] + plus[j] + minus[k]) < val:
            val = abs(plus[i] + plus[j] + minus[k])
            ans = [minus[k], plus[i], plus[j]]
            if not val:
                print(*ans)
                exit()
        if abs(plus[i] + plus[j] + minus[k - 1]) < val:
            val = abs(plus[i] + plus[j] + minus[k - 1])
            ans = [minus[k - 1], plus[i], plus[j]]
            if not val:
                print(*ans)
                exit()
for i in range(m - 1):
    for j in range(i + 1, m):
        k = bisect_left(plus, - minus[i] - minus[j])
        if k < n and abs(plus[k] + minus[i] + minus[j])  < val:
            val = abs(plus[k] + minus[i] + minus[j])
            ans = [minus[i], minus[j], plus[k]]
            if not val:
                print(*ans)
                exit()
        if abs(plus[k - 1] + minus[i] + minus[j]) < val:
            val = abs(plus[k - 1] + minus[i] + minus[j])
            ans = [minus[i], minus[j], plus[k - 1]]
            if not val:
                print(*ans)
                exit()
print(*ans)