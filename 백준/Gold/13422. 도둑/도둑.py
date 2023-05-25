# Thief - two pointer sliding window
from sys import stdin, stdout
from itertools import islice
ans = []
for _ in range(int(stdin.readline())):
    n, m, k = map(int, stdin.readline().split())
    houses = list(map(int, stdin.readline().split()))
    houses += houses
    money = sum(islice(houses, m))
    cnt = int(money < k)
    if n != m:
        for j in range(m, n+m-1):
            money += houses[j] - houses[j - m]
            cnt += money < k
    ans.append(cnt)
stdout.write("\n".join(map(str,ans)))