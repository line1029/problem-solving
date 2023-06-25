from sys import stdin
from collections import deque
def main():
    n = int(stdin.readline())
    graph = [[] for _ in range(n + 1)]
    ind = [0]*(n + 1)
    for i, j in enumerate(map(int, stdin.readline().split()), 1):
        graph[i].append(j)
        ind[j] += 1
    q = deque(i for i in range(1, n + 1) if not ind[i])
    ans = 0
    while q:
        cur = q.popleft()
        ans += 1
        for nex in graph[cur]:
            ind[nex] -= 1
            if not ind[nex]:
                q.append(nex)
    return ans
for _ in range(int(stdin.readline())):
    print(main())