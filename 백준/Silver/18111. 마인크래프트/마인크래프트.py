from sys import stdin
from collections import Counter
n, m, b = map(int, stdin.readline().split())
arr = stdin.readlines()
ground = []
for row in arr:
    ground += list(map(int, row.split()))
c = Counter(ground)
to_inventory = sum(k*v for k, v in c.items())
need_block = 0
need_cur_floor = c[0]
nm = n*m
min_time = 2*to_inventory
max_h = 0
for h in range(1, 257):
    need_block += need_cur_floor
    to_inventory -= nm - need_cur_floor
    need_cur_floor += c[h]
    if to_inventory + b < need_block:
        break
    if 2*to_inventory + need_block <= min_time:
        min_time = 2*to_inventory + need_block
        max_h = h
print(min_time, max_h)