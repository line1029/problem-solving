from sys import stdin, stdout
from math import log
# upper nodes = (k**h - 1) // (k - 1) -> log(x * (k - 1), k) = h + 0.xx..
n, k, q = map(int, stdin.readline().split())
ans = []
for x, y in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    if x > y:
        x, y = y, x
    if k == 1:
        ans.append(y - x)
    else:
        hx, hy = int(log(x * (k - 1), k)), int(log(y * (k - 1), k))
        dist = 0
        while hy > hx:
            dist += 1
            hy -= 1
            y = (y + k - 2)//k
        while x != y:
            dist += 2
            x = (x + k - 2)//k
            y = (y + k - 2)//k
        ans.append(dist)
stdout.write("\n".join(map(str, ans)))