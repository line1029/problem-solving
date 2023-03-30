from sys import stdin
from heapq import heappop, heappush
input = stdin.readline
for _ in range(int(input())):
    min_heap = []
    max_heap = []
    counter = dict()
    total = 0
    for _ in range(int(input())):
        oper, num = input().split()
        num = int(num)
        if oper == "I":
            heappush(min_heap, num)
            heappush(max_heap, -num)
            total += 1
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        else:
            if total == 0:
                continue
            if num == 1:
                while counter[-max_heap[0]] == 0:
                    heappop(max_heap)
                counter[-heappop(max_heap)] -= 1
            else:
                while counter[min_heap[0]] == 0:
                    heappop(min_heap)
                counter[heappop(min_heap)] -= 1
            total -= 1
            if not total:
                min_heap = []
                max_heap = []
    
    
    if not total:
        print("EMPTY")
        continue
    while counter[-max_heap[0]] == 0:
        heappop(max_heap)
    while counter[min_heap[0]] == 0:
        heappop(min_heap)
    print(-max_heap[0], min_heap[0])