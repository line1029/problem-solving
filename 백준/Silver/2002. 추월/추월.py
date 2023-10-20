from sys import stdin
n = int(stdin.readline())
ans = 0
cars = [stdin.readline().strip() for _ in range(n)]
order = {v:i for i, v in enumerate(cars)}
visited = [0]*n
nex = 0
for i in range(n):
    car = stdin.readline().strip()
    visited[order[car]] = 1
    if order[car] > order[cars[nex]]:
        ans += 1
    else:
        while nex < n and visited[nex]:
            nex += 1
    
print(ans)