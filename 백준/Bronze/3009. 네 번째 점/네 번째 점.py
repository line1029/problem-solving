from sys import stdin
a, b = [], []
for x, y in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    if x not in a:
        a.append(x)
    else:
        a.remove(x)
    if y not in b:
        b.append(y)
    else:
        b.remove(y)
print(" ".join(map(str, a + b)))