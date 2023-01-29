from sys import stdin, stdout
from heapq import heappush, heappop
n = int(stdin.readline())
nums = map(int, stdin.readlines())
abs_heap = []
for num in nums:
    if not num and abs_heap:
        stdout.write(f"{heappop(abs_heap)[1]}\n")
    elif not num:
        stdout.write("0\n")
    else:
        heappush(abs_heap, (abs(num), num))