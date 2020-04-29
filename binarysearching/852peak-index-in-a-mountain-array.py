class Solution:
    # binary search to shorten the range: O(logn), O(1)
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        N = len(A)
        l, r = 0, N - 1
        while l < r:
            m = l + ((r - l) >> 1)
            # at least two nums in the range
            # m + 1 <= N - 1, so no need to check
            if A[m] < A[m + 1]:
                l = m + 1
            else:
                r = m
        return l
