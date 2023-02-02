from sys import stdin
n = int(stdin.readline())
triangle = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
for i in range(1, n):
    triangle[i][0] += triangle[i-1][0]
    triangle[i][-1] += triangle[i-1][-1]
    for j in range(1, i):
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
print(max(triangle[-1]))