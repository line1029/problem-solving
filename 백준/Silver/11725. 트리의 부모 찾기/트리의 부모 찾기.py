from sys import stdin, stdout
from collections import deque
from itertools import islice
n = int(stdin.readline())
graph = [[] for _ in range(n + 1)]
parents = [-1]*(n + 1)
parents[1] = 0
for a, b in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
while q:
    cur = q.popleft()
    for nex in graph[cur]:
        if nex != parents[cur]:
            q.append(nex)
            parents[nex] = cur
stdout.write("\n".join(map(str, islice(parents, 2, None))))