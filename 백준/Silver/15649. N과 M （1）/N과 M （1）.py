from sys import stdin, stdout
from itertools import permutations
n, m = map(int, input().split())
stdout.write("\n".join(" ".join(i) for i in permutations(map(str, range(1, n + 1)), m)))