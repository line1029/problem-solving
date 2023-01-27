from sys import stdin
from collections import deque

n = int(stdin.readline())
k = int(stdin.readline())
arr = stdin.readlines()
apples = set(map(lambda x: tuple(map(lambda x: int(x)-1, x.split())), arr[:k]))
l = int(arr[k])
turns = list(map(lambda x: (int(x.split()[0]), x.split()[1]), arr[k+1:]))
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cur_direc = 0

snake = deque([(0, 0)])
snake_set = {(0, 0)}

cur_time = 0
turns_idx = 0
while True:
    cur_time += 1
    y, x = snake[0]
    dy, dx = direction[cur_direc]
    next_y, next_x = y+dy, x+dx
    if any([next_y<0, next_y>=n, next_x<0, next_x>=n, (next_y, next_x) in snake_set]):
        break
    snake.appendleft((next_y, next_x))
    snake_set.add((next_y, next_x))
    if (next_y, next_x) in apples:
        apples.discard((next_y, next_x))
    else:
        snake_set.discard(snake.pop())
    if turns_idx < len(turns) and cur_time == turns[turns_idx][0]:
        if turns[turns_idx][1] == "D":
            cur_direc = (cur_direc+1)%4
        else:
            cur_direc = (cur_direc-1)%4
        turns_idx += 1
print(cur_time)