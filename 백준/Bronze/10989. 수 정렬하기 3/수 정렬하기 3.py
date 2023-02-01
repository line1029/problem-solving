from sys import stdin, stdout
n = int(stdin.readline())
arr = [0]*10001
for _ in range(n):
    arr[int(stdin.readline())] += 1
for i in range(10001):
    for j in range(arr[i]):
        stdout.write(f'{i}\n')