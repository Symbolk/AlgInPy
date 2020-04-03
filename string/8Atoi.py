class Solution:
    # conversion: O(n), O(1)
    def myAtoi(self, str: str) -> int:
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        sign = -1 if ls[0] == '-' else 1

        if ls[0] in ['-', '+']:
            del ls[0]  # del语句作用在变量上，而不是数据对象上，引用计数器-1
        res, i = 0, 0

        while i < len(ls) and ls[i].isdigit():
            # ord("x") - ord("0"): compute the int value of x
            res = res * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))

    # FDA: O(n), O(1)
    def myAtoi1(self, str: str) -> int:
        fda = FDA()
        for c in str:
            fda.transform(c)
        return fda.sign * fda.ans

    # regex expression
    def myAtoi2(self, str: str) -> int:
        import re
        INT_MIN = - (1 << 31)
        INT_MAX = -INT_MIN - 1
        str = str.strip()
        num_re = re.compile(r'^[\+\-]?\d+')
        nums = num_re.findall(str)
        ans = int(*nums)
        return max(min(ans, INT_MAX), INT_MIN)


INT_MAX = 2 ** 31 - 1
# INT_MAX = 1 << 31
INT_MIN = -2 ** 31


class FDA:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        # transformation table: ' '	+/-	number	other
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_type(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def transform(self, c):
        self.state = self.table[self.state][self.get_type(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


solution = Solution()
print(solution.myAtoi("   -66899M"))
print(solution.myAtoi("-91283472332"))
print(solution.myAtoi1("   -66899M"))
print(solution.myAtoi2("2147483646"))
