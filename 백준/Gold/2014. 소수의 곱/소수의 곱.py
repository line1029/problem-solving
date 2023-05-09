from sys import stdin
import heapq
k, n = map(int, stdin.readline().split())
primes = list(map(int, stdin.readline().split()))
s = set(primes)
pq = primes[:]
heapq.heapify(pq)
max_val = primes[-1]
for i in range(1, n + 1):
    ans = heapq.heappop(pq)
    for p in primes:
        nex_val = ans * p
        if i + len(pq) >= n and max_val < nex_val:
            break
        if nex_val not in s:
            max_val = max(max_val, nex_val)
            s.add(nex_val)
            heapq.heappush(pq, nex_val)
print(ans)