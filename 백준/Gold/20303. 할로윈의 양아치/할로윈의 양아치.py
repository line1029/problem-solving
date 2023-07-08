from sys import stdin
n, m, k = map(int, stdin.readline().split())
candies = [0]
candies.extend(map(int, stdin.readline().split()))
visited = [0]*(n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

values = []
weights = []
for i in range(1, n + 1):
    if not visited[i]:
        cnt = 1
        candidate = candies[i]
        stack = [i]
        visited[i] = 1
        while stack:
            cur = stack.pop()
            for nex in graph[cur]:
                if not visited[nex]:
                    visited[nex] = 1
                    stack.append(nex)
                    cnt += 1
                    candidate += candies[nex]
        values.append(candidate)
        weights.append(cnt)
idxs = list(range(len(values)))
idxs.sort(key=lambda x: (weights[x], -values[x]))
values = [values[i] for i in idxs]
weights = [weights[i] for i in idxs]
dp = [0]*k
cur_max = 0
for i in range(len(values)):
    cur_max = min(k - 1, cur_max + weights[i])
    for j in range(cur_max, weights[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
print(max(dp))
