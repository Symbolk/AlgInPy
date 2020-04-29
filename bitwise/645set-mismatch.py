from typing import List


class Solution:
    # O(n), O(1)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        miss = 1
        for n in nums:
            # if already seen, duplicate
            if nums[abs(n) - 1] < 0:
                dup = abs(n)
            else:
                # negative to mark seen
                nums[abs(n) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                miss = i + 1

        return [dup, miss]

    # O(n), O(1)
    def findErrorNums1(self, nums: List[int]) -> List[int]:
        def singleNumbers(nums):
            xor = 0
            for n in nums:
                xor ^= n
            mask = xor & (-xor)
            a, b = 0, 0
            for n in nums:
                if n & mask == 0:
                    a ^= n
                else:
                    b ^= n
            return [a, b]

        nums = [0] + nums
        # use index to convert the problem to 260!
        idx = []
        for i in range(len(nums)):
            idx.append(i)
        a, b = singleNumbers(idx + nums)
        # determine dup and miss
        for n in nums:
            if n == a:
                return [a, b]
        return [b, a]

    def findErrorNums2(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        # nums should contain all nums in [1, len(nums)]
        for i in range(1, len(nums) + 1):
            xor ^= i

        # there are 2 nums only appear once
        # converted to 260
        right_most_bit = xor & (-xor)
        a = b = 0
        for n in nums:
            if n & right_most_bit == 0:
                a ^= n
            else:
                b ^= n
        for i in range(1, len(nums) + 1):
            if i & right_most_bit == 0:
                a ^= i
            else:
                b ^= i

        for n in nums:
            if n == a:
                return [a, b]
        return [b, a]


sol = Solution()
print(sol.findErrorNums([4, 2, 2, 1]))
