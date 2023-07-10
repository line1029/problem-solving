import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, m = int(input()), int(input())
INF = 10_000_001
adj_mat = [[INF]*(n + 1) for _ in range(n + 1)]
transit_mat = [[INF]*(n + 1) for _ in range(n + 1)]
path_mat = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    adj_mat[i][i] = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    adj_mat[a][b] = min(adj_mat[a][b], cost)
    transit_mat[a][b] = 0
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if adj_mat[i][k] != INF and adj_mat[k][j] != INF and adj_mat[i][k] + adj_mat[k][j] < adj_mat[i][j]:
                adj_mat[i][j] = adj_mat[i][k] + adj_mat[k][j]
                transit_mat[i][j] = k
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if adj_mat[i][j] == INF:
            adj_mat[i][j] = 0
def dfs(i, j):
    if path_mat[i][j]:
        return path_mat[i][j]
    if not transit_mat[i][j]:
        path_mat[i][j] = [i]
        return path_mat[i][j]
    if transit_mat[i][j] == INF:
        return
    path = []
    path.extend(dfs(i, transit_mat[i][j]))
    path.extend(dfs(transit_mat[i][j], j))
    path_mat[i][j] = path
    return path

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if adj_mat[i][j] < INF:
            dfs(i, j)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if path_mat[i][j]:
            path_mat[i][j].append(j)
ans = __pypy__.builders.StringBuilder()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ans.append(f"{adj_mat[i][j]} ")
    ans.append("\n")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if path_mat[i][j]:
            ans.append(f"{len(path_mat[i][j])} ")
            for k in path_mat[i][j]:
                ans.append(f"{k} ")
        else:
            ans.append("0 ")
        ans.append("\n")
os.write(1, ans.build().encode())
