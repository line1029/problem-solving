from sys import stdin
stdin.readline()
last = 0
cnt = 0
for num in map(int, stdin.read().splitlines()[::-1]):
    if num > last:
        cnt += 1
        last = num
print(cnt)