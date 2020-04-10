class Solution:
    # O(n), O(n)
    def reverseWords(self, s: str) -> str:
        # split() does strip() too
        return ' '.join(s.split()[::-1])

        # return ' '.join(re.findall('[^ ]+', s)[::-1])

        # list comprehension
        # return ' '.join([i for i in s.split() if i][::-1])

        # return ' '.join([i for i in s.split()][::-1]).strip()

        # return ' '.join(reversed(s.split()))

        # strs = s.split()
        # strs.reverse()
        # return ' '.join(strs)

        # return ' '.join(reversed(s.strip().split()))

    # double pointers: l & r with deque
    def reverseWords1(self, s: str) -> str:
        from collections import deque
        l, r = 0, len(s) - 1
        # ! note here
        while l <= r and s[l] == ' ':
            l += 1
        while l <= r and s[r] == ' ':
            r -= 1

        d = deque()
        word = []
        while l <= r:
            if s[l] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[l] != ' ':
                word.append(s[l])
            l += 1
        d.appendleft(''.join(word))

        return ' '.join(d)

    # double pointers from end (smart!)
    def reverseWords2(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            # stop util the first space
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1:j + 1])
            # jump the spaces
            while s[i] == ' ':
                i -= 1
            # j is the end of the next word
            j = i
        return ' '.join(res)

    # with a stack
    def reverseWords3(self, s: str) -> str:
        # str is immutable
        s = s.strip()
        stack = []
        res = ''
        for i in range(len(s), 0, -1):
            if s[i - 1] == ' ':
                if not stack:
                    continue
                while stack:
                    res += stack.pop()
                res += ' '
            else:
                stack.append(s[i - 1])
        while stack:
            res += stack.pop()
        return res


sol = Solution()
print(sol.reverseWords("  hello world!  "))
