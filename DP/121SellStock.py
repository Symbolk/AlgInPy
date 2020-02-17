from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        # dp[i][0] = max profit without holding stock util ith day
        # day rows, 2 cols
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = 0 - prices[i]
                continue
            # transformation: 0-0, 1-0, 1-1
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])
        return max(dp[-1][0], dp[-1][1])


if __name__ == "__main__":
    solution = Solution()
    prices = [7, 6, 4, 3, 1]
    print(solution.maxProfit(prices))
