from sys import stdin
M = 1_000_000_007
m = int(stdin.readline())
print(sum(map(lambda y: pow(next(y), M - 2, M) * next(y) % M, map(lambda x: map(int, x.split()), stdin.read().splitlines())))%M)