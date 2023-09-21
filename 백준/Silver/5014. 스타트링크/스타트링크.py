from collections import deque
from math import gcd
f, s, g, u, d = map(int, input().split())
if u and d and (g - s)%gcd(u, d):
    print("use the stairs")
    exit()
building = [-1]*(f + 1)
building[s] = 0
q = deque([s])
for i in range(1, f + 2):
    if not q: break
    for _ in range(len(q)):
        cur = q.popleft()
        if cur + u <= f and building[cur + u] == -1:
            building[cur + u] = i
            q.append(cur + u)
        if cur - d > 0 and building[cur - d] == -1:
            building[cur - d] = i
            q.append(cur - d)
if building[g] == -1:
    print("use the stairs")
    exit()
print(building[g])
