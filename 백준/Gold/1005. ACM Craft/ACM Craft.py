from sys import stdin
from collections import deque
ans = []
for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    times = list(map(int, stdin.readline().split()))
    graph = [[] for _ in range(n + 1)]
    ind = [0]*(n + 1)
    need = [0]*(n + 1)
    for _ in range(k):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        ind[b] += 1
    w = int(stdin.readline())
    q = deque(i for i in range(1, n + 1) if not ind[i])
    for i in q:
        need[i] = times[i - 1]
    while q:
        cur = q.popleft()
        for nex in graph[cur]:
            need[nex] = max(need[nex], times[nex - 1] + need[cur])
            ind[nex] -= 1
            if not ind[nex]:
                if nex == w:
                    break
                q.append(nex)
        else:
            continue
        break
    ans.append(need[w])
print("\n".join(map(str, ans)))