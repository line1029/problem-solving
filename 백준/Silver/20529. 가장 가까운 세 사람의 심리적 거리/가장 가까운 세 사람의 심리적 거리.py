from sys import stdin
from itertools import combinations
ans = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n > 32:
        stdin.readline()
        ans.append(0)
        continue
    tmp = 12
    for students in combinations(stdin.readline().split(), 3):
        tmp = min(tmp, sum(((i != j) + (j != k) + (k != i)) for i, j, k in zip(*students)))
    ans.append(tmp)
print("\n".join(map(str, ans)))