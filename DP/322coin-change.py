from typing import List


class Solution:
    # dp: O(amount*n), O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    # faster than dp
    def coinChange1(self, coins: List[int], amount: int) -> int:
        def change(coins, amount, c_index, count, ans):
            if amount == 0:
                return min(ans, count)
            if c_index == len(coins):
                return ans
            k = amount // coins[c_index]
            while k >= 0 and k + count < ans:
                ans = change(coins, amount - k * coins[c_index], c_index + 1, count + k, ans)
                k -= 1
            return ans

        if amount == 0:
            return 0
        coins.sort(reverse=True)
        # float('inf') = +infinity
        ans = change(coins, amount, 0, 0, float('inf'))
        return ans if ans != float('inf') else -1
