# use topological sort with priority queue
from sys import stdin, stdout
import heapq
n, m = map(int, stdin.readline().split())
graph = [list() for _ in range(n + 1)]
ind_arr = [0]*(n + 1)
for pre, nex in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    graph[pre].append(nex)
    ind_arr[nex] += 1

pq = [i for i in range(1, n + 1) if not ind_arr[i]]
heapq.heapify(pq)
ans = []
while pq:
    cur = heapq.heappop(pq)
    ans.append(cur)
    for node in graph[cur]:
        ind_arr[node] -= 1
        if not ind_arr[node]:
            heapq.heappush(pq, node)
stdout.write(" ".join(map(str, ans)))