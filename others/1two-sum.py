from typing import List


class Solution:
    # hash to achieve O(1) in checking: O(n), O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            t = target - n
            if t in d:
                return [d[t], i]
            else:
                d[n] = i


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
