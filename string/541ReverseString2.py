class Solution:
    # wrong
    def reverseStr1(self, s: str, k: int) -> str:
        s = list(s)
        N = len(s)

        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        # the relative 0 position
        for p in range(0, N, 2 * k):
            # offsets
            i = p
            j = min(p + k - 1, N - 1)
            reverse(i, j)
        return ''.join(s)

    # correct
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        N = len(a)
        for i in range(0, N, 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
            # a[i:i + k] = a[i:i + k][::-1]
        return ''.join(a)


sol = Solution()
s = "abcdefg"
print(sol.reverseStr1(s, 2))
print(sol.reverseStr(s, 2))
