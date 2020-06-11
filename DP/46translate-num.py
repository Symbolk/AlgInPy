class Solution:
    # DP: O(n), O(n)
    def translateNum0(self, num: int) -> int:
        s = str(num)
        N = len(s)
        a = b = 1
        # dp[i] = dp[i-1]+dp[i-2] if n[i-1]*10+n[i] in [10, 25]
        for i in range(2, N + 1):
            a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
        return a

    def translateNum1(self, num: int) -> int:
        s = str(num)
        N = len(s)
        a = b = 1
        for i in range(N - 2, -1, -1):
            a, b = (a + b if 10 <= int(s[i]) * 10 + int(s[i + 1]) <= 25 else a), a
        return a

    # iteration: O(2^n), O(n) (with memo: O(n), O(n))
    def translateNum(self, num: int) -> int:
        if num <= 9:
            return 1
        # get the last two
        t = num % 100
        if t <= 9 or t >= 26:
            return self.translateNum(num // 10)
        else:
            return self.translateNum(num // 10) + self.translateNum(num // 100)

    # DP: O(n), O(1)
    def translateNum2(self, num: int) -> int:
        a = b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            a, b = (a + b if 10 <= x * 10 + y <= 25 else a), a
            y = x
        return a
