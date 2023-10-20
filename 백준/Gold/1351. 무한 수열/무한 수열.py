n, p, q = map(int, input().split())
cach = {0:1}
def dfs(x):
    if x in cach:
        return cach[x]
    res = dfs(x//p) + dfs(x//q)
    cach[x] = res
    return res
print(dfs(n))