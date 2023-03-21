from sys import stdin, stdout
from itertools import product
input = stdin.readline
n, m = map(int, input().split())
stdout.write("\n".join(map(" ".join, product(map(str, range(1, n + 1)), repeat=m))))