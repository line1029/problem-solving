r = list()

t = int(input())

for i in range(t):
    d = input().split()
    h = int(d[0])
    w = int(d[1])
    n = int(d[2])
    if n % h == 0:
        r.append((h * 100) + (n // h))
    else:
        r.append(((n % h) * 100) + (n // h + 1))

for i in r:
    print(i)
