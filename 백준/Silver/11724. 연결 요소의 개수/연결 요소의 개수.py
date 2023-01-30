from sys import stdin
from collections import defaultdict
n, m = map(int, stdin.readline().split())
edges = map(lambda x: tuple(map(int, x.split())), stdin.read().splitlines())
graph = defaultdict(list)
for n1, n2 in edges:
    graph[n1].append(n2)
    graph[n2].append(n1)
visited = [0]*n
cnt = 0
for node in range(1, n+1):
    if not visited[node - 1]:
        cnt += 1
        visited[node - 1] = 1
        stack = [node]
        while stack:
            cur = stack.pop()
            for nex in graph[cur]:
                if not visited[nex - 1]:
                    visited[nex - 1] = 1
                    stack.append(nex)
            
print(cnt)