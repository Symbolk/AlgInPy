class Solution:
    # O(max(m,n)), O(1)
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            # prepend
            res = str(tmp % 10) + res
            i -= 1
            j -= 1
        return '1' + res if carry else res

    # quicker
    def addStrings1(self, num1: str, num2: str) -> str:
        res = ''
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            carry, tmp = divmod(n1 + n2 + carry, 10)
            res = str(tmp) + res
            # early break
            if i < 0 and carry == 0:
                return num2[:j] + res
            if j < 0 and carry == 0:
                return num1[:i] + res
            i, j = i - 1, j - 1
        return '1' + res if carry else res


s = Solution()
print(s.addStrings("1234", "123"))
