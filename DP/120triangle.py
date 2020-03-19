from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[m - 1])
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = triangle[m - 1][i]

        for i in range(m - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


sol = Solution()
print(sol.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
