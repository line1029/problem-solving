from sys import stdin
from collections import defaultdict

for _ in range(int(stdin.readline())):
    clothes = defaultdict(list)
    n = int(stdin.readline())
    for i in range(n):
        c, kind = stdin.readline().split()
        clothes[kind].append(c)
    ans = 1
    for v in clothes.values():
        ans *= len(v) + 1
    print(ans - 1)