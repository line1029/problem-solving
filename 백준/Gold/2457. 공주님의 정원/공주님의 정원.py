import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
mtod = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
flowers = []
for _ in range(n):
    date = list(map(int, input().split()))
    a, b = mtod[date[0]] + date[1], mtod[date[2]] + date[3]
    if b < 61 or a > 334: continue
    if a < 60: a = 60
    if b > 335: b = 335
    flowers.append([a, b])
flowers.sort(key=lambda x: (x[0], -x[1]))
if flowers[0][0] > 60 or max(i[1] for i in flowers) < 335:
    print(0)
    exit()
cur = nex = flowers[0][1]
cnt = 1
for s, e in flowers:
    if s <= cur:
        if e > nex:
            nex = e
    else:
        if s > nex:
            print(0)
            exit()
        cur = nex
        cnt += 1
        if e > nex:
            nex = e
if cur == 335:
    print(cnt)
else:
    print(cnt + 1)
    