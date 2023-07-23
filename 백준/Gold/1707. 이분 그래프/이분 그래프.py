import io, os
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def bfs():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0]*(v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v + 1):
        if not visited[i]:
            q = deque([i])
            visited[i] = 1
            for j in range(1, v*e + 2):
                if not q:
                    break
                for _ in range(len(q)):
                    cur = q.popleft()
                    for nex in graph[cur]:
                        if not visited[nex]:
                            visited[nex] = (j&1) + 1
                            q.append(nex)
                        elif visited[nex] != (j&1) + 1:
                            return True

k = int(input())
ans = ["YES"]*k
for i in range(k):
    if bfs():
        ans[i] = "NO"
print("\n".join(ans))