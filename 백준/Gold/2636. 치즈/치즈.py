from sys import stdin
from collections import deque

def main():
    m, n = map(int, stdin.readline().split())
    grid = [0] * m * n
    D = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = [0] * m * n
    for i, row in enumerate(stdin.readlines()):
        grid[i * n : (i + 1) * n] = map(int, row.split())
    cur_cheese = sum(grid)
    if not cur_cheese:
        print(0, 0, sep="\n")
        exit()

    for cur_time in range(m * n):
        if not cur_cheese:
            break
        prev_cheese = cur_cheese
        q = deque([0])
        visited[0] = 1
        for _ in range(m * n):
            if not q:
                break
            for _ in range(len(q)):
                cur = q.popleft()
                i, j = cur // n, cur % n
                for di, dj in D:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < m and 0 <= nj < n and not visited[(nex := ni * n + nj)]:
                        visited[nex] = 1
                        if grid[nex]:
                            grid[nex] = 0
                            cur_cheese -= 1
                            continue
                        q.append(nex)
        visited = [0] * m * n
    print(cur_time, prev_cheese, sep="\n")


main()
