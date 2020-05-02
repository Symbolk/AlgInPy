from typing import List


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

    # find the index where ascending arr was rotated
    def findRotateIndex(self, a):
        N = len(a)
        # not rotated
        if a[0] < a[N - 1]:
            return 0
        l, r = 0, N - 1
        m = 0
        while l <= r:
            m = l + ((r - l) >> 1)
            if a[m] > a[m + 1]:
                # find
                return m + 1
            else:
                if a[m] < a[l]:
                    # within [l, m)
                    r = m - 1
                else:
                    # within [m, r]
                    l = m + 1
        return m

    # template for range binary search
    def binarySearch(self, nums, l, r, target):
        while l < r:
            m = l + ((r - l) >> 1)
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1

    def search1(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        N = len(nums)
        if N == 1:
            return 0 if nums[0] == target else -1
        # find rotate index
        index = self.findRotateIndex(nums)
        if index == 0:
            # not rotated
            l, r = 0, N - 1
        else:
            if target >= nums[0]:
                # search in the left
                l, r = 0, index
            else:
                # search in the right
                l, r = index, N - 1

        return self.binarySearch(nums, l, r, target)


sol = Solution()
print(sol.findRotateIndex([4, 5, 6, 7, 0, 1, 2]))
print(sol.binarySearch([1, 2, 3, 4], 0, 3, 3))
print(sol.search1([4, 5, 6, 7, 0, 1, 2], 5))
