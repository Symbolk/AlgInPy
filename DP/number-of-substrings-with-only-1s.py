class Solution:
    def numSub(self, s: str) -> int:
        if not s:
            return 0
        N = len(s)
        dp = [0] * N
        cnt = 0
        if s[0] == '1':
            dp[0] = 1
            cnt = 1
        for i in range(1, N):
            if s[i] == '0':
                dp[i] = dp[i-1]
                cnt = 0
            elif s[i] == '1':
                cnt += 1
                dp[i] = dp[i-1] + cnt

            # 10^9 --> 10**9 in py
        return dp[-1] % (10**9 + 7)


sol = Solution()
print(sol.numSub("1111111111011010011"))
