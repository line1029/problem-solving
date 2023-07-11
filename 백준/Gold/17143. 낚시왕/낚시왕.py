from sys import stdin
r, c, m = map(int, stdin.readline().split())
grid = [[0]*c for _ in range(r)]
shark = dict()
speed = [0]*10001
direc = [0]*10001
D = [0, 0, 2, 3, 1]
for i, j, s, d, z in sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()), key=lambda x: x[-1]):
    grid[i - 1][j - 1] = z
    direc[z] = D[d]
    speed[z] = s%(2*c - 2) if direc[z]&1 else s%(2*r - 2)
    shark[z] = [i - 1, j - 1]
ans = 0
for j in range(c):
    for i in range(r):
        if grid[i][j]:
            ans += grid[i][j]
            del shark[grid[i][j]]
            grid[i][j] = 0
            break
    
    dels = []
    nex = [[0]*c for _ in range(r)]
    for z, (i, j) in shark.items():
        if direc[z] == 1:
            if j + c - 1 < speed[z]:
                j += (c << 1) - 2 - speed[z]
            elif j < speed[z]:
                j = speed[z] - j
                direc[z] = 3
            else:
                j -= speed[z]
        elif direc[z] == 3:
            if (c << 1) - 2 - j < speed[z]:
                j += speed[z] - (c << 1) + 2
            elif c - 1 - j < speed[z]:
                j = (c << 1) - 2 - speed[z] - j
                direc[z] = 1
            else:
                j += speed[z]
        elif direc[z] == 0:
            if i + r - 1 < speed[z]:
                i += (r << 1) - 2 - speed[z]
            elif i < speed[z]:
                i = speed[z] - i
                direc[z] = 2
            else:
                i -= speed[z]
        else:
            if (r << 1) - 2 - i < speed[z]:
                i += speed[z] - (r << 1) + 2
            elif r - 1 - i < speed[z]:
                i = (r << 1) - 2 - speed[z] - i
                direc[z] = 0
            else:
                i += speed[z]
        if nex[i][j] < z:
            if nex[i][j]:
                dels.append(nex[i][j])
            nex[i][j] = z
        shark[z] = [i, j]
    for z in dels:
        del shark[z]
    grid = nex

print(ans)