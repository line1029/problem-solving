from sys import stdin
n = int(stdin.readline())
room = stdin.read().splitlines()
x = 0
length = 0
for i in range(n):
    for j in range(n):
        if room[i][j] == "X":
            if length >= 2:
                x += 1
            length = 0
            continue
        length += 1
    if length >= 2:
        x += 1
    length = 0
y = 0
for i in range(n):
    for j in range(n):
        if room[j][i] == "X":
            if length >= 2:
                y += 1
            length = 0
            continue
        length += 1
    if length >= 2:
        y += 1
    length = 0
print(x, y)