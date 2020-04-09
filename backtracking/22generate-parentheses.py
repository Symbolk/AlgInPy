from typing import List
from functools import lru_cache


class Solution:
    # brutal force/recursion: O(2^2n*n), O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    res.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            cnt = 0
            for c in A:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        generate([])
        return res

    # backtrack with pruning: much faster than force
    def generateParenthesis1(self, n: int) -> List[str]:
        res = []

        # number of left and right bracket
        def backtrack(S, l, r):
            if len(S) == 2 * n:
                res.append(''.join(S))
                return
            if l < n:
                S.append('(')
                backtrack(S, l + 1, r)
                S.pop()
            if r < l:
                S.append(')')
                backtrack(S, l, r + 1)
                S.pop()

        backtrack([], 0, 0)
        return res

    # iterate with seq length: S = (a)b
    @lru_cache(None)
    def generateParenthesis2(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        res = []
        for i in range(n):
            for l in self.generateParenthesis(i):
                for r in self.generateParenthesis(n - i - 1):
                    res.append('({}){}'.format(l, r))

        return res

    # search util complete state in the solution space, so use dfs(recursion)
    # bracket matching, so use stack
    def generateParenthesis3(self, n: int) -> List[str]:
        res = []

        # remaining number of left and right bracket
        # use stack to test if valid (only keep '(')
        def dfs(l, r, stack, S):
            # reach complete state/get a feasible solution
            if l == r == 0 and len(stack) == 0:
                res.append(S)
                return
            if l > 0:
                dfs(l - 1, r, stack + ['('], S + '(')
            if stack and stack[-1] == '(':
                stack.pop()
                dfs(l, r - 1, stack, S + ')')

        dfs(n, n, [], '')
        return res

    # dp: bottom up, from basic/simple case to final case
    def generateParenthesis4(self, n: int) -> List[str]:
        if n == 0:
            return []
        # use dp[i] to save the sequence list
        dp = [None for _ in range(n + 1)]
        # base case
        dp[0] = ['']

        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for l in left:
                    for r in right:
                        cur.append('({}){}'.format(l, r))
            dp[i] = cur
        return dp[n]


sol = Solution()
print(sol.generateParenthesis3(3))
