from sys import stdin
import heapq

n = int(stdin.readline())
classes = sorted(map(lambda x: list(map(int, x.split())), stdin.readlines()))
pq = []
res = 1
for s, t in classes:
    if pq and pq[0][0] <= s:
        heapq.heappop(pq)
    heapq.heappush(pq, [t, s])
    res = max(res, len(pq))
print(res)
