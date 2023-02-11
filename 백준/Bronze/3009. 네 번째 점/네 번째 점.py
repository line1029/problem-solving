from sys import stdin
from collections import defaultdict
x_dict, y_dict = defaultdict(int), defaultdict(int)
for x, y in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    x_dict[x] += 1
    y_dict[y] += 1
ans = [0, 0]
for x in x_dict:
    if x_dict[x] == 1:
        ans[0] = x
for y in y_dict:
    if y_dict[y] == 1:
        ans[1] = y
print(" ".join(map(str, ans)))