from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    p, m = map(int, input().split())
    ans = 0
    arr = [0]*(m + 1)
    for __ in range(p):
        arr[int(input())] += 1
    for i in arr:
        if i > 1:
            ans += i - 1
    print(ans)