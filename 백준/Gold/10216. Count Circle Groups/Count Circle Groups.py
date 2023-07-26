from sys import stdin
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if size[x] < size[y]:
        x, y = y, x
    parent[y] = x
    size[x] += size[y]

ans = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    parent = list(range(n))
    size = [1]*n
    x, y, r = [0]*n, [0]*n, [0]*n
    for i in range(n):
        x[i], y[i], r[i] = map(int, stdin.readline().split())
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (x[i] - x[j])**2 + (y[i] - y[j])**2 <= (r[i] + r[j])**2:
                union(i, j)
    ans.append(sum(parent[i] == i for i in range(n)))
print("\n".join(map(str, ans)))