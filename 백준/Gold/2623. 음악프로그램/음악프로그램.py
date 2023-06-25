from sys import stdin, stdout
from collections import deque
def main():
    n, m = map(int, stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    ind = [0]*(n + 1)
    for _ in range(m):
        k, *arr = map(int, stdin.readline().split())
        for i in range(1, len(arr)):
            graph[arr[i - 1]].append(arr[i])
            ind[arr[i]] += 1
    q = deque(i for i in range(1, n + 1) if not ind[i])
    ans = []
    while q:
        cur = q.popleft()
        ans.append(cur)
        for nex in graph[cur]:
            ind[nex] -= 1
            if not ind[nex]:
                q.append(nex)
    if len(ans) < n:
        print(0)
    else:
        stdout.write("\n".join(map(str, ans)))
main()