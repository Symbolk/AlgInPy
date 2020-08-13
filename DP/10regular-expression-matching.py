from functools import lru_cache


class Solution:
    # iteration
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        # empty only matches empty
        if not p:
            return not s
        first_match = (len(s) > 0) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        return first_match and self.isMatch(s[1:], p[1:])

    # memorized searching: O(mn), O(mn)
    def isMatch1(self, s: str, p: str) -> bool:
        memo = dict()

        def dp(i, j):
            # i in s and j in p
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)

            first = i < len(s) and p[j] in {s[i], '.'}

            if j <= len(p) - 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)

    # dfs with slicing
    def isMatch2(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(a, b):
            if (a, b) not in memo:
                if not b:  # if b is empty
                    return not a  # if a is empty too
                first = len(a) > 0 and b[0] in {a[0], '.'}
                if len(b) > 1 and b[1] == '*':
                    # match 0 or match many
                    res = dfs(a, b[2:]) or (first and dfs(a[1:], b))
                else:
                    res = first and dfs(a[1:], b[1:])
                memo[(a, b)] = res
            return memo[(a, b)]

        return dfs(s, p)

    # dp: O(mn), O(mn)
    def isMatch3(self, s: str, p: str) -> bool:
        if not p:
            return not s
        sn, pn = len(s), len(p)
        # whether first i match first j
        # 0...i-1, 0...j-1
        # dp[i][j] = isMatch(s[:i], p[:j])
        dp = [[False] * (pn + 1) for _ in range((sn + 1))]
        dp[0][0] = True

        # i == 0
        for j in range(1, pn + 1):
            # * will not appear at start
            # j - 1, j can appear 0..* times
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, sn + 1):
            for j in range(1, pn + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        # match 0/1/n times
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                    else:
                        # directly remove * (match 0 times)
                        dp[i][j] = dp[i][j - 2]

        return dp[-1][-1]


s = Solution()
print(s.isMatch3("abaaac", "a.a*c"))
print(s.isMatch3("aa", "a*"))
