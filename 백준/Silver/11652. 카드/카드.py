from sys import stdin
from collections import Counter
stdin.readline()
c = Counter(map(int, stdin.read().splitlines()))
print(sorted(c.most_common(), key=lambda x: (-x[1], x[0]))[0][0])