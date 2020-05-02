class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res, cur = 0, 0
        N = len(s)
        l = 0
        visited = set()
        for i in range(N):
            cur += 1
            # remove the left element util not repeat with current
            while s[i] in visited:
                visited.remove(s[l])
                l += 1
                cur -= 1
            res = cur if cur > res else res
            visited.add(s[i])
        return res

    # O(n), O(k) (k is the number of possible chars)
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if not s:
            return 0
        N = len(s)
        res = 0
        seen = set()
        r = -1
        for i in range(N):
            if i > 0:
                # remove the left one to slide
                seen.remove(s[i - 1])
            # expand while no repeat
            while r + 1 < N and s[r + 1] not in seen:
                seen.add(s[r + 1])
                r += 1
            res = (r - i + 1) if (r - i + 1) > res else res
        return res


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring1("abcabcbb"))
