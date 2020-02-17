from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        # m rows, n cols
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        for i in range(1, N):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]

        for j in range(1, M):
            if obstacleGrid[j][0] == 1:
                obstacleGrid[j][0] = 0
            else:
                obstacleGrid[j][0] = obstacleGrid[j - 1][0]

        for i in range(1, M):
            for j in range(1, N):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]


grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
sol = Solution()
print(sol.uniquePathsWithObstacles(grid))