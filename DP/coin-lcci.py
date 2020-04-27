class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [1, 5, 10, 25]
        dp = [0] * (n + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, n + 1):
                dp[i] = (dp[i] + dp[i - c])

        return dp[n] % 1000000007
