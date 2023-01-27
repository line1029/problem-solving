from collections import defaultdict, deque
from sys import stdin
n, m, v = map(int, stdin.readline().split())
edges = list(map(lambda x: list(map(int, x.split())), stdin.readlines()))
graph = defaultdict(list)
for s, e in edges:
    graph[s].append(e)
    graph[e].append(s)
for val in graph.values():
    val.sort()

bfs_ans = []
bfs_visited = set([v])
q = deque([v])
while q:
    cur = q.popleft()
    bfs_ans.append(cur)
    for nex in graph[cur]:
        if nex not in bfs_visited:
            bfs_visited.add(nex)
            q.append(nex)
dfs_ans = []
dfs_visited = set([v])
def dfs(node):
    dfs_ans.append(node)
    for nex in graph[node]:
        if nex not in dfs_visited:
            dfs_visited.add(nex)
            dfs(nex)
dfs(v)
print(" ".join(map(str, dfs_ans)))
print(" ".join(map(str, bfs_ans)))