class Solution:
    # get the common prefix of binary m and n
    # O(logn), O(1)
    # logn is the digits of binary n
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m < n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift
    
    # Brian Kernighan: erase rightmost 1 in binary
    # O(logn), O(1)
    def rangeBitwiseAnd1(self, m: int, n: int) -> int:
        while m <n:
            n &= (n-1)
        return n