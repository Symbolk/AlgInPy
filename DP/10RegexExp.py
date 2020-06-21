class Solution:
    # iteration
    @lru_cache(None)
    def isMatch(s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = (len(s) > 0) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        return first_match and self.isMatch(s[1:], p[1:])

    # dp: O(mn), O(mn)
    def isMatch1(s: str, p: str) -> bool:
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
    def isMatch2(s: str, p: str) -> bool:
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


s = Solution()
print(s.isMatch("abaaac", "a.a*c"))
print(s.isMatch("aa", "a*"))
