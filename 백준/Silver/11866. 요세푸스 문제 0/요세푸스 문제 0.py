from collections import deque
n, k = map(int,input().split())
q = deque(range(1, n+1))
ans = []
while q:
    q.rotate(-k+1)
    ans.append(q.popleft())
print("<" + ", ".join(map(str, ans)) + ">")