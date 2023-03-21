from sys import stdin
from itertools import combinations
input = stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    for cand in combinations(arr, i):
        if sum(cand) == s:
            ans += 1
print(ans)