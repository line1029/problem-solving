from sys import stdin
from collections import deque
def main():
    n, m = map(int, stdin.readline().split())
    INF = 20001
    dist = [INF]*(n + 1)
    dist[0] = dist[1] = 0
    graph = [[] for _ in range(n + 1)]
    for a, b in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
        graph[a].append(b)
        graph[b].append(a)
    pq = deque([1])
    for cost in range(1, 20002):
        if not pq:
            break
        for _ in range(len(pq)):
            cur = pq.popleft()
            for nex in graph[cur]:
                if cost < dist[nex]:
                    dist[nex] = cost
                    pq.append(nex)
    k = max(dist)
    print(dist.index(k), k, dist.count(k))
main()