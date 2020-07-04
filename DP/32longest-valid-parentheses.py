class Solution:
    # brutal force: O(n^3), O(n)
    def longestValidParentheses0(self, s: str) -> int:
        def isValid(x):
            stack = []
            for i in range(len(x)):
                if x[i] == '(':
                    stack.append('(')
                elif x[i] == ')' and len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return len(stack) == 0

        N = len(s)
        if N < 2:
            return 0
        # ans must be even, so backward with step 2
        # enumerate the length of substring i
        for i in range(N if N % 2 == 0 else N - 1, 0, -2):
            for j in range(N - i + 1):
                if isValid(s[j:j + i]):
                    return i
        return 0

    # dp: O(n), O(n)
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        N = len(s)
        dp = [0] * N
        for i in range(N):
            #  i - dp[i - 1] - 1 is the pos of matched '(' of ')'
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]
        return max(dp)

    # stack: O(n), O(n)
    def longestValidParentheses1(self, s: str) -> int:
        if not s:
            return 0
        N = len(s)
        stack = [-1]
        ans = 0
        for i in range(N):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    ans = max(ans, length)

        return ans

    # forward and backward scanning: O(n), O(1)
    def longestValidParentheses2(self, s: str) -> int:
        N = len(s)
        if N < 2:
            return 0
        # the number of '(' and ')'
        l, r = 0, 0
        ans = 0
        for i in range(N):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, 2 * r)
            elif r > l:
                l = r = 0
        l = r = 0
        for i in range(N - 1, -1, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, 2 * l)
            elif l > r:
                l = r = 0
        return ans
