from sys import stdin
from collections import deque
a, b = map(int, stdin.readline().split())
q = deque([a])
t = 2
while q:
    for _ in range(len(q)):
        cur = q.popleft()
        if 2*cur <= b:
            if 2*cur == b:
                break
            q.append(2*cur)
        if 10*cur + 1 <= b:
            if 10*cur + 1 == b:
                break
            q.append(10*cur + 1)
    else:
        t += 1
        continue
    break
    
else:
    print(-1)
    exit()
print(t)