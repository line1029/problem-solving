from sys import stdin, stdout
from collections import deque
n, k = map(int, stdin.readline().split())
ind = [0]*(n + 1)
graph = [[] for _ in range(n + 1)]
history = [0]*(n + 1)
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    ind[b] += 1
q = deque(i for i, v in enumerate(ind) if i and not v)
while q:
    cur = q.popleft()
    for nex in graph[cur]:
        history[nex] |= 1 << cur
        history[nex] |= history[cur]
        ind[nex] -= 1
        if not ind[nex]:
            q.append(nex)
stdin.readline()
ans = []
for a, b in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    if history[a] & (1 << b):
        ans.append(1)
    elif history[b] & (1 << a):
        ans.append(-1)
    else:
        ans.append(0)
stdout.write("\n".join(map(str, ans)))