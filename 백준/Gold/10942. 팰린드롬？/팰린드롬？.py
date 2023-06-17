from sys import stdin, stdout
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
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
m = int(stdin.readline())
ans = []
for s, e in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    if radii[s + e - 1] >= e - s + 1:
        ans.append("1")
    else:
        ans.append("0")
stdout.write("\n".join(ans))