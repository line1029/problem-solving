m, n = map(int, input().split())
board = []
for i in range(m):
    board.append(input())

cnt = 32
for i in range(m - 7):
    for j in range(n - 7):
        pattern = [board[row][j:j + 8] for row in range(i, i + 8)]
        # pattern = []
        # for row in range(8):
        #     pattern.append(board[i + row][j: j+ 8])
        tmp1 = 0
        tmp2 = 0
        for y in range(8):
            for x in range(8):
                if not (x + y) % 2:
                    if pattern[y][x] == "W":
                        tmp1 += 1
                    else:
                        tmp2 += 1
                else:
                    if pattern[y][x] == "B":
                        tmp1 += 1
                    else:
                        tmp2 += 1
        cnt = min(cnt, tmp1, tmp2)

print(cnt)