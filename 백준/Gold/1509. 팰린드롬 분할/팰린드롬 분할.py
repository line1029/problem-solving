from sys import stdin
# manacher
s = stdin.readline().strip()
n = len(s)
m = n*2 + 1
radii = [0]*m
center = 0
right_edge = 0
dp = list(range(n + 1))
for i in range(m):
    if i & 1:
        dp[(i >> 1) + 1] = min(dp[(i >> 1) + 1], dp[i >> 1] + 1)
    if i <= right_edge:
        r = radii[(center << 1) - i]
        if i + r < right_edge:
            radii[i] = r
        elif i + r > right_edge:
            radii[i] = right_edge - i
        else:
            radii[i] = r
            tmp = right_edge + 1
            while not tmp & 1 or tmp < m and 0 <= ((i << 1) - tmp) and s[tmp >> 1] == s[((i << 1) - tmp) >> 1]:
                tmp += 1
                radii[i] += 1
            if tmp - 1 > right_edge:
                center = i
                right_edge = tmp - 1
    else:
        center = i
        tmp = i + 1
        while not tmp & 1 or tmp < m and 0 <= ((i << 1) - tmp) and s[tmp >> 1] == s[((i << 1) - tmp) >> 1]:
            tmp += 1
            radii[i] += 1
        right_edge = tmp - 1
for i, r in enumerate(radii):
    for j in range(r % 2, r + 1, 2):
        dp[(i + j + 1) >> 1] = min(dp[(i + j + 1) >> 1], dp[(i - j) >> 1] + 1)
print(dp[-1])