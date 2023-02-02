from sys import stdin

def bellman_ford(edges, v):
    dist = [25000001]*(v+1)
    for i in range(v):
        for s, e, w in edges:
            if dist[s] + w < dist[e]:
                if i == v - 1:
                    return True
                dist[e] = dist[s] + w
    return False


for _ in range(int(stdin.readline())):
    edges = []
    n, m, w = map(int, stdin.readline().split())
    for _ in range(m):
        s, e, weight = map(int, stdin.readline().split())
        edges.append([s, e, weight])
        edges.append([e, s, weight])
    for _ in range(w):
        s, e, weight = map(int, stdin.readline().split())
        edges.append([s, e, -weight])
    if bellman_ford(edges, n):
        print("YES")
    else:
        print("NO")