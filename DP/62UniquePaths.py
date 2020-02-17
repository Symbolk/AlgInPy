import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))

    # O(m*n), O(m*n)
    def uniquePaths1(self, m: int, n: int) -> int:
        # m columns, n rows
        dp = [[1] * m] + [[1] + [0] * (m - 1) for _ in range(n - 1)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # O(m*n), O(n)
    def uniquePaths2(self, m: int, n: int) -> int:
        cur = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                cur[j] += cur[j - 1]
        return cur[-1]


sol = Solution()
print(sol.uniquePaths1(3, 2))
print(sol.uniquePaths2(3, 2))
print(sol.uniquePaths1(7, 3))
print(sol.uniquePaths2(7, 3))
