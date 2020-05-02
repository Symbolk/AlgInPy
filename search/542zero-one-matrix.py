class Solution:
    # single-source BFS from non-zero points: O(mn), O(mn)
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import deque
        def bfs(i, j):
            q = deque()
            q.append((i, j, 0))
            while len(q) > 0:
                i, j, s = q.popleft()
                if matrix[i][j] == 0:
                    return s + 1
                for dx, dy in move:
                    _i, _j = i + dx, j + dy
                    if 0 <= _i < N and 0 <= _j < M:
                        if matrix[_i][_j] == 0:
                            return s + 1
                        else:
                            q.append((_i, _j, s + 1))

        N, M = len(matrix), len(matrix[0])
        # res = [[0] * M for _ in range(N)]
        move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(N):
            for j in range(M):
                if matrix[i][j] != 0:
                    # modify onspot can be done
                    matrix[i][j] = bfs(i, j)

        return matrix

    # multi-source (super source) BFS from 0s: O(mn), O(mn)
    def updateMatrix1(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import deque
        N, M = len(matrix), len(matrix[0])
        res = [[0] * M for _ in range(N)]

        zeros = [(i, j) for i in range(N) for j in range(M) if matrix[i][j] == 0]
        q = deque(zeros)
        move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # BFS on graph must record visited to void looping
        visited = set(zeros)

        while q:
            i, j = q.popleft()
            for dx, dy in move:
                _i, _j = i + dx, j + dy
                # xx not in instead of not xx in
                if 0 <= _i < N and 0 <= _j < M and (_i, _j) not in visited:
                    res[_i][_j] = res[i][j] + 1
                    q.append((_i, _j))
                    visited.add((_i, _j))
        return res

    # dp: for each res, how to get here? O(mn), O(1)
    def updateMatrix2(self, matrix: List[List[int]]) -> List[List[int]]:
        N, M = len(matrix), len(matrix[0])
        dp = [[N * M] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    dp[i][j] = 0

        # from left-up corner
        for i in range(N):
            for j in range(M):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

        # from right-bottom corner
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if i + 1 < N:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j + 1 < M:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)

        return dp
