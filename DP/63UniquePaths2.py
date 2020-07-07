from typing import List


class Solution:
    # O(mn), O(mn)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]
        for i in range(0, rows):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            # no way to pass
            else:
                break
        for j in range(0, cols):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[rows - 1][cols - 1]

    # O(mn), O(1)
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # first row
        for i in range(1, cols):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]
        # first col
        for i in range(1, rows):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]


grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
grid2 = [[0]]
grid3 = [[0, 0], [1, 1], [0, 0]]

sol = Solution()
print(sol.uniquePathsWithObstacles(grid))
print(sol.uniquePathsWithObstacles(grid2))
print(sol.uniquePathsWithObstacles(grid3))
