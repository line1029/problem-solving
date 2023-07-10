import os, io
from sys import stdout
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def main():
    s = input().rstrip()
    n = len(s)
    dp = [[0]*26 for _ in range(n + 1)]
    for j, i in enumerate(map(lambda x: x - 97, s)):
        dp[j][i] += 1
    for i in range(26):
        for j in range(n - 1):
            dp[j + 1][i] += dp[j][i]

    q = int(input())
    ans = []
    for a, i, j in (input().split() for _ in range(q)):
        a, i, j = int.from_bytes(a, "little") - 97, int(i), int(j)
        ans.append(dp[j][a] - dp[i - 1][a])
    stdout.write("\n".join(map(str, ans)))
main()