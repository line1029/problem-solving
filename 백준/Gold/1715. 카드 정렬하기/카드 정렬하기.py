from sys import stdin
import heapq
n = int(stdin.readline())
pq = list(map(int, stdin.read().splitlines()))
heapq.heapify(pq)
ans = 0
while pq:
    cur = heapq.heappop(pq)
    if pq:
        cur += heapq.heappop(pq)
        heapq.heappush(pq, cur)
        ans += cur
print(ans)