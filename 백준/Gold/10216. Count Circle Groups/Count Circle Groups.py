from sys import stdin
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

ans = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    parent = list(range(n))
    x, y, r = [0]*n, [0]*n, [0]*n
    for i in range(n):
        x[i], y[i], r[i] = map(int, stdin.readline().split())
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (x[i] - x[j])**2 + (y[i] - y[j])**2 <= (r[i] + r[j])**2:
                a, b = find(i), find(j)
                if a != b:
                    parent[b] = a
    ans.append(sum(parent[i] == i for i in range(n)))
print("\n".join(map(str, ans)))