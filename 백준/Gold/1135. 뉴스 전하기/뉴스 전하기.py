from sys import stdin
n = int(stdin.readline())
parent = list(map(int, stdin.readline().split()))
tree = [[] for _ in range(n)]
for i in range(1, n):
    tree[parent[i]].append(i)
times = [0]*n
for i in range(n - 1, -1, -1):
    if tree[i]:
        tree[i].sort(key=lambda x: -times[x])
        times[i] = max(a + times[b] for a, b in zip(range(1, len(tree[i]) + 1), tree[i]))
    else:
        times[i] = 1
print(times[0] - 1)