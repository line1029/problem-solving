from sys import stdin
n = int(stdin.readline())
arr = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
s = 0
for i in range(n):
    s += (arr[i][0] + arr[i - 1][0])*(arr[i][1] - arr[i - 1][1])
s = abs(s)
print(f"{s/2:.1f}")