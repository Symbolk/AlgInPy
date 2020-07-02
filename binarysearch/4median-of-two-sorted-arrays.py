from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M = len(nums1)
        N = len(nums2)

        mid = (M + N) // 2 + 1
        cnt = 0
        i, j = 0, 0
        t1, t2 = 0, 0
        while i < M or j < N:
            if nums1[i] <= nums2[j] and i < M:
                t1 = nums1[i]
                i += 1
            elif nums1[i] > nums2[j] and j < N:
                t2 = nums2[j]
                j += 1
            cnt += 1
            if cnt == mid:
                if (M + N) % 2 != 0:
                    return min(t1, t2)
                else:
                    return (t1 + t2) / 2

    # binary search: O(log min(m,n)), O(1)
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        # switch to make nums1 shorter
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            # OR recall
            # return self.findMedianSortedArrays1(nums2, nums1)
        M, N = len(nums1), len(nums2)

        # total num of nums in the left part
        # split nums1 at i, split nums2 at j
        total_left = (M + N + 1) // 2
        left, right = 0, M
        # search in nums1[0 : M+1] for nums1[i-1] <= nums2[j] && nums2[j-1] <= nums1[i]
        while left < right:
            i = (left + right) // 2
            j = total_left - i
            if nums1[i] < nums2[j - 1]:
                # should move i right
                left = i + 1
            else:
                right = i
        i, j = left, total_left - left

        # left max
        c1 = max(nums1[i - 1] if i > 0 else float("-inf"), nums2[j - 1] if j > 0 else float('-inf'))
        # right min
        c2 = min(nums1[i] if i < M else float('inf'), nums2[j] if j < N else float('inf'))
        if (M + N) % 2 == 1:
            # odd total length
            return c1
        else:
            return (c1 + c2) / 2


sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))
print(sol.findMedianSortedArrays([1, 2], [3, 4]))
