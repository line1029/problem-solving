from sys import stdin
from collections import defaultdict, deque
n = int(stdin.readline())
mat = list(map(lambda x: list(map(int, x.strip())), stdin.readlines()))
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
q = deque()
visited = set()
ans = []
for i in range(n):
    for j in range(n):
        if mat[i][j]:
            mat[i][j] = 0
            q.append((i, j))
            visited.add((i, j))
            while q:
                y, x = q.popleft()
                for dy, dx in directions:
                    row, col = y+dy, x+dx
                    if 0<=row<n and 0<=col<n and mat[row][col] == 1:
                        mat[row][col] = 0
                        q.append((row, col))
                        visited.add((row, col))
            ans.append(len(visited))
            visited.clear()
ans.sort()
print(len(ans))
print("\n".join(map(str, ans)))