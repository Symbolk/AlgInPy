from typing import List


class Solution:
    # O(n), O(n)
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        # n rows, 2 cols
        dp = [[0] * 2 for _ in range(N)]
        for i in range(N):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = nums[i]
            else:  # i >= 1
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1][0], dp[-1][1])

    # O(n), O(n)
    def rob2(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, N + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[N]

    # O(n), O(1)
    def rob3(self, nums: List[int]) -> int:
        # i-1, i-2
        cur, pre = 0, 0
        for n in nums:
            cur, pre = max(pre + n, cur), cur
        return cur


if __name__ == "__main__":
    solution = Solution()
    prices = [2, 7, 9, 3, 1]
    print(solution.rob(prices))
    print(solution.rob2(prices))
