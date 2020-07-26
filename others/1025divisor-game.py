class Solution:
    # mathematical induction: who gets even win: O(1), O(1)
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

    # dp: O(n^2), O(n)
    # 1 <= N <= 1000
    def divisorGame1(self, N: int) -> bool:
        if N == 1:
            return False
        dp = [False] * (N + 1)
        dp[1] = False
        dp[2] = True
        for i in range(3, N + 1):
            for j in range(1, i // 2 + 1):
                # exists i-j that make Bob lose, then Alice win
                if i % j == 0 and dp[i - j] == False:
                    dp[i] = True
                    break
        return dp[N] == True
