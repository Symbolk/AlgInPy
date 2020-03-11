from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0

        dp_max = [0] * (N + 1)
        dp_min = [0] * (N + 1)

        import sys
        res = 0 - sys.maxsize
        dp_max[0] = 1
        dp_min[0] = 1
        for i in range(1, N + 1):
            if nums[i - 1] < 0:
                dp_max[i - 1], dp_min[i - 1] = dp_min[i - 1], dp_max[i - 1]
            dp_min[i] = min(nums[i - 1], dp_min[i - 1] * nums[i - 1])
            dp_max[i] = max(nums[i - 1], dp_max[i - 1] * nums[i - 1])
            res = max(res, dp_max[i])
        return res

    def maxProduct2(self, nums: List[int]) -> int:
        import sys
        res = 0 - sys.maxsize
        imax, imin = 1, 1
        for _, n in enumerate(nums):
            if n < 0:
                imax, imin = imin, imax
            imax = max(n, imax * n)
            imin = min(n, imin * n)
            res = max(res, imax)
        return res


sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))
print(sol.maxProduct2([2, 3, -2, 4]))
print(sol.maxProduct([-2, 0, -1]))
print(sol.maxProduct2([-2, 0, -1]))
