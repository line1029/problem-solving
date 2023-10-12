from sys import stdin
n, c = map(int, stdin.readline().split())
m = int(stdin.readline())
boxs = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()), key=lambda x: (x[1], x[0]))
capacity = [c]*n
ans = 0
for a, b, num in boxs:
    if (x:=min(capacity[a:b])):
        ans += (y:=min(x, num))
        for i in range(a, b):
            capacity[i] -= y
print(ans)
