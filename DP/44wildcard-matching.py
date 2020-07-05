class Solution:
    # DP: O(m*n), O(m*n)
    def isMatch(self, s: str, p: str) -> bool:
        pn, sn = len(p), len(s)
        dp = [[False] * (sn + 1) for _ in range(pn + 1)]
        dp[0][0] = True
        for i in range(1, pn + 1):
            if p[i - 1] != '*':
                break
            else:
                dp[i][0] = True
        for i in range(1, pn + 1):
            for j in range(1, sn + 1):
                if p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] | dp[i][j - 1]
                elif p[i - 1] == s[j - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[pn][sn]


sol = Solution()
print(sol.isMatch("aa", "a"))
print(sol.isMatch("adceb", "*a*b"))
