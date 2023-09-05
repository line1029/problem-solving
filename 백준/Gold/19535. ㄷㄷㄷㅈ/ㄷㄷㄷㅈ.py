import os, io
from math import comb
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
graph = [0]*(n + 1)
edges = [0]*(n - 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a] += 1
    graph[b] += 1
    edges[i] = [a, b]
D_tree = G_tree = 0
for i in range(1, n + 1):
    G_tree += comb(graph[i], 3)
G_tree *= 3
for a, b in edges:
    D_tree += (graph[a] - 1)*(graph[b] - 1)
if D_tree > G_tree:
    print("D")
elif D_tree < G_tree:
    print("G")
else:
    print("DUDUDUNGA")