from sys import stdin, stdout

def main():
    stdin.readline()
    dp = [[0]*31 for _ in range(31)]
    for i in range(31):
        dp[i][0] = dp[i][i] = 1
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    ans = []
    for n, m in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
        ans.append(dp[m][n])
    stdout.write("\n".join(map(str, ans)))

main()