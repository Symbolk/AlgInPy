class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r = 1, x
        while l < r:
            m = (l + r + 1) >> 1
            if m * m > x:
                r = m - 1
            else:
                l = m
        return l

    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return int(r)
