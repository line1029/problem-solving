from sys import stdin
# naive O(height)
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    parent = [-1]*(n + 1)
    for _ in range(n - 1):
        a, b = map(int, stdin.readline().split())
        parent[b] = a
    a, b = map(int, stdin.readline().split())
    pa, pb = [], []
    while a != -1:
        pa.append(a)
        a = parent[a]
    while b != -1:
        pb.append(b)
        b = parent[b]
    p = -1
    while pa and pb and pa[-1] == pb[-1]:
        p = pa.pop()
        pb.pop()
    print(p)