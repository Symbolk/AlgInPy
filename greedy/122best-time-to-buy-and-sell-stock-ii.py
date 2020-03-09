from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N <= 1:
            return 0
        res = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                res += tmp
        return res
