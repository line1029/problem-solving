from sys import stdin
from collections import deque
def main():
    n = int(stdin.readline())
    compl = [0]*(n + 1)
    need = [0]*(n + 1)
    ind = [0]*(n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        need[i], ind[i], *s = map(int, stdin.readline().split())
        for j in s:
            graph[j].append(i)
    q = deque(i for i, x in enumerate(ind) if not x)
    q.popleft()
    for i, x in enumerate(ind):
        if not x:
            compl[i] = need[i]
    for _ in range(n + 1):
        if not q: break
        for __ in range(len(q)):
            cur = q.popleft()
            for i in graph[cur]:
                if ind[i]:
                    ind[i] -= 1
                    compl[i] = max(compl[i], compl[cur] + need[i])
                    if not ind[i]:
                        q.append(i)
    print(max(compl))
main()