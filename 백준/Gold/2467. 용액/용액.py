from sys import stdin
n = int(stdin.readline())
plus = []
minus = []
for i in map(int, stdin.readline().split()):
    if i >= 0:
        plus.append(i)
    else:
        minus.append(i)
plus.sort(reverse=True)
minus.sort()
if len(plus) >= 2 and plus[1] == 0:
    print(0, 0)
    exit()
elif not minus:
    print(plus[-1], plus[-2])
    exit()
elif not plus:
    print(minus[-2], minus[-1])
    exit()
i = j = 0
k = len(plus)
l = len(minus)
m = 2_000_000_000
ans = [0, 0]
if k >= 2 and plus[-1] + plus[-2] < m:
    m = plus[-1] + plus[-2]
    ans[0], ans[1] = plus[-2], plus[-1]
if l >= 2 and abs(minus[-1] + minus[-2]) < m:
    m = abs(minus[-1] + minus[-2])
    ans[0], ans[1] = minus[-1], minus[-2]
while i < k and j < l:
    if abs(plus[i] + minus[j]) < m:
        m = abs(plus[i] + minus[j])
        ans[0], ans[1] = plus[i], minus[j]
    if abs(plus[i]) == abs(minus[j]):
        print(minus[j], plus[i])
        exit()
    elif abs(plus[i]) < abs(minus[j]) and j < l - 1:
        j += 1
    elif abs(plus[i]) > abs(minus[j]) and i < k - 1:
        i += 1
    else:
        break
print(ans[1], ans[0])