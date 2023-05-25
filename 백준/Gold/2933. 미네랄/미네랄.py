from sys import stdin, stdout
from collections import deque
r, c = map(int, stdin.readline().split())
cave = []
for _ in range(r):
    cave.append(list(stdin.readline().strip()))
n = int(stdin.readline())
sticks = map(int, stdin.readline().split())
direc = ((1, 0), (0, 1), (-1, 0), (0, -1))
for idx, stick_height in enumerate(sticks):
    stick_height = r - stick_height
    if idx&1:
        for j in range(c-1, -1, -1):
            if cave[stick_height][j] == "x":
                break
        else:
            continue
        linked_direc = ((-1, 0), (0, -1), (1, 0))
    else:
        for j in range(c):
            if cave[stick_height][j] == "x":
                break
        else:
            continue
        linked_direc = ((-1, 0), (0, 1), (1, 0))
    cave[stick_height][j] = "."
    cluster = set()
    for di, dj in linked_direc:
        row, col = stick_height+di, j+dj
        if 0<=row<r and 0<=col<c and cave[row][col] == "x":
            if (row, col) in cluster:
                continue
            else:
                cluster.clear()
            queue = deque([(row, col)])
            cluster.add((row, col))
            flag = False
            while queue:
                if flag:
                    break
                ci, cj = queue.popleft()
                for di, dj in direc:
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<r and 0<=nj<c and cave[ni][nj] == "x":
                        if ni == r-1:
                            flag=True
                            break
                        if (ni, nj) not in cluster:
                            cluster.add((ni, nj))
                            queue.append((ni, nj))
            if not flag:
                need_fall = 101
                for cj in range(c):
                    row_fall = 101
                    cnt = 102
                    for ci in range(r):
                        if (ci, cj) in cluster:
                            cnt = 0
                            continue
                        if cave[ci][cj] == ".":
                            cnt += 1
                        elif cave[ci][cj] == "x":
                            row_fall = min(row_fall, cnt)
                            cnt = 102
                    row_fall = min(row_fall, cnt)
                    need_fall = min(need_fall, row_fall)
                for ci, cj in cluster:
                    cave[ci][cj] = "."
                for ci, cj in cluster:
                    cave[ci + need_fall][cj] = "x"
stdout.write("\n".join("".join(row) for row in cave))