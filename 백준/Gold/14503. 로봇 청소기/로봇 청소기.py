from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
room = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
direction = ((-1, 0), (0, 1), (1, 0), (0, -1))

def is_cleanable(i, j):
    for di, dj in direction:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and room[ni][nj] == 0:
            return True
    return False


def can_backward(i, j, d):
    ni, nj = i - direction[d][0], j - direction[d][1]
    if 0 <= ni < n and 0 <= nj < m and room[ni][nj] != 1:
        return True
    return False


def get_first_direction(i, j, d):
    for t in range(d - 1, d - 5, -1):
        di, dj = direction[t]
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and room[ni][nj] == 0:
            return t % 4


cnt = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    if is_cleanable(r, c):
        d = get_first_direction(r, c, d)
        di, dj = direction[d]
        r += di
        c += dj
    elif can_backward(r, c, d):
        di, dj = direction[d]
        r -= di
        c -= dj
    else:
        break

print(cnt)