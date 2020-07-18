class Solution:
    # O(m+n), O(m+n)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        res = set()
        for i in nums2:
            if i in s:
                res.add(i)
        return res

    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def intersect(s1, s2):
            return [x for x in s1 if x in s2]

        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return intersect(set1, set2)
        else:
            return intersect(set2, set1)

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
