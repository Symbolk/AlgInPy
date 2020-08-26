from typing import List


class Solution:
    # backtrack to find all answers
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2": "abc",
                 "3": "def",
                 "4": "ghi",
                 "5": "jkl",
                 "6": "mno",
                 "7": "pqrs",
                 "8": "tuv",
                 "9": "wxyz"}

        N = len(digits)
        res = []

        def backtrack(s, i):
            if i == N:
                res.append(s)
                return
            tmp = phone[digits[i]]
            for j in range(len(tmp)):
                # s+tmp[j] creates a new str (str is immutable)
                backtrack(s + tmp[j], i + 1)

        backtrack('', 0)
        return res

    def letterCombinations1(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2": "abc",
                 "3": "def",
                 "4": "ghi",
                 "5": "jkl",
                 "6": "mno",
                 "7": "pqrs",
                 "8": "tuv",
                 "9": "wxyz"}

        N = len(digits)
        res = []
        tmp = []

        def bt(i):
            if i == N:
                res.append(''.join(tmp))
                return
            chars = phone[digits[i]]
            for c in chars:
                tmp.append(c)
                bt(i + 1)
                tmp.pop()

        bt(0)
        return res


s = Solution()
print(s.letterCombinations("23"))
