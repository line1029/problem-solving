from sys import stdin
n, m = map(int, stdin.readline().split())
sn, sm = set(map(int, stdin.readline().split())), set(map(int, stdin.readline().split()))
print(n + m - 2*len(sn.intersection(sm)))