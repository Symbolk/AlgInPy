class Solution:
    # O(n), O(n)
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        res = ''
        stack = []
        N = len(s)
        for i in range(N):
            if s[i] == ' ':
                res += ''.join(stack[::-1])
                res += ' '
                stack = []
            elif i == N - 1:
                stack.append(s[i])
                res += ''.join(stack[::-1])
            else:
                stack.append(s[i])

        return res

    def reverseWords1(self, s: str) -> str:
        res = ''
        N = len(s)
        i = 0
        while i < N:
            j = i
            while i < N and s[i] != ' ':
                i += 1
            res += ''.join(s[j:i][::-1])
            i += 1
            res += ' '
        return res[:-1]

    def reverseWords2(self, s: str) -> str:
        ss = s.split(' ')
        res = ''
        for c in ss:
            res += ''.join(c[::-1])
            res += ' '
        # drop the last
        return res[:-1]


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverseWords1("Let's take LeetCode contest"))
