class Solution:
    # DP: O(n^3), O(n^2)
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (N + 2) for _ in range(N + 2)]
        # backward
        for i in range(N - 1, -1, -1):
            for j in range(i + 2, N + 2):
                # k is the last burst ballon
                # (i,j) == [i+1, j-1]
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
        return dp[0][N + 1]

    # memorized searching: O(n^3), O(n^2)
    def maxCoins1(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def solve(l, r):
            if r - l <= 1:
                return 0
            res = 0
            for i in range(l + 1, r):
                res = max(res, solve(l, i) + nums[l] * nums[i] * nums[r] + solve(i, r))
            return res

        return solve(0, N + 1)

    def maxCoins2(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (N + 2) for _ in range(N + 2)]
        # forward
        for j in range(2, N + 2):
            for i in range(j - 2, -1, -1):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])

        return dp[0][N + 1]

    # enumerate length
    def maxCoins4(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        for length in range(2, N):
            for i in range(0, N - length):
                # i < N - length
                j = i + length
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
        return dp[0][-1]
