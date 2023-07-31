import os, io, __pypy__
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n = int(input())
parent = list(range(n + 1))
def find(x):
    while parent[x] != x:
        x, parent[x] = parent[x], parent[parent[x]]
    return x
for _ in range(n - 2):
    a, b = map(lambda x: find(int(x)), input().split())
    if a < b:
        parent[a] = b
    else:
        parent[b] = a
ans = __pypy__.builders.StringBuilder()
for i in range(1, n + 1):
    if i == parent[i]:
        ans.append(f"{i} ")
os.write(1, ans.build().encode())