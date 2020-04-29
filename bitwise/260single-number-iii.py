from typing import List

# 136, 137, 645
class Solution:
    # map: O(n), O(n)
    def singleNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        return [num for num in cnt if cnt[num] == 1]

    # bitwise: O(n), O(1)
    def singleNumbers1(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        # xor = nums1 ^ num2
        mask = 1
        num1 = num2 = 0
        # get lowbit 1
        # mask = xor & -xor
        # mask = xor & (~(xor - 1))
        while xor & mask == 0:
            mask <<= 1
        # divide the nums into 2 groups by odd/even of one arbitrary bit
        # each contains one single num, use ^ to find it!
        for n in nums:
            if n & mask == 0:
                num1 ^= n
            else:
                num2 ^= n
        return [num1, num2]


sol = Solution()
print(sol.singleNumbers1([4, 1, 4, 6]))
