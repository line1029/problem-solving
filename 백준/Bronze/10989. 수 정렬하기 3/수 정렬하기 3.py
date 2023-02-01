from sys import stdin, stdout
n = int(stdin.readline())
arr = [0]*10001
for i in range(n):
    num = int(stdin.readline())
    arr[num] += 1
for i in range(1, 10001):
    if arr[i]:
        for j in range(arr[i]):
            stdout.write(f'{i}\n')