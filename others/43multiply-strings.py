class Solution:
    def add(self, num1, num2):
        res = ''
        i, j = len(num1) - 1, len(num2) - 1
        # carry = 0 or 1
        carry = 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            carry, tmp = divmod(n1 + n2 + carry, 10)
            res = str(tmp) + res
            i -= 1
            j -= 1
        return str(carry) + res if carry else res

    # simulate by adding every product: O(mn+n^2) O(m+n)
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        ans = '0'
        N1, N2 = len(num1), len(num2)
        for j in range(N2 - 1, -1, -1):
            carry = 0
            # add all num1 * y, append (n-i-1) 0
            y = int(num2[j])
            # adding can also overflow, so should add as string
            # save as a list, because need to reverse
            cur = ['0'] * (N2 - j - 1)
            for i in range(N1 - 1, -1, -1):
                x = int(num1[i])
                product = x * y + carry
                carry, tmp = divmod(product, 10)
                cur.append(str(tmp))
            if carry > 0:
                cur.append(str(carry))
            cur = ''.join(cur[::-1])
            ans = self.add(ans, cur)
        return ans

    # a little math: O(mn), O(m+n)
    def multiply1(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        # the result will be m+n-1 or m+n length
        ansArr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                # directly save the product in array
                ansArr[i + j + 1] += x * int(num2[j])

        for i in range(m + n - 1, 0, -1):
            # check if > 10
            # if > 10, add the carry to previous one
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10

        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans


s = Solution()
print(s.multiply('1234', '567'))
