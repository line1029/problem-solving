from sys import stdin
n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
start = 0
ans = 100000
x = 0
for end in range(n):
    x += arr[end]
    while start <= end and x >= s:
        ans = min(ans, end - start + 1)
        x -= arr[start]
        start += 1
if ans == 100000:
    print(0)
else:
    print(ans)
