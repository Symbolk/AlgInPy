from typing import List


class Solution:
    # DP: O(n^2), O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        wordSet = set(wordDict)

        # dp[i]: whether 0...i-1 can be broken
        dp[0] = True
        # [0 ... j ... i]
        for i in range(1, N + 1):
            for j in range(i - 1, -1, -1):
                # transformation
                dp[i] = dp[j] and (s[j:i] in wordSet)
                # if found one, break
                if dp[i]:
                    break
        return dp[-1]

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        wordSet = set(wordDict)

        dp = [False] * (N + 1)
        dp[0] = True
        for i in range(N):
            if dp[i]:
                for j in range(i + 1, N + 1):
                    if s[i:j] in wordSet:
                        dp[j] = True
        return dp[-1]


sol = Solution()
print(sol.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(sol.wordBreak1(s="leetcode", wordDict=["leet", "code"]))
