import functools


class Solution:
    # dfs: O(mn), O(mn)
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])

        @functools.lru_cache(None)
        def dfs(x, y):
            res = []
            for dx, dy in [(0, 1), (1, 0)]:
                if x + dx < M and y + dy < N:
                    res.append(dfs(x + dx, y + dy))
            return max(1, min(res) - dungeon[x][y]) if res else max(1, 1 - dungeon[x][y])

        return dfs(0, 0)

    # DP: O(mn), O(mn)
    def calculateMinimumHP1(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])
        dp = [[0] * N for _ in range(M)]
        # init
        # last is 1
        dp[M - 1][N - 1] = 1
        # last column, can only go/from down
        for i in range(M - 2, -1, -1):
            dp[i][N - 1] = max(dp[i + 1][N - 1] - dungeon[i + 1][N - 1], 1)
        # last row, can only go/from right
        for j in range(N - 2, -1, -1):
            dp[M - 1][j] = max(dp[M - 1][j + 1] - dungeon[M - 1][j + 1], 1)

        for i in range(M - 2, -1, -1):
            for j in range(N - 2, -1, -1):
                down = max(dp[i + 1][j] - dungeon[i + 1][j], 1)
                right = max(dp[i][j + 1] - dungeon[i][j + 1], 1)
                dp[i][j] = min(right, down)

        return max(dp[0][0] - dungeon[0][0], 1)

    def calculateMinimumHP2(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])
        dp = [[0] * N for _ in range(M)]
        # init
        # last is 1
        dp[M - 1][N - 1] = max(0, -dungeon[M - 1][N - 1])
        # last column, can only go/from down
        for i in range(M - 2, -1, -1):
            dp[i][N - 1] = max(dp[i + 1][N - 1] - dungeon[i][N - 1], 0)
        # last row, can only go/from right
        for j in range(N - 2, -1, -1):
            dp[M - 1][j] = max(dp[M - 1][j + 1] - dungeon[M - 1][j], 0)

        for i in range(M - 2, -1, -1):
            for j in range(N - 2, -1, -1):
                dp[i][j] = max(0, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])

        return dp[0][0] + 1

    def calculateMinimumHP3(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])
        INF = 10 ** 9
        dp = [[INF] * (N + 1) for _ in range(M + 1)]
        dp[M][N - 1] = dp[M - 1][N] = 1
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return dp[0][0]
