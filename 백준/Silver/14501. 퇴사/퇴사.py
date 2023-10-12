n = int(input())
t, p = [], []
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)
dp = [0] * n
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        continue
    dp[i] = max(max(dp[i + 1:], default=0), p[i] + max(dp[i + t[i]:], default=0))
print(max(dp))
