class Solution:
    # slow version
    def validPalindrome2(self, s: str) -> bool:
        if not s:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(s, i, j - 1) or self.isPalindrome(s, i + 1, j)
            i += 1
            j -= 1
        return True

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        length = len(s)
        i, j = 0, length - 1
        while i < j:
            if s[i] != s[j]:
                a = s[i + 1:j + 1]  # [i+1, j+1)
                b = s[i:j]  # [i, j)
                # return a[::-1] == a or b[::-1] == b
                return a == ''.join(reversed(a)) or b == ''.join(reversed(b))
            i += 1
            j -= 1
        return True


solution = Solution()
print(solution.validPalindrome("abfddcba"))
print(solution.validPalindrome2("abfddcba"))
print(solution.validPalindrome("abdcba"))
print(solution.validPalindrome2("abdcba"))
print(solution.validPalindrome2("deeee"))
