import os, io
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def find(x):
    while parent[x] != x:
        x, parent[x] = parent[x], parent[parent[x]]
    return x

ans = []
for _ in range(int(input())):
    n = int(input())
    parent = list(range(n))
    x, y, r = [0]*n, [0]*n, [0]*n
    for i in range(n):
        x[i], y[i], r[i] = map(int, input().split())
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (x[i] - x[j])**2 + (y[i] - y[j])**2 <= (r[i] + r[j])**2:
                a, b = find(i), find(j)
                if a > b:
                    parent[b] = a
                else:
                    parent[a] = b
    ans.append(sum(parent[i] == i for i in range(n)))
print("\n".join(map(str, ans)))