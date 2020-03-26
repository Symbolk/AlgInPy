from typing import List


class Solution:
    # simulation: O(n^2)
    def numRookCaptures(self, board: List[List[str]]) -> int:
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        res = 0
        si = sj = 0
        N = len(board)
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'R':
                    si, sj = i, j
        for dx, dy in move:
            step = 1
            while True:
                n_i, n_j = si + step * dx, sj + step * dy
                if n_i < 0 or n_i >= 8 or n_j < 0 or n_j >= 8 or board[n_i][n_j] == 'B':
                    break
                elif board[n_i][n_j] == 'p':
                    res += 1
                    break  # !eat p and stop in this direction
                step += 1
        return res

    # with py tricks
    def numRookCaptures1(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            if 'R' in board[i]:
                x = i
                y = board[i].index('R')
                break
        row = ''.join(board[x]).replace('.', '')
        col = ''.join(i[y] for i in board).replace('.', '')

        return row.count('Rp') + row.count('pR') + col.count('Rp') + col.count('pR')


sol = Solution()
print(sol.numRookCaptures1([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                            [".", ".", ".", "p", "p", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
                            [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
                            [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
