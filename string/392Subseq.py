class Solution:
    # pythonic
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(i in t for i in s)

    # double pointers: O(m+n), O(1)
    def isSubsequence1(self, s: str, t: str) -> bool:
        M, N = len(s), len(t)
        if M > N:
            return False
        i = j = 0
        while i < M and j < N:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == M

    # with stack: O(n), O(n)
    def isSubsequence2(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        stack = []
        M, N = len(s), len(t)
        for i in range(M - 1, -1, -1):
            stack.append(s[i])
        for j in range(N):
            if stack[-1] == t[j]:
                stack.pop()
            if len(stack) == 0:
                return True
        return False

    # DP: pre-cache t to speed up matching many s
    def isSubsequence3(self, s: str, t: str) -> bool:
        M, N = len(s), len(t)
        # dp[i][j]: first appear position of j in t[i:]
        # if t[i:] == j, then dp[i][j] = j
        # else: sub-problem: t[i+1:]
        # the (N+1)th row is the border case, no chars at all
        dp = [[-1] * 26 for _ in range(N + 1)]

        # "first appear", so backwards
        for i in range(N - 1, -1, -1):
            for j in range(26):
                if ord(t[i]) - ord('a') == j:
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i + 1][j]

        # start from 0 of the table, and jump
        i = 0
        for k in range(M):
            if dp[i][ord(s[k]) - ord('a')] == -1:
                # found one char not appear in t
                return False
            # jump to the next row
            i = dp[i][ord(s[k]) - ord('a')] + 1
        return True


s = Solution()
print(s.isSubsequence3("abc", "ahbgdc"))
