from typing import List


class Solution:
    # from end: O(n), O(1)
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        last = N - 1
        for i in range(N - 2, -1, -1):
            if nums[i] >= (last - i):
                last = i
        return last == 0


    # from start: O(n), O(1)
    def canJump2(self, nums: List[int]) -> bool:
        rightmost = 0
        for i, jump in enumerate(nums):
            if i > rightmost:
                return False
            if i <= rightmost < i + jump:
                rightmost = i + jump
        # i also keeps the last position
        return rightmost >= nums[-1]


sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))
print(sol.canJump([3, 2, 1, 0, 4]))
