from sys import stdin
n = int(stdin.readline())
arr = stdin.readline().split()
stack = 0
ans = [0 for _ in range(n + 1)]
for i in range(n):
    num = arr[i]
    if num == "1":
        stack -= 1
    else:
        stack += 1
    ans[i] += stack
print(max(ans) - min(ans))
        