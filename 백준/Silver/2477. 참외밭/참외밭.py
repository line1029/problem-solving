from sys import stdin
k = int(stdin.readline())
edges = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
for i in range(6):
    if edges[i][0] == edges[(i+2)%6][0] and edges[(i+1)%6][0] == edges[(i+3)%6][0]:
        if i <= 2:
            edges = edges[i:i+4]
        else:
            edges = edges[i:] + edges[:(i+4)%6]
        break
x1, y1, x2, y2 = [i[1] for i in edges]
print(((x1 + x2)*(y1 + y2) - y1*x2)*k)