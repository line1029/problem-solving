from sys import stdin
from collections import deque

def main():
    n, d = map(int, stdin.readline().split())
    ans = [10001]*(d + 1)
    graph = [[] for _ in range(d + 1)]
    for _ in range(n):
        s, e, dist = map(int, stdin.readline().split())
        if e > d or dist >= e - s: continue
        graph[s].append((e, dist))
    q = deque([(0, 0)])
    while q:
        cur, cur_d = q.popleft()
        if ans[cur] < cur_d: continue
        if cur < d:
            if ans[cur + 1] > cur_d + 1:
                ans[cur + 1] = cur_d + 1
                q.append((cur + 1, cur_d + 1))
        for nex, nex_d in graph[cur]:
            if ans[nex] > cur_d + nex_d:
                ans[nex] = cur_d + nex_d
                q.append((nex, cur_d + nex_d))
    print(ans[-1])
main()