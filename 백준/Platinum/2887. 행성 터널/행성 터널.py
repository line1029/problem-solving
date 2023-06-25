from sys import stdin
def find(p, x):
    if x != p[x]:
        p[x] = find(p, p[x])
    return p[x]
def union(s, p, x, y):
    x, y = find(p, x), find(p, y)
    if x == y:
        return False
    if s[x] < s[y]:
        x, y = y, x
    s[x] += s[y]
    p[y] = x
    return s[x]
def main():
    # kruskal
    n = int(stdin.readline())
    planets = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
    idxs = list(range(n))
    edges = [0]*(n - 1)*3
    for i in range(3):
        idxs.sort(key=lambda x: planets[x][i])
        for j in range(n - 1):
            edges[i*(n - 1) + j] = (abs(planets[idxs[j]][i] - planets[idxs[j + 1]][i]), idxs[j], idxs[j + 1])
    edges.sort()
    parent = list(range(n))
    size = [1]*n
    ans = 0
    for e, i, j in edges:
        cnt = union(size, parent, i, j)
        if cnt:
            ans += e
        if cnt == n:
            break
    return ans
print(main())