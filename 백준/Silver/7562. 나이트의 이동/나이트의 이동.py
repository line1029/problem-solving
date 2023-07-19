from sys import stdin
from collections import deque
def bfs(ans, idx, D):
    n = int(stdin.readline())
    s = list(map(int, stdin.readline().split()))
    e = list(map(int, stdin.readline().split()))
    if s == e:
        return
    visited = [[0]*n for _ in range(n)]
    q = deque([s])
    for depth in range(1, n*n + 1):
        if not q:
            break
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in D:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = depth
                    q.append((ni, nj))
                    if [ni, nj] == e:
                        ans[idx] = depth
                        return

def main():
    t = int(stdin.readline())
    ans = [0]*t
    D = ((2, 1), (1, 2), (-2, 1), (1, -2), (2, -1), (-1, 2), (-1, -2), (-2, -1))
    for tcase in range(t):
        bfs(ans, tcase, D)
    print("\n".join(map(str, ans)))
main()