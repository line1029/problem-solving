from sys import stdin, setrecursionlimit
setrecursionlimit(10001)
n = int(stdin.readline())
graph = [list() for _ in range(n+1)]
visited = [0]*(n+1)
ans = [0, 1]
edges = map(lambda x: map(int, x.split()), stdin.read().splitlines())
for s, e, w in edges:
    graph[s].append((e, w))
    graph[e].append((s, w))

def dfs(dist, node):
    cnt = 0
    for nex, weight in graph[node]:
        if not visited[nex]:
            visited[nex] = 1
            dfs(dist + weight, nex)
            visited[nex] = 0
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