from sys import stdin, stdout
from itertools import islice
n = int(stdin.readline())
a = stdin.readline().split()
b = stdin.readline().split()
m = int(stdin.readline())
c = stdin.readline().split()
ans = [b[i] for i in range(n-1, -1, -1) if a[i] == "0"]
ans += c[:m - len(ans)]
stdout.write(" ".join(islice(ans, m)))