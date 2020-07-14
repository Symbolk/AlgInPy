from typing import List


class Solution:
    # O(n^2), O(n)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # N rows, M cols in the last line
        N = len(triangle)
        M = len(triangle[N - 1])
        dp = [0 for _ in range(M)]
        for j in range(M):
            dp[j] = triangle[N - 1][j]

        for j in range(N - 2, -1, -1):
            for j in range(len(triangle[j])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]

    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = [0] * (N + 1)
        for i in range(N - 1, -1, -1):
            for j in range(i + 1):  # len(triangle) = i+1
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


sol = Solution()
print(sol.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
