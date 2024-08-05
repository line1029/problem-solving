from sys import stdin

n = int(stdin.readline())
x, y = map(int, stdin.readline().split())
m = int(stdin.readline())
grid = dict()
for i, j in map(lambda e: map(int, e.split()), stdin.readlines()):
    if i not in grid:
        grid[i] = set()
    if j not in grid:
        grid[j] = set()
    grid[i].add(j)
    grid[j].add(i)
dist = [-1] * (n + 1)
dist[x] = 0
stack = [[x, 0]]
while stack:
    cur, d = stack.pop()
    for nex in grid[cur]:
        if dist[nex] == -1:
            dist[nex] = d + 1
            stack.append([nex, d + 1])
print(dist[y])
