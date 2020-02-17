from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return min(cost[0], cost[1])
        dp = [0] * (n + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n + 1):
            if i == n:
                dp[i] = min(dp[i - 1], dp[i - 2])
            # dp[i] 表示要爬当前楼梯时，当前最小的花费
            else:
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[n]

    # optimized
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        x = y = 0
        for i in cost[::-1]:
            x, y = i + min(x, y), x
        return min(x, y)


if __name__ == "__main__":
    solution = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(solution.minCostClimbingStairs(cost))
    print(solution.minCostClimbingStairs2(cost))
