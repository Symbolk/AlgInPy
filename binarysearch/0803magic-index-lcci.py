class Solution:
    # O(n), O(1)
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i == n:
                return i
        return -1

    def findMagicIndex1(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == nums[i]:
                return i
            if nums[i] > i + 1:
                i = nums[i] - 1
            else:
                i += 1
        return -1

    # binary pruning: O(logn), O(n)
    def findMagicIndex2(self, nums: List[int]) -> int:
        def fun(l, r):
            if l > r:
                return -1
            m = (l + r) // 2
            left = fun(l, m - 1)
            if left != -1:
                return left
            elif nums[m] == m:
                return m
            else:
                return fun(m + 1, r)

        return fun(0, len(nums) - 1)
