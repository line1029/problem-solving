from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
arr = stdin.readlines()
got = set(arr[:n])
cnt = 0
for word in arr[n:]:
    cnt += (word in got)
print(cnt)