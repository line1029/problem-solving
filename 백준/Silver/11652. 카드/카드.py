from sys import stdin
from collections import Counter
stdin.readline()
c = Counter(map(int, stdin.read().splitlines()))
d = c.most_common()
_min_num = d[0][0]
_max_cnt = d[0][1]
for v, cnt in d:
    if cnt < _max_cnt:
        break
    if _min_num > v:
        _min_num = v
    
print(_min_num)