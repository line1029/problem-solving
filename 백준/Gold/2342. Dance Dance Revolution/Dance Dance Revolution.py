from sys import stdin
arr = list(map(int, stdin.readline().split()))
arr.pop()
n = len(arr)
INF = 400001
# 01 02 03 04 12 13 14 23 24 34
#  0  1  2  3  4  5  6  7  8  9
idxs = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
d = [[0, 1, 2, 3], [0, 4, 5, 6], [1, 4, 7, 8], [2, 5, 7, 9], [3, 6, 8, 9]]
dp = [[INF]*n for _ in range(10)]
dp[arr[0] - 1][0] = 2
def get_idx(j, num):
    for i in idxs[j]:
        if i != num:
            return i
def get_diff(j, k):
    if j == k:
        return 1
    tmp = 0
    for i in idxs[j]:
        tmp ^= 1 << i
    for i in idxs[k]:
        tmp ^= 1 << i
    if tmp & 1:
        return 2
    if tmp == 10 or tmp == 20:
        return 4
    return 3
def get_min(i, num):
    for j in d[num]:
        for k in d[get_idx(j, num)]:
            dp[j][i] = min(
                dp[j][i],
                dp[k][i - 1] + get_diff(j, k)
            )


for i in range(1, n):
    get_min(i, arr[i])

print(min(dp[i][-1] for i in range(10)))