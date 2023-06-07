from sys import stdin, stdout
INF = 1e9
n, m = int(stdin.readline()), int(stdin.readline())
cities = [[INF]*n for _ in range(n)]
for i in range(n):
    cities[i][i] = 0
for i, j, c in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    cities[i-1][j-1] = min(cities[i-1][j-1], c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            cities[i][j] = min(cities[i][j], cities[i][k] + cities[k][j])
for i in range(n):
    for j in range(n):
        if cities[i][j] == INF:
            cities[i][j] = 0
stdout.write("\n".join(" ".join(map(str, i)) for i in cities))