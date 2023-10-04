import io, os
import heapq
def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n, m, k = map(int, input().split())
    INF = 10**11
    dist = [[INF]*(n + 1) for _ in range(k + 1)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    for i in range(k + 1):
        dist[i][0] = 0
    pq = [[0, 0, 1]]
    while pq:
        d, used, cur = heapq.heappop(pq)
        if dist[used][cur] < d: continue
        for nex, nw in graph[cur]:
            if used < k and d < dist[used + 1][nex]:
                dist[used + 1][nex] = d
                heapq.heappush(pq, [d, used + 1, nex])
            nd = d + nw
            if nd < dist[used][nex]:
                dist[used][nex] = nd
                heapq.heappush(pq, [nd, used, nex])
    print(min(dist[i][-1] for i in range(k + 1)))
main()