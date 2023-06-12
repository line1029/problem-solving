from sys import stdin, stdout
from itertools import chain
from collections import deque, defaultdict
n = int(stdin.readline())
alphabet_to_idx = dict(chain(([chr(65 + i),i] for i in range(25)), ([chr(97 + i),i + 25] for i in range(26)), [["Z", 51]]))
visited = [0]*52
graph = [defaultdict(int) for _ in range(52)]
for i in range(n):
    a, b, c = stdin.readline().split()
    a, b = alphabet_to_idx[a], alphabet_to_idx[b]
    c = int(c)
    graph[a][b] += c
    graph[b][a] += c


while True:
    # series pipe
    flag = f1 = True
    while flag:
        flag = False
        for i in range(1, 51):
            if len(graph[i]) == 2:
                left, right = graph[i].keys()
                flow = min(graph[i].values())
                flag = True
                graph[left][right] += flow
                graph[right][left] += flow
                graph[left].pop(i)
                graph[right].pop(i)
                graph[i].clear()
                f1 = False

    # parralel pipe are automatically added

    # delete useless pipe
    for i in range(1, 51):
        if len(graph[i]) == 1:
            prev = next(iter(graph[i]))
            graph[i].clear()
            graph[prev].pop(i)
    if f1:
        break
print(graph[0][51])