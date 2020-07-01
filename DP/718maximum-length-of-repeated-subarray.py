class Solution:
    # forward DP: O(n*m), O(n*m)
    def findLength(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        M = len(B)
        # (M+1) cols, (N+1) rows
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        ans = 0
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                # dp[i][j] = findLength(A[:i], B[:j]
                dp[i][j] = dp[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else 0
                ans = max(ans, dp[i][j])

        return ans

    # backward DP: O(n*m), O(n*m)
    def findLength1(self, A: List[int], B: List[int]) -> int:
        N, M = len(A), len(B)
        ans = 0
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                # dp[i][j] = findLength(A[i:], B[j:]
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])

        return ans
