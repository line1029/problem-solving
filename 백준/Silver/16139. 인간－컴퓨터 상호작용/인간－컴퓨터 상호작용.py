import os, io
from sys import stdout
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def main():
    s = input().rstrip()
    n = len(s)
    dp = [[0]*(n + 1) for _ in range(26)]
    for j, i in enumerate(map(lambda x: x - 97, s)):
        dp[i][j] += 1
    for i in range(26):
        for j in range(n - 1):
            dp[i][j + 1] += dp[i][j]

    q = int(input())
    ans = []
    for a, i, j in (input().split() for _ in range(q)):
        a, i, j = int.from_bytes(a, "little") - 97, int(i), int(j)
        ans.append(dp[a][j] - dp[a][i - 1])
    stdout.write("\n".join(map(str, ans)))
main()