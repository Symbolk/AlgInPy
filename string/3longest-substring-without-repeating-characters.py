class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        N = len(s)
        l, max, cur = 0, 0, 0
        memo = set()
        for i in range(N):
            cur += 1
            while s[i] in memo:
                memo.remove(s[l])
                l += 1
                cur -= 1
            max = cur if cur > max else max
            memo.add(s[i])
        return max


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
