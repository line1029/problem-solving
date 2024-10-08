class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        D = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
        for i in range(m):
            for j in range(n):
                live_neis = 0
                for di, dj in D:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in [-1, 1, 3]:
                        live_neis += 1
                if board[i][j] and live_neis not in [2, 3] or not board[i][j] and live_neis == 3:
                    board[i][j] += 2
                else:
                    board[i][j] -= 2
        for i in range(m):
            for j in range(n):
                if board[i][j] < 0:
                    board[i][j] += 2
                else:
                    board[i][j] = ((board[i][j] - 1) & 1)
