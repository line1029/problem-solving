def solution(m, n, board):
    board_t = [[""]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            board_t[j][m-1-i] = board[i][j]
    
    def sliding_window(n, m, board):
        res = set()
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] != "#" and board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]:
                    res.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])
        return res
    
    def delete_blocks(n, m, board, del_set):
        for i, row in enumerate(board):
            tmp = []
            for j, char in enumerate(row):
                if (i, j) not in del_set:
                    tmp.append(char)
            tmp += ["#"]*(m - len(tmp))
            board[i] = tmp
    
    ans = 0
    while True:
        del_set = sliding_window(n, m, board_t)
        ans += len(del_set)
        if not del_set:
            break
        delete_blocks(n, m, board_t, del_set)
    return ans