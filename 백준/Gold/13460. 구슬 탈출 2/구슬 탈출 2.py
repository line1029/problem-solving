from sys import stdin
from collections import deque
def main():
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    n, m = map(int, stdin.readline().split())
    grid = stdin.read().splitlines()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "R":
                xr, yr = i, j
            elif grid[i][j] == "B":
                xb, yb = i, j
            elif grid[i][j] == "O":
                xo, yo = i, j
    q = deque([(xr, yr, xb, yb)])
    visited = [[[[0]*(m + 1) for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
    visited[xr][yr][xb][yb] = 1
    for cnt in range(10):
        for _ in range(len(q)):
            xr, yr, xb, yb = q.popleft()
            for dx, dy in D:
                f1 = f2 = False
                if dx:
                    nxr = xr + dx
                    while grid[nxr][yr] != "#":
                        if nxr == xo and yr == yo:
                            f1 = True
                        nxr += dx
                    nxr -= dx
                    nxb = xb + dx
                    while grid[nxb][yb] != "#":
                        if nxb == xo and yb == yo:
                            f2 = True
                        nxb += dx
                    nxb -= dx
                    if f1 and not f2:
                        print(cnt + 1)
                        exit()
                    if f2:
                        continue
                    if nxr == nxb and yr == yb:
                        if xr < xb:
                            if dx == 1:
                                nxr -= 1
                            else:
                                nxb += 1
                        else:
                            if dx == 1:
                                nxb -= 1
                            else:
                                nxr += 1
                    if not visited[nxr][yr][nxb][yb]:
                        visited[nxr][yr][nxb][yb] = 1
                        q.append((nxr, yr, nxb, yb))
                if dy:
                    nyr = yr + dy
                    while grid[xr][nyr] != "#":
                        if nyr == yo and xr == xo:
                            f1 = True
                        nyr += dy
                    nyr -= dy
                    nyb = yb + dy
                    while grid[xb][nyb] != "#":
                        if nyb == yo and xb == xo:
                            f2 = True
                        nyb += dy
                    nyb -= dy
                    if f1 and not f2:
                        print(cnt + 1)
                        exit()
                    if f2:
                        continue
                    if nyr == nyb and xr == xb:
                        if yr < yb:
                            if dy == 1:
                                nyr -= 1
                            else:
                                nyb += 1
                        else:
                            if dy == 1:
                                nyb -= 1
                            else:
                                nyr += 1
                    if not visited[xr][nyr][xb][nyb]:
                        visited[nxr][yr][nxb][yb] = 1
                        q.append((xr, nyr, xb, nyb))
    print(-1)

main()