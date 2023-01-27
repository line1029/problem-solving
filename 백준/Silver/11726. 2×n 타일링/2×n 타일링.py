n = int(input())
mod = 10007
dp = {1:1, 2:2}
def fibo_recur(num):
    if num in dp:
        return dp[num]
    ans = fibo_recur(num - 1) + fibo_recur(num - 2)
    ans %= mod
    dp[num] = ans
    return ans
print(fibo_recur(n))