from collections import deque
n, m = map(int, input().split())
d = deque(range(1, n + 1))
order = map(int, input().split())
ans = 0
for wanted in order:
    tmp = 0
    while d[0] != wanted:
        d.rotate(-1)
        tmp += 1
    d.popleft()
    ans += min(tmp, len(d) - tmp + 1)
print(ans)