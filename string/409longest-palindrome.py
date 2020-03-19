class Solution:
    # slow
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for i in range(len(s)):
            if s[i] in counter.keys():
                counter[s[i]] += 1
            else:
                counter[s[i]] = 1
        res = 0
        for k, v in counter.items():
            res += (v // 2) * 2
        return res if res + 1 > len(s) else res + 1

    # slower
    def longestPalindrome2(self, s: str) -> int:
        import collections
        cnt = collections.Counter(s)
        res = 0
        for v in cnt.values():
            res += (v // 2) * 2
            if res % 2 == 0 and v % 2 == 1:
                res += 1
        return res

    def longestPalindrome3(self, s: str) -> int:
        # a - z:97 - 122, A - Z:65 - 90, 0 - 9:48 - 57
        cnt = [0 for _ in range(60)]
        res = 0
        # for c in s
        # for index, ch in enumerate(strs)
        # for ch in iter(strs):
        for ch in s:
            cnt[ord(ch) - ord('A')] += 1
        for i in range(60):
            res += (cnt[i] - cnt[i] % 2)
        return res + (res != len(s))


sol = Solution()
print(sol.longestPalindrome("abccccdd"))
print(sol.longestPalindrome2("abccccdd"))
print(sol.longestPalindrome3("abccccdd"))
print(sol.longestPalindrome("bb"))
print(sol.longestPalindrome3("bb"))
