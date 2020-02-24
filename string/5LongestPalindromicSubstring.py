class Solution:
    # 枚举中心
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        N = len(s)
        if not s or N < 1:
            return ""
        start = 0
        end = 0
        for i in range(N):
            # odd and even length
            length = max(expand(s, i, i), expand(s, i, i + 1))
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end + 1]

    # dp
    def longestPalindrome1(self, s: str) -> str:
        N = len(s)
        res = ""
        dp = [[False] * N for _ in range(N)]

        i = N - 1
        while i >= 0:
            for j in range(i, N):
                dp[i][j] = (s[i] == s[j]) and (j - i < 2 or dp[i + 1][j - 1])
                # if dp[i][j]:
                #   if j-i+1>len(res):
                if (dp[i][j] and j - i + 1) > len(res):
                    res = s[i:j + 1]
            i -= 1
        return res


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome1("babad"))

# for i in range(5, 0, -1):
#     print(i)
