from sys import stdin
from collections import deque
n, k = map(int, stdin.readline().split())
if n >= k:
    print(n - k)
    exit()
times = [-1] * (2 * k + 1)
times[n] = 0
q = deque([n])
t = 0
while q:
    tmp = []
    for i in q:
        i *= 2
        while i <= 2*k and times[i] == -1:
            times[i] = t
            tmp.append(i)
            if i == k:
                print(t)
                exit()
            i *= 2
    q.extend(tmp)
    for _ in range(len(q)):
        cur = q.popleft()
        if cur >= 1 and times[cur - 1] == -1:
            times[cur - 1] = t + 1
            if cur - 1 == k:
                print(t + 1)
                exit()
            q.append(cur - 1)
        if cur <= 2*k and times[cur + 1] == -1:
            times[cur + 1] = t + 1
            if cur + 1 == k:
                print(t + 1)
                exit()
            q.append(cur + 1)
    t += 1