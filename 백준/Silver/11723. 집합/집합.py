from sys import stdin, stdout
m = int(stdin.readline())
_set = 0
_all = 0b11111111111111111111
for _ in range(m):
    order = stdin.readline().split()
    if order[0] == "all":
        _set = _all
    elif order[0] == "empty":
        _set = 0
    else:
        num = int(order[1]) - 1
        if order[0] == "add":
            _set |= (1 << num)
        elif order[0] == "remove":
            _set &= ~(1 << num)
        elif order[0] == "check":
            print((_set & (1 << num)) >> num)
        else:
            _set ^= (1 << num)