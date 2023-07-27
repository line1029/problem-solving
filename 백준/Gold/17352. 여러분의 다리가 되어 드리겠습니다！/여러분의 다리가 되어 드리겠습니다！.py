import os, io
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n = int(input())
parent = list(range(n + 1))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
for _ in range(n - 2):
    a, b = map(lambda x: find(int(x)), input().split())
    if a < b:
        parent[a] = b
    else:
        parent[b] = a
ans = []
for i in range(1, n + 1):
    if i == parent[i]:
        ans.append(i)
print(*ans)