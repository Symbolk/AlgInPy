from typing import List


class Solution:
    # brutal force: O(n^2), O(n)
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        count = Counter(deck)
        N = len(deck)
        for i in range(2, N + 1):
            if N % i == 0:
                if all(v % i == 0 for v in count.values()):
                    return True
        return False

    # gcd: O(nlogc), O(n) (c is the range of deck)
    def hasGroupsSizeX1(self, deck: List[int]) -> bool:
        from collections import Counter
        from functools import reduce
        # Greatest Common Divider
        def gcd(a, b):
            return b if a % b == 0 else gcd(b, a % b)

        # from fractions import gcd
        # from math import gcd
        counts = Counter(deck).values()
        return reduce(gcd, counts) >= 2


sol = Solution()
# print(sol.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
# print(sol.hasGroupsSizeX([1]))
# print(sol.hasGroupsSizeX([1, 1]))
# print(sol.hasGroupsSizeX([1,1,1,2,2,2,3,3]))
print(sol.hasGroupsSizeX1([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]))
