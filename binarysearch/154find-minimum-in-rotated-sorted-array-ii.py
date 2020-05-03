from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        l, r = 0, N - 1
        while l <= r:
            # nums[l] must < nums[r], since there are duplicates
            if nums[l] < nums[r] or l == r:
                return nums[l]
            m = l + ((r - l) >> 1)
            if nums[l] < nums[m]:
                l = m + 1
            elif nums[l] == nums[m]:
                # cannot determine which half is ordered
                l += 1
            else:
                r = m


sol = Solution()
print(sol.findMin([3, 1, 3]))
