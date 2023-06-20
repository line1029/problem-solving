from sys import stdin, stdout
from collections import deque
n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
ind = [0]*(n + 1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    ind[b] += 1

ans = []
q = deque(i for i in range(1, n + 1) if not ind[i])
while q:
    cur = q.popleft()
    ans.append(cur)
    for nex in graph[cur]:
        ind[nex] -= 1
        if not ind[nex]:
            q.append(nex)
stdout.write(" ".join(map(str, ans)))