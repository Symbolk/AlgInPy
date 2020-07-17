class Solution:
    # find the first nums[i] >= target
    # O(logn), O(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if not N:
            return 0
        if nums[N - 1] < target:
            return N
        l, r = 0, N - 1
        while l < r:
            m = l + ((r - l) >> 1)
            # m = (l + r) // 2  # if overflow, python automatically convert to long int
            if nums[m] < target:
                # in right part
                l = m + 1
            else:
                r = m
        return l
