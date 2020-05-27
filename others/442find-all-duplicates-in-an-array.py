from typing import List


class Solution:
    # mark inplace: O(n), O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        for i in range(N):
            j = abs(nums[i]) - 1
            if nums[j] < 0:
                # already < 0, means appear
                res.append(j + 1)
            else:
                nums[j] *= -1

        return res

    def findDuplicates1(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            # swap to the proper position
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i, v in enumerate(nums, 1):  # enumerate(sequence, [start=0]): index start from [start]
            if i != v:
                res.append(v)
        return res


sol = Solution()
print(sol.findDuplicates1([4, 3, 2, 7, 8, 2, 3, 1]))
