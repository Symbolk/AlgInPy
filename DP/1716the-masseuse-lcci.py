class Solution:
    # same with house-robber
    # naive dp: O(n), O(n)
    def massage(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        dp = [[0] * 2 for _ in range(N)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, N):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1][0], dp[-1][1])

    # O(n), O(n)
    def massage1(self, nums: List[int]) -> int:
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
        return dp[-1]

    # total space: 2N O(n), O(1)
    def massage2(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0

        dp0, dp1 = 0, nums[0]
        for i in range(1, N):
            tdp0 = max(dp0, dp1)
            tdp1 = dp0 + nums[i]
            dp0, dp1 = tdp0, tdp1
        return max(dp0, dp1)
