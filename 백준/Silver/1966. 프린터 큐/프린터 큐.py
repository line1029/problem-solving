from sys import stdin
from collections import deque
for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    tmp = stdin.readline().split()
    priority = deque(sorted(map(int, tmp), reverse = True))
    q = deque((int(tmp[i]), True) if i == m else (int(tmp[i]), False) for i in range(n))
    order = 1
    _max = priority[0]
    while q:
        if q[0][0] == _max:
            o, t = q.popleft()
            priority.popleft()
            if t:
                break
            order += 1
            _max = priority[0]
        else:
            q.rotate(-1)
    print(order)