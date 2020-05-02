from typing import List


class Solution:
    # brutal force: O(MN)
    # state: revive(2): 0 --> 1; die(-1): 1 --> 0
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        M, N = len(board), len(board[0])
        move = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]
        for i in range(M):
            for j in range(N):
                cnt1 = 0
                for dx, dy in move:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < M and 0 <= nj < N:
                        # note here: also check for -1
                        # & 1
                        if abs(board[ni][nj]) == 1:
                            cnt1 += 1
                if board[i][j] == 0:
                    if cnt1 == 3:
                        board[i][j] = 2
                elif board[i][j] == 1:
                    if cnt1 < 2:
                        board[i][j] = -1
                    elif cnt1 > 3:
                        board[i][j] = -1
                    elif cnt1 == 2 or cnt1 == 3:
                        continue

        for i in range(M):
            for j in range(N):
                if board[i][j] > 0:
                    board[i][j] = 1
                elif board[i][j]:
                    board[i][j] = 0

    # convolution
    def gameOfLife1(self, board: List[List[int]]) -> None:
        import numpy as np
        # 下面两行做zero padding
        board_exp = np.array([[0 for _ in range(c + 2)] for _ in range(r + 2)])
        board_exp[1:1 + r, 1:1 + c] = np.array(board)
        # 设置卷积核
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        # 开始卷积
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                # 统计细胞周围8个位置的状态
                temp_sum = np.sum(kernel * board_exp[i - 1:i + 2, j - 1:j + 2])
                # 按照题目规则进行判断
                if board_exp[i, j] == 1:
                    if temp_sum < 2 or temp_sum > 3:
                        board[i - 1][j - 1] = 0
                else:
                    if temp_sum == 3:
                        board[i - 1][j - 1] = 1


sol = Solution()
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
sol.gameOfLife(board)
print(board)
