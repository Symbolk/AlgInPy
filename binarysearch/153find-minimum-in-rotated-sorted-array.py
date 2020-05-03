class Solution:
    # num at the rotate index is the min: O(logn), O(1)
    def findMin(self, nums: List[int]) -> int:
        def findRotateIndex(a):
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

        N = len(nums)
        if N == 1:
            return nums[0]
        return nums[findRotateIndex(nums)]

    def findMin1(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        l, r = 0, N - 1
        while l <= r:
            if nums[l] <= nums[r]:
                # ordered
                return nums[l]
            m = l + ((r - l) >> 1)
            # if N == 2, l == r, nums[l] == nums[r]
            if nums[l] <= nums[m]:
                # left is ordered, min in right
                l = m + 1
            else:
                r = m
        # never reach
        return nums[l]

# pay special attention to corner cases!
# includes: empty, one, two