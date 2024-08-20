from collections import defaultdict, deque
def solution(edges):
    graph = defaultdict(list)
    ind = defaultdict(int)
    oud =  defaultdict(int)
    n = 0
    l = len(edges)
    for a, b in edges:
        n = max(n, a, b)
        graph[a].append(b)
        ind[b] += 1
        oud[a] += 1
    start = max(filter(lambda x: not ind[x], range(1, n + 1)), key=lambda y: oud[y])
    if oud[start] == 1:
        return [start, 0, 1, 0]
    res = [start, 0, 0, 0]
    for graph_start in graph[start]:
        ind[graph_start] -= 1
        if ind[graph_start] != oud[graph_start] or not ind[graph_start]:
            res[2] += 1
        elif ind[graph_start] == oud[graph_start] == 2:
            res[3] += 1
        else:
            visited = set()
            cur = graph_start
            while cur not in visited:
                visited.add(cur)
                if ind[cur] == oud[cur] == 2:
                    res[3] += 1
                    break
                elif ind[cur] != oud[cur]:
                    res[2] += 1
                    break
                else:
                    cur = graph[cur][0]
            else:
                res[1] += 1
    return res
                
        
        