import collections
n = list(map(int, input().split()))
s = collections.Counter(n)
if max(s.values()) == 3:
    print(10000 + 1000 * n[0])
elif max(s.values()) == 1:
    print(max(n) * 100)
else:
    if s[n[0]] == 2:
        print(n[0] * 100 + 1000)
    else:
        print(n[1] * 100 + 1000)