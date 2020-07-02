class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        N, M = len(A), len(B)
        ans = 0
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
                ans = max(ans, dp[i][j])
        return ans

    def maxUncrossedLines1(self, A: List[int], B: List[int]) -> int:
        N, M = len(A), len(B)
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
