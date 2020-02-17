class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        # filter()是一个高阶函数，其关键在于arg1的筛选函数。
        # filter()是一个惰性函数，需要套用list()来迫使其完成运算。
        # filter()将符合str.isalnum条件的s中的元素放入列表中。条件是str.isalnum 只有数字和字母
        # isalnum() 检测字符串是不是由字母和数字组成
        # s = [*filter(str.isalnum, s.lower())]
        s = list(filter(str.isalnum, s.lower()))
        return s[::-1] == s

    def isPalindrome2(self, s: str) -> bool:
        if not s:
            return True
        import re
        # str in python is immutable
        s = re.sub('[^a-z0-9]', '', s.lower())
        return s == s[::-1]


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome2("race a car"))
