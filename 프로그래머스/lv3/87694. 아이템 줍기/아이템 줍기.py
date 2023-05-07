def solution(rectangle, characterX, characterY, itemX, itemY):
    from collections import deque
    grid = [[0]*102 for _ in range(102)]
    for rec in rectangle:
        for x in range(rec[0]*2, rec[2]*2 + 1):
            for y in range(rec[1]*2, rec[3]*2 + 1):
                grid[y][x] = 1
    
    direc = ((0, 1), (1, 0), (0, -1), (-1, 0))
    inside = []
    for i in range(1, 101):
        for j in range(1, 101):
            for di, dj in direc + ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                ni, nj = i + di, j + dj
                if not grid[ni][nj]:
                    break
            else:
                inside.append((i, j))
    for i, j in inside:
        grid[i][j] = 0
    
    q = deque([(characterX*2, characterY*2)])
    grid[characterY*2][characterX*2] = 0
    while q:
        curX, curY = q.popleft()
        for dy, dx in direc:
            nexX, nexY = curX + dx, curY + dy
            if grid[nexY][nexX] == 1:
                grid[nexY][nexX] += grid[curY][curX]
                if nexX == itemX*2 and nexY == itemY*2:
                    return grid[nexY][nexX] //2
                q.append((nexX, nexY))
        