class Solution:
    # recursion
    def add(self, a: int, b: int) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a
        return add((a & b) << 1, a ^ b)

    # python -1 >> 1 == -1 infinite loop
    def add1(self, a: int, b: int) -> int:
        while b != 0:
            carry = (a & b) << 1
            a ^= b
            b = carry
        return a


s = Solution()
print(s.add(8, 5))
print(s.add(-1, 2))  # easy to infinite loop
print(s.add1(8, 5))
