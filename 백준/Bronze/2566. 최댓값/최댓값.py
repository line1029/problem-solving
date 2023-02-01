import sys
idx = None
maximum = -1
for i in range(9):
    row = map(int, sys.stdin.readline().split())
    for j, num in enumerate(row):
        if num > maximum:
            maximum = num
            idx = (i, j)

print(maximum)
print(f"{idx[0]+1} {idx[1]+1}")