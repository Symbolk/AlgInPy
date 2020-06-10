class Solution:
    # O(n), O(n)
    def isPalindrome(self, x: int) -> bool:
        rl = list(str(x))
        rl.reverse()
        return rl == list(str(x))

    # O(n), O(1)
    def isPalindrome1(self, x: int) -> bool:
        # reversed() return iterator
        return list(reversed(str(x))) == list(str(x))

    # O(logn), O(1)
    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev = 0
        # if x <= rev, rev has contains half
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        return x == rev or x == (rev // 10)


sol = Solution()
print(sol.isPalindrome1(12321))
print(sol.isPalindrome2(11))
