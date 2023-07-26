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
    enemies = [list(map(int, stdin.readline().split())) for _ in range(n)]
    for i in range(n - 1):
        x1, y1, r1 = enemies[i]
        for j in range(i + 1, n):
            x2, y2, r2 = enemies[j]
            if (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2) <= (r1 + r2)*(r1 + r2):
                union(i, j)
    ans.append(sum(parent[x] == x for x in range(n)))
print("\n".join(map(str, ans)))