from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.read().splitlines()))
if arr[0]*arr[2] == arr[1]*arr[1]:
    print(arr[-1]*(arr[1]//arr[0]))
else:
    print(2*arr[-1] - arr[-2])