def main():
    n = int(input())
    if n <= 4:
        if n & 1:
            print("CY")
        else:
            print("SK")
        exit()
    dp = [False]*n
    dp[-4:] = [True, False, True, False]
    for i in range(5, n + 1):
        dp[n - i] = not all([dp[n - i + 1], dp[n - i + 3], dp[n - i + 4]])
    if dp[0]:
        print("SK")
    else:
        print("CY")
main()