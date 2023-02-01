from sys import stdin, stdout
from collections import Counter
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
c = Counter(arr)
order = sorted(list(c.keys()))
d = dict([[order[i], i] for i in range(len(order))])
for num in arr:
    stdout.write(f"{d[num]} ")