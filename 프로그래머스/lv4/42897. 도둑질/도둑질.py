def solution(money):
    n = len(money)
    dp = [0]*n
    dp[0] = money[0]
    # dp[1] = money[1]
    dp[2] = dp[0] + money[2]
    dp2 = [0]*n
    dp2[1] = money[1]
    dp2[2] = money[2]
    for i in range(3, n):
        dp[i] += max(dp[i - 2], dp[i - 3]) + money[i]
        dp2[i] += max(dp2[i - 2], dp2[i - 3]) + money[i]
    return max(dp[n-3], dp[n-2], dp2[n-1], dp2[n-2])