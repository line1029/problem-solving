from sys import stdin, stdout
from itertools import islice
n, m = map(int, stdin.readline().split())
arr = stdin.read().splitlines()
passwords = dict(map(lambda x: x.split(), islice(arr, n)))
ans = [passwords[i] for i in islice(arr, n, None)]
stdout.write("\n".join(ans))