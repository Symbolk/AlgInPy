class Solution:
    # O(n), O(n)
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        # dp[i][0]: i day with stock
        # dp[i][1]: i day without stock, freezing
        # dp[i][2]: i day without stock, not freezing
        dp = [[0] * 3 for _ in range(N)]
        dp[0][0] = -prices[0]
        # !start from 1
        for i in range(1, N):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        return max(dp[-1][1], dp[-1][2])

    # O(n), O(1)
    def maxProfit1(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, N):
            ff0 = max(f0, f2 - prices[i])
            ff1 = f0 + prices[i]
            ff2 = max(f1, f2)
            f0, f1, f2 = ff0, ff1, ff2
        return max(f1, f2)
