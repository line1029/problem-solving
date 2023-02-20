def solution(board, moves):
    n = len(board)
    board_turned = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            board_turned[j][n-1-i] = board[i][j]
    for row in board_turned:
        while row and row[-1] == 0:
            row.pop()
    stack = []
    cnt = 0
    for move in moves:
        if not board_turned[move-1]:
            continue
        cur = board_turned[move-1].pop()
        if stack and cur == stack[-1]:
            stack.pop()
            cnt += 2
        else:
            stack.append(cur)
    return cnt