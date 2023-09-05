import os, io
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def main():
    n = int(input())
    parent = [[0]*(n + 1) for _ in range(len(bin(n)) - 1)]
    depth = [0]*(n + 1)
    visited = [0]*(n + 1)
    visited[1] = 1
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    q = deque([1])
    for i in range(1, n + 1):
        if not q: break
        for _ in range(len(q)):
            cur = q.popleft()
            for nex in graph[cur]:
                if visited[nex]: continue
                visited[nex] = 1
                parent[0][nex] = cur
                depth[nex] = i
                q.append(nex)
    p = parent[0]
    k = len(parent)
    for i in range(1, k):
        for j in range(2, n + 1):
            parent[i][j] = parent[i - 1][parent[i - 1][j]]
    m = int(input())
    ans = [0]*m
    for i in range(m):
        a, b = map(int, input().split())
        if depth[a] < depth[b]:
            a, b = b, a
        elif a == b:
            ans[i] = a
            continue
        d = depth[a] - depth[b]
        r = 0
        while d:
            if d&1:
                a = parent[r][a]
            d >>= 1
            r += 1
        while p[a] != p[b]:
            for r in range(1, k):
                if parent[r][a] == parent[r][b]:
                    r -= 1
                    a, b = parent[r][a], parent[r][b]
                    break
        if a != b:
            a = p[a]
        ans[i] = a
    print("\n".join(map(str, ans)))
main()