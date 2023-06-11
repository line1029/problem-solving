from sys import stdin
a, b = stdin.readline().strip(), stdin.readline().strip()
dp = [0]*(len(a) + 1)
for c1 in b:
    tmp = 0
    for i, c2 in enumerate(a, 1):
        tmp2 = dp[i]
        if c1 == c2:
            dp[i] = tmp + 1
        else:
            dp[i] = max(dp[i], dp[i - 1])
        tmp = tmp2
print(dp[-1])