from typing import List
import collections


class Solution:
    # sort and scan with double pointers: O(n1logn1 + n2logn2), O(1)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        N1, N2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < N1 and index2 < N2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1

        return intersection

    # O(m+n), O(min(m,n))
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        cnt = collections.Counter(nums1)
        res = list()
        for n in nums2:
            # assignment expression (> py 3.8)
            if cnt.get(n, 0) > 0:
                res.append(n)
                cnt[n] -= 1
                # if cnt[n] == 0:
                #     cnt.pop(n)
        return res

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = collections.Counter(nums1)
        cnt2 = collections.Counter(nums2)

        return list((cnt1 & cnt2).elements())


sol = Solution()
print(sol.intersect2([1, 2, 2, 1], [2, 2]))
