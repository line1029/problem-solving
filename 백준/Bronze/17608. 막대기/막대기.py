from sys import stdin
stdin.readline()
last = 0
cnt = 0
for num in map(int, reversed(stdin.read().splitlines())):
    if num > last:
        cnt += 1
        last = num
print(cnt)