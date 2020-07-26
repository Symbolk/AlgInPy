from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # n rows, m cols
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]  # return the last element

    # optimized
    def minPathSum2(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

    # more clear
    def minPathSum3(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        M, N = len(grid), len(grid[0])
        dp = [[0] * N for _ in range(M)]
        dp[0][0] = grid[0][0]
        for i in range(1, M):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, N):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, M):
            for j in range(1, N):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1]
    ]
    print(solution.minPathSum(grid))
    print(solution.minPathSum2(grid))
