class Solution:
    # total space: 2N O(n), O(1)
    def massage(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0

        dp0, dp1 = 0, nums[0]
        for i in range(1, N):
            tdp0 = max(dp0, dp1)
            tdp1 = dp0 + nums[i]
            dp0, dp1 = tdp0, tdp1
        return max(dp0, dp1)
