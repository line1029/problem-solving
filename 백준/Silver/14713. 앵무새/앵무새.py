from sys import stdin
from collections import deque
input = stdin.readline
n = int(input())
arr = stdin.read().splitlines()
l = arr.pop().split()
arr = list(map(lambda x: deque(x.split()), arr))
for word in l:
    for d in arr:
        if d and d[0] == word:
            d.popleft()
            break
    else:
        print("Impossible")
        exit()
if any(arr):
    print("Impossible")
else:
    print("Possible")