from sys import stdin, stdout
def main():
    n, m, r = map(int, stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0]*(n + 1)
    stack = [r]
    for a, b in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
        graph[a].append(b)
        graph[b].append(a)
    order = 1
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        visited[cur] = order
        order += 1
        for nex in sorted(graph[cur], reverse=True):
            if not visited[nex]:
                stack.append(nex)
    stdout.write("\n".join(map(str, visited[1:])))

main()