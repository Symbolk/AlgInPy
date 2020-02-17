class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(i in t for i in s)

    def isSubsequence2(self, s: str, t: str) -> bool:
        t = iter(t)
        gen = (i for i in s)
        for i in gen:
            print(i)
        gen = ((i in t) for i in s)
        for i in gen:
            print(i)

        b = (i for i in range(5))
        print(2 in b)
        print(4 in b)
        print(3 in b)

sol = Solution()
print(sol.isSubsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(sol.isSubsequence2([1, 4, 3], [1, 2, 3, 4, 5]))
