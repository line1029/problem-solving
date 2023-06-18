from sys import stdin, stdout
s1, s2 = stdin.readline().strip(), stdin.readline().strip()
n, m = len(s1), len(s2)
dp = [[(0, 0, 0) for j in range(n + 1)] for i in range(m + 1)]
maxlen = 0
maxidx = (0, 0)
for i, char1 in enumerate(s2, 1):
    for j, char2 in enumerate(s1, 1):
        dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i - 1][j])
        if char1 == char2:
            if dp[i][j][0] < dp[i - 1][j - 1][0] + 1:
                dp[i][j] = (dp[i - 1][j - 1][0] + 1, i, j)
                if dp[i][j][0] > maxlen:
                    maxlen = dp[i][j][0]
                    maxidx = (i, j)
print(maxlen)
i, j = maxidx
ans = []
while i or j:
    ans.append(s2[i - 1])
    i, j = dp[i - 1][j - 1][1:]
stdout.write("".join(reversed(ans)))
