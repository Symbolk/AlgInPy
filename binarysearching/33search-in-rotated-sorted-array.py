class Solution:
    # binary search: O(logn), O(1)
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] == target:
                return m
            if nums[0] <= nums[m]:
                # left is ordered
                if nums[0] <= target < nums[m]:
                    # search in the left half
                    r = m - 1
                else:
                    # search in the right half
                    l = m + 1
            else:
                # right is ordered
                if nums[m] < target <= nums[N - 1]:
                    # search in the right half
                    l = m + 1
                else:
                    # search in the left half
                    r = m - 1
        return -1
