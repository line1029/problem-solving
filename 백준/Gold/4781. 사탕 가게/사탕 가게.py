from sys import stdin
def candies(s):
    n, m = s.split()
    return int(n), int(m[:-3] + m[-2:])
while True:
    n, m = candies(stdin.readline())
    if not n and not m: break
    dp = [0]*(m + 1)
    candy = sorted((candies(stdin.readline()) for _ in range(n)), key=lambda x: x[1])
    for i in range(1, m + 1):
        for v, j in candy:
            if i - j >= 0:
                dp[i] = max(dp[i], dp[i - j] + v)
    print(dp[m])