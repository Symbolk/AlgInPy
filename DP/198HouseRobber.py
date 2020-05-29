from typing import List


class Solution:
    # O(n), O(n)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        # n rows, 2 cols
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = nums[i]
            else:  # i >= 1
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1][0], dp[-1][1])

    # O(n), O(n)
    def rob1(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]

    # O(n), O(n)
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[n]

    # O(n), O(1)
    def rob3(self, nums: List[int]) -> int:
        # i-2, i-1
        a, b = 0, 0
        for n in nums:
            c = max(b, a + n)
            a = b
            b = c
        return b


if __name__ == "__main__":
    solution = Solution()
    prices = [2, 7, 9, 3, 1]
    print(solution.rob(prices))
    print(solution.rob2(prices))
