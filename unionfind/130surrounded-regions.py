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

    # disjoint set
    def solve2(self, board: List[List[str]]) -> None:
        if not board:
            return
        if not board[0]:
            return
        N, M = len(board), len(board[0])

        p = {}

        def find(x):
            p.setdefault(x, x)
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def find1(x):
            p.setdefault(x, x)
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return p[x]

        def union(x, y):
            p[find(x)] = find(y)

        def isConnected(x, y):
            return find(x) == find(y)

        dummy = N * M
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'O':
                    if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                        # linked border O with dummy
                        union(i * M + j, dummy)
                    else:
                        # link other O with each other
                        for dx, dy in move:
                            if board[i + dx][j + dy] == 'O':
                                union(i * M + j, (i + dx) * M + (j + dy))
        for i in range(N):
            for j in range(M):
                if isConnected(i * M + j, dummy):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


s = Solution()
a = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
b = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
s.solve1(a)
s.solve2(b)
print(b)
