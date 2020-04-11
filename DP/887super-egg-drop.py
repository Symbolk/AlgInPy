class Solution:
    # O(KNlogN), O(KN)
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    # binary search
                    l, h = 1, n
                    while l + 1 < h:
                        x = (l + h) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)
                        if t1 < t2:
                            l = x
                        elif t1 > t2:
                            h = x
                        else:
                            l = h = x
                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x)) for x in (l, h))
                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)


sol = Solution()
print(sol.superEggDrop(1, 2))
print(sol.superEggDrop(2, 6))
print(sol.superEggDrop(3, 14))
