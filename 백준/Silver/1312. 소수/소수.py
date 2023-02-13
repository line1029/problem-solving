a, b, n = map(int, input().split())
a %= b
decimal = []
remainder = dict()
i = 0
while a not in remainder:
    remainder[a] = ((a*10)%b, i)
    decimal.append((a*10)//b)
    a = (a*10)%b
    i += 1
start, period = remainder[a][1], i - remainder[a][1]
if n - 1 < start:
    print(decimal[n - 1])
else:
    print(decimal[(n - 1 - start)%period + start])