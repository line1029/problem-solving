import os, io
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0]*(n + 1)
visited[1] = 1
ans = 0
q = deque([1])
for i in range(1, n + 2):
    if not q: break
    for _ in range(len(q)):
        cur = q.popleft()
        for nex in graph[cur]:
            if not visited[nex]:
                visited[nex] = 1
                q.append(nex)
                if len(graph[nex]) == 1:
                    ans += i
print("Yes" if ans&1 else "No")