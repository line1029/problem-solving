import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
arr = list(map(int, input().split()))
k = 2*n + 1
radii = [0]*k
right_edge = 0
center = 0
for i in range(k):
    if i <= right_edge:
        r = radii[(center << 1) - i]
        if i + r < right_edge:
            radii[i] = r
        elif i + r > right_edge:
            radii[i] = right_edge - i
        else:
            radii[i] = r
            tmp = right_edge + 1
            while not tmp & 1 or tmp < k and (i << 1) - tmp >= 0 and arr[((i << 1) - tmp) >> 1] == arr[tmp >> 1]:
                tmp += 1
                radii[i] += 1
            if tmp - 1 > right_edge:
                center = i
                right_edge = tmp - 1
    else:
        center = i
        tmp = i + 1
        while not tmp & 1 or tmp < k and (i << 1) - tmp >= 0 and arr[((i << 1) - tmp) >> 1] == arr[tmp >> 1]:
            tmp += 1
            radii[i] += 1
        right_edge = tmp - 1
m = int(input())
ans = __pypy__.builders.StringBuilder()
for s, e in map(lambda x: map(int, x.split()), (input() for _ in range(m))):
    if radii[s + e - 1] >= e - s + 1:
        ans.append("1\n")
    else:
        ans.append("0\n")
os.write(1, ans.build().encode())