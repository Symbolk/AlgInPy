class Solution:
    # O(n), O(n)
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2

    # find every bit of the target num: O(n), O(1)
    # WA
    def singleNumber0(self, nums: List[int]) -> int:
        counts = [0] * 32
        for n in nums:
            for j in range(32):
                counts[j] += n & 1
                n >>= 1

        res = 0
        for i in range(1, 32):
            res <<= 1
            res |= counts[31 - i] % 3
        return res if counts[31] % 3 == 0 else -res

    # x ^ 0 = x, x ^ 1 = ~x, x ^ x = 0
    # x & 0 = 0, x & 1 = x
    def singleNumber1(self, nums: List[int]) -> int:
        ones = twos = 0
        for n in nums:
            ones = ones ^ n & ~twos
            twos = twos ^ n & ~ones
        return ones

    def singleNumber2(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            # number of 1 on the current bit
            cnt = 0
            # mark the current bit
            bit = 1 << i
            for n in nums:
                if n & bit != 0:
                    cnt += 1
            # find one bit
            if cnt % 3 != 0:
                res |= bit
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res
