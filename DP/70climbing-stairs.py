class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1] # dp[n]

    # O(n), O(1)
    def climbStairs1(self, n: int) -> int:
        if n <= 2:
            return n
        a = 1
        b = 2
        for i in range(2, n):
            b, a = a + b, b
        return b
