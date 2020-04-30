class Solution:
    # brutal force: O(logn), O(logn)
    def isHappy(self, n: int) -> bool:
        def compute(n):
            res = 0
            # iterator
            digits = map(int, list(str(n)))
            # digits = list(map(int, list(str(n))))
            for d in digits:
                res += d ** 2
            return res

        visited = set()
        s = compute(n)
        while s != 1:
            if s in visited:
                return False
            else:
                visited.add(s)
                s = compute(s)
        return True

    def isHappy1(self, n: int) -> bool:
        def get_next(n):
            res = 0
            while n > 0:
                n, digit = divmod(n, 10)
                res += d ** 2
            return res

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1

    # slow and quick pointers to check loop: O(logn) but quicker, O(1)
    def isHappy2(self, n: int) -> bool:
        def get_next(n):
            res = 0
            while n > 0:
                d = n % 10
                res += d ** 2
                n //= 10
            return res

        i, j = n, get_next(n)
        while j != -1 and i != j:
            i = get_next(i)
            j = get_next(get_next(j))
        return j == 1


sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(23))
print(sol.isHappy(7))
print(sol.isHappy2(116))
