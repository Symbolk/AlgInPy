class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    # rolling array
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(2)]
        k, l = 0, 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[k][j] = dp[l][j - 1] + 1
                else:
                    dp[k][j] = max(dp[k][j - 1], dp[l][j])
            k, l = l, k
        return dp[l][-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonSubsequence("abcde", "abc"))
    print(solution.longestCommonSubsequence2("abcde", "abcde"))
