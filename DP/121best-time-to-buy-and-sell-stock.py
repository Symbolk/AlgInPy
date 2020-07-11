from typing import List


class Solution:
    # O(n), O(1)
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for p in prices:
            minprice = min(minprice, p)
            maxprofit = max(maxprofit, p - minprice)
        return maxprofit

    # O(n), O(n)
    def maxProfit1(self, prices: List[int]) -> int:
        N = len(prices)
        if N < 2:
            return 0
        # dp[i][0] = max profit without holding stock util ith day
        # day rows, 2 cols
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = 0 - prices[0]
        for i in range(1, N):
            # transformation: 0-0, 1-0, 1-1
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])
        return max(dp[-1][0], dp[-1][1])


if __name__ == "__main__":
    solution = Solution()
    prices = [7, 6, 4, 3, 1]
    print(solution.maxProfit(prices))
