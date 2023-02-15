from sys import stdin
n = int(stdin.readline())
orders = list(map(int, stdin.readline().split()))
ans = []
for i in range(1, n + 1):
    if orders[i - 1]:
        ans.insert(-orders[i - 1], i)
    else:
        ans.append(i)
print(" ".join(map(str, ans)))