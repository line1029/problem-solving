from sys import stdin, stdout
from collections import Counter
n = int(stdin.readline())
got = Counter(map(int, stdin.readline().split()))
m = int(stdin.readline())
ans = map(lambda x: str(got[int(x)]), stdin.readline().split())
stdout.write(" ".join(ans))