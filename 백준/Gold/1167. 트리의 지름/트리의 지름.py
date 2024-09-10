from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)
n = int(stdin.readline())
graph = [None]*(n+1)
visited = [0]*(n+1)
ans = [0, 1]
for _ in range(n):
    v, *edges = map(int, stdin.readline().split())
    graph[v] = [(edges[2*i], edges[2*i + 1]) for i in range(len(edges)//2)]
def dfs(dist, node):
    cnt = 0
    for v, w in graph[node]:
        if not visited[v]:
            visited[v] = 1
            dfs(dist + w, v)
            visited[v] = 0
            cnt += 1
    if not cnt and ans[0] < dist:
        ans[0] = dist
        ans[1] = node
visited[1] = 1
dfs(0, 1)
visited[1] = 0
visited[ans[1]] = 1
dfs(0, ans[1])
print(ans[0])