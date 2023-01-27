n = int(input())
dp = {1:0, 2:1, 3:1}
def rec(num):
    if num in dp:
        return dp[num]
    ans = 1 + min(rec(num//3) + num%3, rec(num//2) + num%2)
    dp[num] = ans
    return ans
print(rec(n))