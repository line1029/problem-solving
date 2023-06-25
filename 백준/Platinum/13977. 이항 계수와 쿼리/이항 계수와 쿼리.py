from sys import stdin, stdout
MOD = 1_000_000_007
m = int(stdin.readline())
queries = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
_max = max(i[0] for i in queries)
f = [0]*(_max + 1)
f[0] = 1
for i in range(1, _max + 1):
    f[i] = f[i - 1]*i%MOD
ans = [0]*m
for i, (n, k) in enumerate(queries):
    if not k or k == n:
        ans[i] = 1
    else:
        ans[i] = f[n]*pow(f[k]*f[n-k]%MOD, MOD - 2, MOD)%MOD
stdout.write("\n".join(map(str, ans)))