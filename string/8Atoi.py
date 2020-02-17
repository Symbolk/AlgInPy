class Solution:
    def myAtoi(self, str: str) -> int:
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        sign = -1 if ls[0] == '-' else 1

        if ls[0] in ['-', '+']:
            del ls[0]  # del语句作用在变量上，而不是数据对象上，引用计数器-1
        res, i = 0, 0

        while i < len(ls) and ls[i].isdigit():
            # ord("x") - ord("0"): compute the value of x
            res = res * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))


if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("   -66899M"))
