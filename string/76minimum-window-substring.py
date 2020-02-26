class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        # a dict/map with unique key
        # NOTICE: len(counter) not neccessary equals len(t)
        counter = Counter(t)

        l, num = 0, 0
        res = ""

        for r, cr in enumerate(s):
            if cr not in counter:
                continue
            counter[cr] -= 1
            if counter[cr] == 0:
                num += 1

            while num == len(counter) and l <= r:
                if not res or len(res) > (r - l + 1):
                    res = s[l:r + 1]
                cl = s[l]
                if cl in counter:
                    counter[cl] += 1
                if counter[cl] == 1:
                    num -= 1
                l += 1
        return res

    # incorrect
    def minWindow1(self, s: str, t: str) -> str:
        # NOT LIMITED TO UPPERCASE!!!
        # ord("A") = 65
        sArr = [ord(i) - 65 for i in s]
        tArr = [ord(i) - 65 for i in t]
        counter = [0 for _ in range(26)]
        l, r, start = 0, 0, 0
        num = 0
        M, N = len(s), len(t)
        for i in range(N):
            counter[tArr[i]] += 1

        import sys
        minLen = sys.maxsize
        for r in range(M):
            if counter[sArr[r]] == 0:
                continue
            counter[sArr[r]] -= 1
            if counter[sArr[r]] == 0:
                num += 1
            while num == N and l <= r:
                if r - l < minLen:
                    start = l
                    minLen = r - l
                if counter[sArr[l]] > 0:
                    counter[sArr[l]] += 1
                if counter[sArr[l]] == 1:
                    num -= 1
                l += 1

        return "" if minLen == sys.maxsize else s[start:start + minLen]


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("aa", "aa"))
