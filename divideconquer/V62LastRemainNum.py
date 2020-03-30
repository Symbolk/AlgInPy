import sys

sys.setrecursionlimit(100000)


class Solution:
    # brutal force/simulation: O(n^2)
    def lastRemaining0(self, n: int, m: int) -> int:
        a = list(range(n))
        i = 0
        while len(a) > 1:
            i = (i + m - 1) % len(a)
            a.pop(i)  # O(n)
        return a[0]

    # recursion: O(n), O(n)
    def lastRemaining(self, n: int, m: int) -> int:
        def f(n, m):
            if n == 0:
                return 0
            return (m + f(n - 1, m)) % n

        return f(n, m)

    # iteration: O(n), O(1)
    def lastRemaining1(self, n: int, m: int):
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f

    def lastRemaining2(self, n: int, m: int):
        if n < 1 or m < 1:
            return None
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last


sol = Solution()
print(sol.lastRemaining(5, 3))
print(sol.lastRemaining(10, 17))
