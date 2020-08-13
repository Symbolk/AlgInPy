class Solution:
    # DP: O(m*n), O(m*n)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        pn, sn = len(p), len(s)
        # dp[i][j]: p[0:i] (0 to i-1) match with s[0:j]
        dp = [[False] * (sn + 1) for _ in range(pn + 1)]
        dp[0][0] = True
        # special case: p starts with several *
        # s == empty
        for i in range(1, pn + 1):
            if p[i - 1] != '*':
                break
            else:
                dp[i][0] = True

        for i in range(1, pn + 1):
            for j in range(1, sn + 1):
                if p[i - 1] == '*':
                    # dp[i - 1][j]: the current * did not match
                    # dp[i][j - 1]: the current * matched s[j-1]
                    dp[i][j] = dp[i - 1][j] | dp[i][j - 1]
                elif p[i - 1] == s[j - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[pn][sn]

    # Prefer to use s as row
    def isMatch1(self, s: str, p: str) -> bool:
        if not p:
            return not s

        sn, pn = len(s), len(p)
        # corner case: s is empty

        dp = [[False] * (pn + 1) for _ in range(sn + 1)]
        dp[0][0] = True
        for j in range(1, pn + 1):
            if p[j - 1] == '*':
                dp[0][j] = True
            else:
                break

        for i in range(1, sn + 1):
            for j in range(1, pn + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]


sol = Solution()
print(sol.isMatch("aa", "a"))
print(sol.isMatch("adceb", "*a*b"))
