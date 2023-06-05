from sys import stdin
from itertools import combinations
ans = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n > 32:
        stdin.readline()
        ans.append(0)
        continue
    students = stdin.readline().split()
    tmp = 8
    for s in combinations(students, 3):
        tmp = min(tmp, sum(((i != j) + (j != k) + (k != i)) for i, j, k in zip(*s)))
        if tmp == 2:
            break
    ans.append(tmp)
print("\n".join(map(str, ans)))