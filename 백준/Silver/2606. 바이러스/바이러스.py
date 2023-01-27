from sys import stdin
from collections import defaultdict, deque
n = int(stdin.readline())
e = int(stdin.readline())
edges = list(map(lambda x : list(map(int, x.split())), stdin.readlines()))
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
q = deque([1])
visited = {1}
while q:
    cur = q.popleft()
    for nex in graph[cur]:
        if nex not in visited:
            visited.add(nex)
            q.append(nex)
print(len(visited) - 1)