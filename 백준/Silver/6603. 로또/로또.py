from sys import stdin, stdout
from itertools import combinations
tcs = stdin.read().splitlines()
tcs.pop()
for tc in tcs:
    _, *s = tc.split()
    stdout.write("\n".join((" ".join(i) for i in combinations(s, 6))))
    stdout.write("\n\n")