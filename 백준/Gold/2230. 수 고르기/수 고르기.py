from sys import stdin
n, m = map(int, stdin.readline().split())
arr = sorted(map(int, stdin.read().splitlines()))
ans = arr[-1] - arr[0]
j = 1
for i in range(n - 1):
    while j < n and arr[j] - arr[i] < m:
        j += 1
    if j == n:
        break
    ans = min(ans, arr[j] - arr[i])
print(ans)