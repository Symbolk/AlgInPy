class Solution:
    # (fake) inplace: O(n), O(1)
    def reverseWords(self, s: str) -> str:
        s = list(s)

        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        i = 0
        N = len(s)
        for j in range(N + 1):
            if j == N or s[j] == ' ':
                reverse(i, j - 1)
                i = j + 1
        reverse(0, N - 1)
        return ''.join(s)


sl = Solution()
s = 'the sky is blue'
print(sl.reverseWords(s))
print(s)
