class Solution:
    # enumerate the center(s) of substring: O(n^2) (but quicker than dp), O(1)
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # expand to left and right
                left -= 1
                right += 1
            # note the -1: while break while, already exceed the valid substring
            return right - left - 1

        N = len(s)
        if N < 2:
            return s
        start = 0
        end = 0
        for i in range(N):
            # odd and even length
            length = max(expand(s, i, i), expand(s, i, i + 1))
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end + 1]

    # dp: O(n^2), O(n^2)
    def longestPalindrome1(self, s: str) -> str:
        N = len(s)
        res = ""
        dp = [[False] * N for _ in range(N)]

        i = N - 1
        while i >= 0:
            for j in range(i, N):
                # remove the equal head and tail (i+1, j-1)
                # border case: j-1-(i+1)-1<2, indicating that it is not an interval
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
                # if dp[i][j]:
                #   if j-i+1>len(res):
                if (dp[i][j] and j - i + 1) > len(res):
                    # no need to slice in the loop, since slicing takes O(k)
                    res = s[i:j + 1]
            i -= 1
        return res

    def longestPalindrome2(self, s: str) -> str:
        N = len(s)
        if N < 2:
            return s
        dp = [[False for _ in range(N)] for _ in range(N)]
        max_len = 1
        start = 0

        for i in range(N):
            dp[i][i] = True

        for j in range(1, N):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome2("babad"))

# for i in range(5, 0, -1):
#     print(i)
