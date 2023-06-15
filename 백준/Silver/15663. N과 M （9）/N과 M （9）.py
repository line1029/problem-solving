from sys import stdin
from itertools import permutations
n, m = map(int, stdin.readline().split())
arr = sorted(map(int, stdin.readline().split()))
print("\n".join(" ".join(map(str, p)) for p in sorted(set(permutations(arr, m)))))