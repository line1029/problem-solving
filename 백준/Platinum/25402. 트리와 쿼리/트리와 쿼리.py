from sys import stdin, stdout
n = int(stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [-1]*(n + 1)
for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
q = int(stdin.readline())
res = [0]*q
for idx in range(q):
    k, *s = map(int, stdin.readline().split())
    ss = set(s)
    ans = 0
    for i in s:
        if visited[i] != idx:
            visited[i] = idx
            cnt = 1
            stack = [i]
            while stack:
                cur = stack.pop()
                for nex in graph[cur]:
                    if nex in ss and visited[nex] != idx:
                        stack.append(nex)
                        cnt += 1
                        visited[nex] = idx
            ans += cnt * (cnt - 1) // 2
    res[idx] = ans
stdout.write("\n".join(map(str, res)))