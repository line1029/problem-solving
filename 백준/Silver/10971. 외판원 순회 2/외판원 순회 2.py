from sys import stdin
input = stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
visited = set()
for i in range(n):
    for idx, d in enumerate(map(int, input().split())):
        if d:
            graph[i].append((idx, d))
ans = 9000000
def backtracking(start_city, cur_city, cur_dist):
    global ans
    if len(visited) == n:
        for nex_city, d in graph[cur_city]:
            if nex_city == start_city:
                ans = min(cur_dist + d, ans)
        return
    for nex_city, d in graph[cur_city]:
        if nex_city not in visited:
            visited.add(nex_city)
            backtracking(start_city, nex_city, cur_dist + d)
            visited.discard(nex_city)
for i in range(n):
    visited.add(i)
    backtracking(i, i, 0)
    visited.discard(i)
print(ans)
    