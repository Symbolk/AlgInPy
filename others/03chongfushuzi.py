class Solution:
    """
    conditions:
        modify original?
        use extra space?
        time complexity?
    """
    # in-place hash: put nums[i] at i: O(n), O(1)
    def findRepeatNumber(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]