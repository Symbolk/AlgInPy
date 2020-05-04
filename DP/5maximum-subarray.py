class Solution:
    # O(n), O(1)
    # if sum before < current num, just drop the sum before!
    # dp[i] = max(nums[i], dp[i-1]+nums[i])
    # res = max(dp[i])
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N == 1:
            return nums[0]
        res = nums[0]
        for i in range(1, N):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
            res = max(res, nums[i])
        return res

    # O(n), O(n)
    def maxSubArray1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N == 1:
            return nums[0]
        # dp[i]: subproblem: the max subarry sum in the array [0, i]
        dp = nums[:]
        for i in range(1, N):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        # get the max in the array (O(n))
        return max(dp)

    # only keep the latest presum
    # update max every time
    def maxSubArray2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N == 1:
            return nums[0]
        presum = res = nums[0]
        for i in range(1, N):
            # equivalent: if presum < 0, drop
            cur = max(nums[i], presum + nums[i])
            res = max(cur, res)
            presum = cur
        return res
