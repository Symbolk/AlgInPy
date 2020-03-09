from typing import List


class Solution:
    # from end
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        last = N - 1
        for i in range(N - 2, -1, -1):
            if nums[i] >= (last - i):
                last = i
        if last == 0:
            return True
        else:
            return False

    # from start
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i, jump in enumerate(nums):
            if i > far:
                return False
            if far >= i and i + jump > far:
                far = i + jump
        return far >= i


sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))
print(sol.canJump([3, 2, 1, 0, 4]))
