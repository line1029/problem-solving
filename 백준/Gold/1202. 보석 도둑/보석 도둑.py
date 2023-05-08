from sys import stdin
import heapq
input = stdin.readline
n, k = map(int, input().split())
jewel = [0]*n
for i in range(n):
    jewel[i] = tuple(map(int, input().split()))
bags = list(map(int, stdin.read().splitlines()))
jewel.sort()
bags.sort()
j_idx = b_idx = 0
pq = []
ans = 0
while b_idx < k:
    while j_idx < n and b_idx < k and bags[b_idx] >= jewel[j_idx][0]:
        heapq.heappush(pq, -jewel[j_idx][1])
        j_idx += 1
    if pq:
        ans -= heapq.heappop(pq)
    b_idx += 1

print(ans)