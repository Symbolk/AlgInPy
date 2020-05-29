class Solution:
    # stack: O(n), O(n)
    def decodeString(self, s: str) -> str:
        res = ''
        # (res before [, num before [)
        stack = []
        multi = 0
        for c in s:
            if c.isdigit():
                # if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            elif c == '[':
                stack.append((res, multi))
                res, multi = '', 0
            elif c == ']':
                last_res, cur_multi = stack.pop()
                res = last_res + cur_multi * res
            else:
                res += c
        return res

    # recursion: O(n), O(n)
    def decodeString1(self, s: str) -> str:
        def dfs(i):
            res, multi = '', 0
            while i < len(s):
                if s[i].isdigit():
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    # update i here, since substring has been precessed!
                    i, last_res = dfs(i + 1)
                    res += multi * last_res
                    multi = 0
                elif s[i] == ']':
                    # return single or double values
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(0)

sol = Solution()
# print(sol.decodeString("abc3[a2[c]]"))
print(sol.decodeString1("abc3[a2[c]]"))
