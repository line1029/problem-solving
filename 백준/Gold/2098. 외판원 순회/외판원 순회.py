from sys import stdin
n = int(stdin.readline())
citys = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
INF = 16_000_001
dp = [[-1]*(1 << n) for _ in range(n)]
al = (1 << n) - 1
def dfs(cur_city, visited):
    if dp[cur_city][visited] != -1:
        return dp[cur_city][visited]
    if visited == al:
        if citys[cur_city][0]:
            dp[cur_city][visited] = citys[cur_city][0]
        else:
            dp[cur_city][visited] = INF
        return dp[cur_city][visited]
    dp[cur_city][visited] = INF
    for i in range(n):
        if not visited & (1 << i) and citys[cur_city][i]:
            dp[cur_city][visited] = min(dp[cur_city][visited], dfs(i, visited|1 << i) + citys[cur_city][i])
    return dp[cur_city][visited]
print(dfs(0, 1))