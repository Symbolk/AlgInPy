from typing import List
import functools


class Solution:
    # DP (bottom up): O(mn), O(mn)
    def minDistance0(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j] = the min ED to convert word1[:i] to word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

        return dp[-1][-1]

    # top down (fast with LRU Cache)
    @functools.lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) + len(word2)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            inserted = 1 + self.minDistance(word1, word2[1:])
            deleted = 1 + self.minDistance(word1[1:], word2)
            replaced = 1 + self.minDistance(word1[1:], word2[1:])
            return min(inserted, deleted, replaced)

    def minDistance1(self, word1: str, word2: str) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            # terminator: if one or both over
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            else:
                inserted = helper(i, j + 1)
                deleted = helper(i + 1, j)
                replaced = helper(i + 1, j + 1)
                return min(inserted, deleted, replaced) + 1

        return helper(0, 0)


solution = Solution()
print(solution.minDistance0("intention", "execution"))
print(solution.minDistance("intention", "execution"))
print(solution.minDistance1("horse", "ros"))
