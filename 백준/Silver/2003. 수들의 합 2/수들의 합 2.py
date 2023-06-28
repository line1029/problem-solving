from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
psum = [0]
for num in arr:
    psum.append(psum[-1] + num)
i = 0
ans = 0
for j in range(1, n + 1):
    while psum[j] - psum[i] > m:
        i += 1
    if psum[j] - psum[i] == m:
        ans += 1
print(ans)