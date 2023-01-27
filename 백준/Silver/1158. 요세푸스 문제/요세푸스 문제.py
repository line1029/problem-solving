from sys import stdin
from collections import deque
n, k = map(int, stdin.readline().split())
seq = []
queue = deque(map(str, range(1, n+1)))
while queue:
    queue.rotate(-k+1)
    seq.append(queue.popleft())
print(f'<{", ".join(seq)}>')