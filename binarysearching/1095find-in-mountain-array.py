# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return self.size


class Solution:
    # binary search: O(logn), O(1)
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findPeakIndex(arr, l, r):
            while l < r:
                m = l + ((r - l) >> 1)
                if arr.get(m) < arr.get(m + 1):
                    # peak in the right
                    l = m + 1
                else:
                    r = m
            return l

        # ascending
        def findInLeft(arr, l, r, t):
            while l < r:
                m = l + ((r - l) >> 1)
                if arr.get(m) < t:
                    l = m + 1
                else:
                    r = m
            # instead of call get() in while, call once here
            # l == r
            return l if arr.get(l) == t else -1

        # descending
        def findInRight(arr, l, r, t):
            while l < r:
                m = l + ((r - l) >> 1)
                if arr.get(m) > t:
                    l = m + 1
                else:
                    r = m
            # instead of call get() in while, call once here
            # l == r
            return l if arr.get(l) == t else -1

        N = mountain_arr.length()
        # find peak index
        peak = findPeakIndex(mountain_arr, 0, N - 1)
        if mountain_arr.get(peak) == target:
            return peak

        # search in left: [0, peak-1]
        res = findInLeft(mountain_arr, 0, peak - 1, target)
        if res != -1:
            return res
        # search in right: [peak+1, N-1]
        res = findInRight(mountain_arr, peak + 1, N - 1, target)
        return res


arr = [0, 5, 3, 1]
mountain_array = MountainArray(arr)
target = 3
solution = Solution()
print(solution.findInMountainArray(target, mountain_array))
