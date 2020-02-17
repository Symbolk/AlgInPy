class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = 0
        dp = [[0] * length for _ in range(length)]
        for j in range(length):
            i = j
            while i >= 0:
                if s[i] == s[j] and ((j - i < 2) or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    res += 1
                i -= 1

        return res


solution = Solution()
print(solution.countSubstrings("abc"))
print(solution.countSubstrings("aaa"))
print(solution.countSubstrings("fdsklf"))
