from sys import stdin
import heapq
n = int(stdin.readline())
arr = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
pq = []
ans = 0
for s, e in arr:
    while pq and pq[0] <= s:
        heapq.heappop(pq)
    heapq.heappush(pq, e)
    ans = max(ans, len(pq))
print(ans)