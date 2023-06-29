from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
psum = [0]
for num in arr:
    psum.append(psum[-1] + num)
cur_max = psum[1]
cur_min = 0
ans = cur_max - cur_min
NINF = -1_000_000_000
for i in range(1, n + 1):
    if psum[i] > cur_max:
        cur_max = psum[i]
        ans = max(ans, cur_max - cur_min)
    if psum[i] < cur_min:
        cur_min = psum[i]
        cur_max = NINF
print(ans)