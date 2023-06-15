from sys import stdin
from itertools import permutations
n, m = map(int, stdin.readline().split())
print("\n".join(" ".join(map(str, p)) for p in permutations(sorted(map(int, stdin.readline().split())), m)))