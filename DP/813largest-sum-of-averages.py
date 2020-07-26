class Solution:
    # forward DP: O(K*n^2), O(N*K)
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N = len(A)
        presum = [0]
        for a in A:
            presum.append(presum[-1] + a)

        # [i:j], or [i, j)
        def avg(i, j):
            return (presum[j] - presum[i]) / float(j - i)

        # dp[i][k]: divide first i nums into k groups
        # i ranges between 0 and N, so N + 1
        # k ranges between 0 and K, so K + 1
        dp = [[0.0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            # k == 1
            dp[i][1] = avg(0, i)
            for k in range(2, min(K, i) + 1):
                # [0:j]: k-1 groups
                # [j:i]: k-the group
                for j in range(1, i):
                    dp[i][k] = max(dp[i][k], dp[j][k - 1] + avg(j, i))

        return dp[-1][-1]

    # backward DP: O(K*n^2), O(N)
    def largestSumOfAverages1(self, A: List[int], K: int) -> float:
        N = len(A)
        presum = [0] * (N + 1)
        for i in range(N):
            presum[i + 1] = presum[i] + A[i]

        # [i:j], or [i, j)
        def avg(i, j):
            return (presum[j] - presum[i]) / float(j - i)

        dp = [0.0] * N
        for i in range(N):
            dp[i] = avg(i, N)
        for k in range(1, K):
            for i in range(N):
                for j in range(i + 1, N):
                    dp[i] = max(dp[i], dp[j] + avg(j, i))

        return dp[0]
