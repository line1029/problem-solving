from sys import stdin
from heapq import heappush, heappop
n = int(stdin.readline())
operations = map(int, stdin.readlines())
max_heap = list()
for op in operations:
    if op == 0 and max_heap:
        print(-heappop(max_heap))
    elif op == 0:
        print(0)
    else:
        heappush(max_heap, -op)
    