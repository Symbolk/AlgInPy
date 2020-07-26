from typing import List
import collections


class Solution:
    # DFS with memo: O(mn), O(mn)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        N, M = len(matrix), len(matrix[0])
        memo = [[0] * M for _ in range(N)]
        move = [0, 1, 0, -1, 0]

        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            # if (i,j) is the min around, will return 1 directly
            ans = 1
            # find the increasing next position around
            for x in range(4):
                ni, nj = i + move[x], j + move[x + 1]
                if ni < 0 or nj < 0 or ni >= N or nj >= M:
                    continue
                if matrix[i][j] >= matrix[ni][nj]:
                    continue
                ans = max(ans, 1 + dfs(ni, nj))

            memo[i][j] = ans
            return ans

        res = 0
        for i in range(N):
            for j in range(M):
                res = max(res, dfs(i, j))

        return res

    # BFS/DP/Toposort: O(mn), O(mn)
    def longestIncreasingPath1(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        N, M = len(matrix), len(matrix[0])
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # in degrees of each node
        # in edge means decreasing direction (from big to small), since we want to get increasing path
        # using out degrees also works (quicker)
        inds = [[0] * M for _ in range(N)]
        q = collections.deque()
        for i in range(N):
            for j in range(M):
                for dx, dy in move:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] < matrix[i][j]:
                        inds[i][j] += 1
                if inds[i][j] == 0:
                    q.append((i, j))

        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                # start from the points where no smaller around
                i, j = q.popleft()
                for dx, dy in move:
                    ni, nj = i + dx, j + dy
                    # from (i,j) to (ni, nj) increase
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] > matrix[i][j]:
                        inds[ni][nj] -= 1
                        if inds[ni][nj] == 0:
                            q.append((ni, nj))
        return res

    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        N, M = len(matrix), len(matrix[0])
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # out degrees of each node
        # out edge means increasing direction
        outds = [[0] * M for _ in range(N)]
        q = collections.deque()
        for i in range(N):
            for j in range(M):
                for dx, dy in move:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] > matrix[i][j]:
                        outds[i][j] += 1
                if outds[i][j] == 0:
                    q.append((i, j))

        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in move:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] < matrix[i][j]:
                        outds[ni][nj] -= 1
                        if outds[ni][nj] == 0:
                            q.append((ni, nj))
        return res


s = Solution()
print(s.longestIncreasingPath1([
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]))
