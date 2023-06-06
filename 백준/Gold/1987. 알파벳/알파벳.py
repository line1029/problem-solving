from sys import stdin
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
r, c = map(int, stdin.readline().split())
grid = stdin.read().splitlines()
visited = [[0]*c for _ in range(r)]
_max = (1 << 26) - 1
ans = 1
stack = [(1, 0, 0, 1 << (ord(grid[0][0]) - 65))]
while stack:
    depth, i, j, path = stack.pop()
    if depth > ans:
        ans = depth
        if path == _max:
            print(ans)
            exit()
    for di, dj in D:
        ni, nj = i + di, j + dj
        if 0<=ni<r and 0<=nj<c:
            letter = 1 << (ord(grid[ni][nj]) - 65)
            if not (path & letter) and visited[ni][nj] != (path|letter):
                visited[ni][nj] = path|letter
                stack.append((depth + 1, ni, nj, path|letter))
print(ans)
