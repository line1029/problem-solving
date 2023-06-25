from sys import stdin
n, m = map(int, stdin.readline().split())
memories = list(map(int, stdin.readline().split()))
costs = list(map(int, stdin.readline().split()))
idxs = list(range(n))
idxs.sort(key=lambda x: memories[x])
memories = [memories[i] for i in idxs]
costs = [costs[i] for i in idxs]
dp = [10001]*(sum(memories) + 1)
k = len(dp) - 1
dp[0] = 0
cur_max = 0
for i in range(n):
    cur_max = min(cur_max + memories[i], k)
    for j in range(cur_max, memories[i] - 1, -1):
        dp[j] = min(dp[j], dp[j - memories[i]] + costs[i])
print(min(dp[m:]))