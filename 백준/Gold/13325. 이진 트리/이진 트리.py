from sys import stdin
k = int(stdin.readline())
edges = list(map(int, stdin.readline().split()))
paths = [0]*(1 << k)
for i in range(1 << k):
    j = i + (1 << k)
    while j > 1:
        paths[i] += edges[j - 2]
        j >>= 1
ans = sum(edges)
s = max(paths)
n = 1 << k
for i in range(1, k + 1):
    for j in range(1 << i):
        x = s - max(paths[j*(1 << (k - i)):(j + 1)*(1 << (k - i))])
        ans += x
        for l in range(j*(1 << (k - i)), (j + 1)*(1 << (k - i))):
            paths[l] += x
print(ans)