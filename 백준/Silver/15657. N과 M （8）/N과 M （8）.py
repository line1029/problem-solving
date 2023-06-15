from sys import stdin
from itertools import combinations_with_replacement as c
n, m = map(int, stdin.readline().split())
print("\n".join(" ".join(map(str, p)) for p in c(sorted(set(map(int, stdin.readline().split()))), m)))