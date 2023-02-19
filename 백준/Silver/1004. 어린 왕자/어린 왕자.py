from sys import stdin
for _ in range(int(stdin.readline())):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    cnt = 0
    for _ in range(int(stdin.readline())):
        cx, cy, r = map(int, stdin.readline().split())
        if any([(x1-cx)**2 + (y1-cy)**2 < r*r and (x2-cx)**2 + (y2-cy)**2 > r*r,
                (x1-cx)**2 + (y1-cy)**2 > r*r and (x2-cx)**2 + (y2-cy)**2 < r*r]):
            cnt += 1
    print(cnt)