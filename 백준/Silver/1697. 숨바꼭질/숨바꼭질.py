n, k = map(int, input().split())
d = {n:0}
from collections import deque

q = deque([n])
while q and k not in d:
    cur = q.popleft()
    if 0<= cur - 1 <=100000 and cur - 1 not in d:
        d[cur - 1] = d[cur] + 1
        q.append(cur - 1)
    if 0<= cur + 1 <=100000 and cur + 1 not in d:
        d[cur + 1] = d[cur] + 1
        q.append(cur + 1)
    if 0<= cur * 2 <=100000 and cur * 2 not in d:
        d[cur * 2] = d[cur] + 1
        q.append(cur * 2)
print(d[k])
    