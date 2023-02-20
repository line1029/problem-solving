from sys import stdin, stdout
from collections import deque
n = int(stdin.readline())
info = stdin.read().splitlines()
info.pop()
q = deque()
for i in info:
    if i == "0":
        q.popleft()
    elif len(q) == n:
        continue
    else:
        q.append(i)
if not q:
    print("empty")
    exit()
stdout.write(" ".join(q))