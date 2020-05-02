class Solution():
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 1, num
        while l <= r: # cannot be <
            m = (l + r) // 2  # math.floor()
            if m * m == num:
                return True
            elif m * m > num:
                r = m - 1
            else:
                l = m + 1 # should be +1
        return False
