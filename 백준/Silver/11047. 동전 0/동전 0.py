from sys import stdin
n, k = map(int, stdin.readline().split())
coins = list(map(int, stdin.readlines()))[::-1]
ans = 0
for coin in coins:
    if not k:
        break
    cur = k // coin
    if cur:
        ans += cur
        k %= coin
print(ans)