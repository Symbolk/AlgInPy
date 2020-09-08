from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        from collections import Counter
        cnt = Counter(candies)
        N = len(candies) // 2
        i = 0
        res = set()
        for j in cnt:
            if cnt[j] > 0:
                res.add(j)
                cnt[j] -= 1
                i += 1
                if i == N:
                    break
        return len(res)

    def distributeCandies1(self, candies: List[int]) -> int:
        from collections import Counter
        cnt = Counter(candies)
        res = 0
        for c in cnt:
            if cnt[c] > 0 and res < len(candies) // 2:
                res += 1
                cnt[c] -= 1
        return res

    def distributeCandies2(self, candies: List[int]) -> int:
        return len(set(candies)) if len(set(candies)) < len(candies) // 2 else len(candies) // 2


s = Solution()
print(s.distributeCandies([1, 1, 2, 2, 3, 3]))
print(s.distributeCandies([1, 1, 2, 3]))
