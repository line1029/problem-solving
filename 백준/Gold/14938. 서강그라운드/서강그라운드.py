from sys import stdin
n, m, r = map(int, stdin.readline().split())
graph = [[1501]*n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0
values = list(map(int, stdin.readline().split()))
for a, b, dist in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    a -= 1
    b -= 1
    graph[a][b] = graph[b][a] = min(dist, graph[a][b])
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
print(max(sum(values[i] for i, num in enumerate(row) if num <= m) for row in graph))