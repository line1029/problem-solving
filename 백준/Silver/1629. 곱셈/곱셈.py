m, n, r = map(int, input().split())
m %= r
if n == 1:
    print(m)
else:
    print(pow(m, n, r))