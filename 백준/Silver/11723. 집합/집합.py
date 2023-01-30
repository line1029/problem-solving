from sys import stdin, stdout
m = int(stdin.readline())
_set = 0
for _ in range(m):
    order = stdin.readline().split()
    if order[0] == "all":
        _set = (1 << 20) - 1
    elif order[0] == "empty":
        _set = 0
    else:
        num = int(order[1]) - 1
        if order[0] == "add":
            _set |= (1 << num)
        elif order[0] == "remove":
            _set &= ~(1 << num)
        elif order[0] == "check":
            if _set & (1 << num):
                stdout.write("1\n")
            else:
                stdout.write("0\n")
        else:
            _set ^= (1 << num)