class Solution:
    # iteration
    @functools.lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        ans = 0
        for i in range(n):
            ans += self.numTrees(i) * self.numTrees(n - i - 1)
        return ans
        # return sum([self.numTrees(i - 1) * self.numTrees(n - i) for i in range(1, n + 1)])

    # DP: O(n^2), O(n)
    def numTrees1(self, n: int) -> int:
        # 1..n
        # G(n) = sum(G(i-1) * G(n-i)) for i in (1,n)
        # left sub-n: i; right sub-n: n - i - 1 (so in [0, n])
        # left sub-n: i-1; right sub-n: n - i (so in [1, n+1])
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            # subproblem
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]
