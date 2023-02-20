def solution(board, moves):
    n = len(board)
    board_turned = [[] for _ in range(n)]
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if board[i][j] == 0:
                break
            board_turned[j].append(board[i][j])
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