from sys import stdin
import heapq
from collections import defaultdict
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    max_pq = []
    min_pq = []
    pq_log = defaultdict(int)
    cnt = 0
    for i in range(n):
        action, num = stdin.readline().split()
        if action == "D":
            if not cnt:
                continue
            if num == "-1":
                while not pq_log[min_pq[0]]:
                    heapq.heappop(min_pq)
                pq_log[heapq.heappop(min_pq)] -= 1
            elif num == "1":
                while not pq_log[-max_pq[0]]:
                    heapq.heappop(max_pq)
                pq_log[-heapq.heappop(max_pq)] -= 1
            cnt -= 1
            if not cnt:
                max_pq = []
                min_pq = []
        else:
            num = int(num)
            heapq.heappush(min_pq, num)
            heapq.heappush(max_pq, -num)
            pq_log[num] += 1
            cnt += 1
    if cnt:
        while not pq_log[-max_pq[0]]:
            heapq.heappop(max_pq)
        while not pq_log[min_pq[0]]:
            heapq.heappop(min_pq)
        print(-max_pq[0], min_pq[0])
    else:
        print("EMPTY")