from sys import stdin
n = int(stdin.readline())
arr = sorted(map(int, stdin.read().splitlines()), reverse=True)
ans = 0
for i in range(n):
    if arr[i] <= i:
        break
    ans += arr[i] - i
print(ans)