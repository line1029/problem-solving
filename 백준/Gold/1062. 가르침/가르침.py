from itertools import combinations
def convert(s):
    res = 0
    for char in s[4:-4]:
        x = ord(char)
        if x == 98:
            res |= 1
        elif 99 < x < 105:
            res |= (1 << x - 99)
        elif 105 < x < 110:
            res |= (1 << x - 100)
        elif 110 < x < 116:
            res |= (1 << x - 101)
        elif x > 116:
            res |= (1 << x - 102)
    return res
n, k = map(int, input().split())
k -= 5
if k < 0:
    print(0)
    exit()
alphas = 0
letters = []
ans = 0
for _ in range(n):
    x = convert(input())
    alphas |= x
    letters.append(x)
x = alphas
y = 0
a = []
while x:
    if x&1:
        a.append(y)
    x >>= 1
    y += 1
for pattern in combinations(a, min(len(a), k)):
    x = 0
    cnt = 0
    for i in pattern:
        x |= (1 << i)
    for i in letters:
        if not i&(~x):
            cnt += 1
    ans = max(ans, cnt)
        
print(ans)