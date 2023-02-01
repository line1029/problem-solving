from sys import stdin, stdout
n = int(stdin.readline())
arr = [tuple(map(int, i.split())) for i in stdin.read().split("\n")]
arr.pop()
arr.sort(key=lambda x: (x[1], x[0]))
for i in range(n):
    stdout.write(f"{arr[i][0]} {arr[i][1]}\n")