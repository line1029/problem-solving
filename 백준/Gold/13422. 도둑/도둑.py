# Thief - two pointer sliding window
from sys import stdin
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
print(*ans, sep="\n")