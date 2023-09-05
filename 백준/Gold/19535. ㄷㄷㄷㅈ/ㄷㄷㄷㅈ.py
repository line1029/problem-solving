import os, io
from math import comb
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
D_tree = G_tree = 0
g = dict()
for i in range(1, n + 1):
    if (k:=len(graph[i])) == 1: continue
    if k in g:
        g[k] += 1
    else:
        g[k] = 1
    for j in graph[i]:
        if j < i: continue
        if (l:= len(graph[j])) != 1:
            D_tree += (k - 1)*(l - 1)
for k, v in g.items():
    G_tree += v*comb(k, 3)
G_tree *= 3
if D_tree > G_tree:
    print("D")
elif D_tree < G_tree:
    print("G")
else:
    print("DUDUDUNGA")