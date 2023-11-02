from sys import stdin
n, k, m = map(int, stdin.readline().split())
stdin.readline()
for i in map(int, stdin.read().splitlines()):
    if 0 < k <= i:
        k = i - k + 1
    elif 0 > i and n + i + 1 <= k:
        k = 2*n - k + i + 1
print(k)
