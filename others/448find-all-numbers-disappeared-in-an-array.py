class Solution:
    # mark in place: O(n), O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N):
            j = abs(nums[i]) - 1
            if nums[j] > 0:
                nums[j] *= -1

        res = []
        for i in range(N):
            if nums[i] > 0:
                res.append(i + 1)
        return res
