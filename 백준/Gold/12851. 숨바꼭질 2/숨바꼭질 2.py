from sys import stdin
from collections import deque
n, k = map(int, stdin.readline().split())
times = [-1]*(2*max(k, n) + 1)
ways = [0]*(2*max(k, n) + 1)
ways[n] = 1
times[n] = 0
q = deque([n])
for t in range(abs(k - n) + 2):
    if ways[k]:
        print(t)
        print(ways[k])
        exit()
    for _ in range(len(q)):
        cur = q.popleft()
        if cur - 1 >= 0:
            if times[cur - 1] == -1 or times[cur - 1] == t + 1:
                if not ways[cur - 1]:
                    times[cur - 1] = t + 1
                    q.append(cur - 1)
                ways[cur - 1] += ways[cur]
        if cur <= k:
            if times[cur + 1] == -1 or times[cur + 1] == t + 1:
                if not ways[cur + 1]:
                    times[cur + 1] = t + 1
                    q.append(cur + 1)
                ways[cur + 1] += ways[cur]
            if times[2*cur] == -1 or times[2*cur] == t + 1:
                if not ways[2*cur]:
                    times[2*cur] = t + 1
                    q.append(2*cur)
                ways[2*cur] += ways[cur]
