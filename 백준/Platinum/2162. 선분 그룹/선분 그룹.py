from sys import stdin
def is_crossing(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 == x2:
        if (x3 - x2)*(x4 - x2) < 0:
            return True
        elif (x3 - x2)*(x4 - x2) == 0:
            if x3 == x4:
                if max(y3, y4) >= min(y1, y2) and min(y3, y4) <= max(y1, y2):
                    return True
                return False
            else:
                return True
    elif y1 == y2:
        if (y3 - y2)*(y4 - y2) < 0:
            return True
        elif (y3 - y2)*(y4 - y2) == 0:
            if y3 == y4:
                if max(x3, x4) >= min(x1, x2) and min(x3, x4) <= max(x1, x2):
                    return True
                return False
            else:
                return True
    else:
        # (x2 - x1)*(y - y1) = (y2 - y1)*(x - x1)
        if ((x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1))*((x2 - x1)*(y4 - y1) - (y2 - y1)*(x4 - x1)) < 0:
            return True
        elif ((x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1))*((x2 - x1)*(y4 - y1) - (y2 - y1)*(x4 - x1)) == 0:
            if (y4 - y3)*(x2 - x1) == (y2 - y1)*(x4 - x3):
                if max(x3, x4) >= min(x1, x2) and min(x3, x4) <= max(x1, x2):
                    return True
                return False
            else:
                return True


def _find(x):
    if x != parent[x]:
        parent[x] = _find(parent[x])
    return parent[x]


def _union(x, y):
    x, y = _find(x), _find(y)
    if x == y:
        return
    if size[x] < size[y]:
        x, y = y, x
    size[x] += size[y]
    parent[y] = x


n = int(stdin.readline())
segments = list(map(lambda x: tuple(map(int, x.split())), stdin.read().splitlines()))
parent = {i:i for i in segments}
size = {i:1 for i in segments}
for i in segments:
    for j in segments:
        if i != j and is_crossing(*i, *j) and is_crossing(*j, *i):
            _union(i, j)
s = set(_find(x) for x in segments)
print(len(s))
print(max(size.values()))