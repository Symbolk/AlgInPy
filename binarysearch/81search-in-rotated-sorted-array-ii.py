class Solution:
    # O(n) worst case, O(1)
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] == target:
                return True
            if nums[0] == nums[mid]:
                # cannot determine which half is ordered
                l += 1
                continue
            if nums[l] < nums[mid]:
                # left is ascending
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # right is ascending
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

    # brutal force: O(n), O(n)
    def search1(self, nums: List[int], target: int) -> bool:
        nums = set(nums)
        return target in nums