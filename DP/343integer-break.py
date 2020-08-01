class Solution:
    # DP: O(n^2), O(n)
    def integerBreak(self, n: int) -> int:
        # dp[i]: the max product when split i into positive integers
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

        return dp[-1]
