m , n = map(int, input().split())
s = [False, True]*(n//2 + 1)
s[1] = False
s[2] = True
rootn = int(n**(0.5)) + 1
for i in range(3, rootn + 1):
    s[i*i::2*i] = [False] * len(s[i*i::2*i])

for num in [i for i in range(m, n+1) if s[i]]:
    print(num)