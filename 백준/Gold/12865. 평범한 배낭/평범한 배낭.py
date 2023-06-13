from sys import stdin
n, k = map(int, stdin.readline().split())
dp = [0]*(k + 1)
dp[0] = 1
cur_max = 0
cur_val = 0
for w, v in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    cur_max = min(cur_max + w, k)
    for i in range(cur_max, w - 1, -1):
        if dp[i - w]:
            dp[i] = max(dp[i], dp[i - w] + v)
            cur_val = max(cur_val, dp[i])
print(max(cur_val - 1, 0))