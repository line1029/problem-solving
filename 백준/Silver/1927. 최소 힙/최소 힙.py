from sys import stdin
import heapq
n = int(stdin.readline())
queries = list(map(int, stdin.readlines()))

h = []
for query in queries:
    if query == 0:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, query)