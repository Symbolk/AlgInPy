from typing import List
import collections


class Solution:
    # reverse problem: find the O linked with border O (unsurrounded by X)
    # DFS: search from border O: O(n*m), O(n*m)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        if not board[0]:
            return
        N, M = len(board), len(board[0])
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(i, j):
            if i < 0 or i >= N or j < 0 or j >= M:
                return
            if board[i][j] == 'O':
                board[i][j] = '#'
                for dx, dy in move:
                    dfs(i + dx, j + dy)

        for i in range(N):
            for j in range(M):
                if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                    if board[i][j] == 'O':
                        dfs(i, j)

        for i in range(N):
            for j in range(M):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    # BFS: O(n*m), O(n*m)
    def solve1(self, board: List[List[str]]) -> None:
        if not board:
            return
        if not board[0]:
            return
        N, M = len(board), len(board[0])
        move = [0, 1, 0, -1, 0]

        q = collections.deque()
        for i in range(N):
            for j in range(M):
                if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                    if board[i][j] == 'O':
                        q.append((i, j))

        while q:
            i, j = q.popleft()
            board[i][j] = '#'
            for x in range(4):
                ni, nj = i + move[x], j + move[x + 1]
                if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 'O':
                    q.append((ni, nj))

        for i in range(N):
            for j in range(M):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


s = Solution()
a = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
s.solve1(a)
print(a)
