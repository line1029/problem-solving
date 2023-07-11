from sys import stdin
n, m = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
parent = list(range(m*n + 1))
rank = [0]*(m*n + 1)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return 0
    if rank[x] < rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[x] += 1
    parent[y] = x
    return 1

ans = m*n
for i in range(n):
    for j in range(m):
        if grid[i][j] == "D":
            ans -= union(i*m + j, (i + 1)*m + j)
        elif grid[i][j] == "U":
            ans -= union(i*m + j, (i - 1)*m + j)
        elif grid[i][j] == "R":
            ans -= union(i*m + j, i*m + j + 1)
        else:
            ans -= union(i*m + j, i*m + j - 1)
print(ans)