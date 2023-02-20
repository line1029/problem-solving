# two stack solution
from sys import stdin, stdout
stdin.readline()
raws = stdin.read().splitlines()
for s in raws:
    left, right = [], []
    for char in s:
        if char == "<":
            if left:
                right.append(left.pop())
        elif char == ">":
            if right:
                left.append(right.pop())
        elif char == "-":
            if left:
                left.pop()
        else:
            left.append(char)
    stdout.write("".join(left))
    stdout.write("".join(reversed(right)))
    stdout.write("\n")