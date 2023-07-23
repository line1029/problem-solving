import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def bfs():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [-1]*(v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v + 1):
        if visited[i] == -1:
            st = [i]
            visited[i] = 0
            while st:
                cur = st.pop()
                for nex in graph[cur]:
                    if visited[nex] == -1:
                        visited[nex] = visited[cur]^1
                        st.append(nex)
                    elif visited[nex] == visited[cur]:
                        return True

k = int(input())
ans = ["YES"]*k
for i in range(k):
    if bfs():
        ans[i] = "NO"
print("\n".join(ans))