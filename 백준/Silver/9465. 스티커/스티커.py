from sys import stdin, stdout, setrecursionlimit
from itertools import islice
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr1 = list(map(int, stdin.readline().split()))
    arr2 = list(map(int, stdin.readline().split()))
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0], dp2[0] = arr1[0], arr2[0]
    if n > 1:
        dp1[1], dp2[1] = arr2[0] + arr1[1], arr1[0] + arr2[1]
    for i in range(2, n):
        dp1[i] = max(dp2[i-1], dp2[i-2]) + arr1[i]
        dp2[i] = max(dp1[i-1], dp1[i-2]) + arr2[i]
    print(max(dp1[-1], dp2[-1]))