import sys
p = list(map(int, sys.stdin.readline().split()))
a = [1, 1, 2, 2, 2, 8]
ans = [a[i] - p[i] for i in range(len(p))]
for i in ans:
    print(i, end=" ")