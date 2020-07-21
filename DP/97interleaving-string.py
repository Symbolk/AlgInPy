class Solution:
    # DP: O(mn), O(mn)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True
        # is able to form first i char in s3 with just first i char in s1
        for i in range(1, l1 + 1):
            dp[i][0] = dp[i - 1][0] and s3[i - 1] == s1[i - 1]
        for j in range(1, l2 + 1):
            dp[0][j] = dp[0][j - 1] and s3[j - 1] == s2[j - 1]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                dp[i][j] = (dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]) or (
                        dp[i - 1][j] and s3[i - 1 + j] == s1[i - 1])
        return dp[-1][-1]

    # O(mn), O(m)
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        dp = [False] * (l2 + 1)
        dp[0] = True
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                k = i + j - 1
                if i > 0 and s3[k] != s1[i - 1]:
                    dp[j] = False
                if j > 0 and s3[k] == s2[j - 1]:
                    dp[j] |= dp[j - 1]
        return dp[-1]
