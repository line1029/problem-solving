from sys import stdin
stdin.readline()
arr = list(map(int, stdin.readline().split()))
print(sum(arr) - max(arr))