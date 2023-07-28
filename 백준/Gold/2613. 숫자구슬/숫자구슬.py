from sys import stdin
def main():
    n, m = map(int, stdin.readline().split())
    marbles = list(map(int, stdin.readline().split()))
    psum = [0]
    for mar in marbles:
        psum.append(psum[-1] + mar)
    dp = [[30001]*n for _ in range(m)]
    nums = [[0]*n for _ in range(m)]
    nums[0] = list(range(1, n + 1))
    dp[0] = psum[1:]
    for i in range(1, m):
        dp[i][i] = max(dp[i - 1][i - 1], marbles[i])
        nums[i][i] = 1
        for j in range(i + 1, n):
            for k in range(j - i + 1):
                p = max(dp[i - 1][j - k - 1], dp[0][j] - dp[0][j - k - 1])
                if dp[i][j] > p:
                    dp[i][j] = p
                    nums[i][j] = k + 1
    ans = []
    j = n - 1
    for i in range(m - 1, -1, -1):
        ans.append(nums[i][j])
        j -= nums[i][j]
    print(dp[-1][-1])
    print(" ".join(map(str, reversed(ans))))
main()
