from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # ord("a) = 97
        sArr = [ord(i) - 97 for i in s]
        pArr = [ord(i) - 97 for i in p]
        counter = [0 for _ in range(26)]

        m, n = len(s), len(p)

        for i in range(n):
            counter[pArr[i]] += 1

        l, r, num = 0, 0, 0
        res = []

        while r < m:
            counter[sArr[r]] -= 1
            if counter[sArr[r]] >= 0:
                num += 1
            if r > n - 1:  # now we can slide
                # sliding by one to right
                counter[sArr[l]] += 1
                if counter[sArr[l]] > 0:
                    # remove one but still exist
                    num -= 1
                l += 1
            if num == n:
                res.append(l)
            r += 1
        return res


sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
print(sol.findAnagrams("abab", "ab"))
