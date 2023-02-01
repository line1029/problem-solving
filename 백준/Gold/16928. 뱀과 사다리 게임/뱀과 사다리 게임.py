from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
graph = dict(map(lambda x: map(int, x.split()), stdin.read().splitlines()))
ladder_snake = set(graph.keys())
dist = [-1]*101
dist[1] = 0
for i in range(1, 101):
    if i not in graph:
        graph[i] = list(range(min(i+6, 100), i, -1))
q = deque([(1, 0)])
while q:
    cur_node, cur_depth = q.popleft()
    if cur_node == 100:
        print(cur_depth)
        exit()
    if cur_node in ladder_snake:
        cur_node = graph[cur_node]
    for nex_node in graph[cur_node]:
        if dist[nex_node] == -1:
            dist[nex_node] = cur_depth + 1
            q.append((nex_node, cur_depth + 1))