from typing import List


class Solution:
    # res in [1, N + 1]
    # custom hash inplace: O(n), O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        N = len(nums)
        for i in range(N):
            # 1 <= nums[i] <= N: is (nums[i]-1) a valid index
            while 1 <= nums[i] <= N and nums[i] != nums[nums[i] - 1]:
                # incorrect: nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                # nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                swap(i, nums[i] - 1)
        for i in range(N):
            if i + 1 != nums[i]:
                return i + 1
        return N + 1

    # bitmap
    def firstMissingPositive1(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] <= 0:
                nums[i] = N + 1
        for i in range(N):
            t = abs(nums[i])
            if t <= N:
                nums[t - 1] = -abs(nums[t - 1])

        for i in range(N):
            if nums[i] > 0:
                return i + 1
        return N + 1


sol = Solution()
print(sol.firstMissingPositive([3, 4, -1, 1]))
