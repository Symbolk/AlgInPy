class Solution:
    # possible duplicates in t
    # sliding window
    def minWindow0(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ''
        from collections import Counter, defaultdict
        need = Counter(t)
        window = defaultdict(lambda: 0)
        l, r = 0, 0
        valid = 0
        start = 0  # save the start of the final substring
        min_len = len(s) + 1
        while r < len(s):
            cr = s[r]
            if cr in need:
                window[cr] += 1
                if window[cr] == need[cr]:
                    valid += 1
            r += 1

            while valid == len(need):
                # [l, r)
                if r - l < min_len:
                    start = l
                    min_len = r - l
                cl = s[l]
                if cl in need:
                    if window[cl] == need[cl]:
                        valid -= 1
                    window[cl] -= 1
                l += 1

        return '' if min_len == len(s) + 1 else s[start:start + min_len]

    def minWindow1(self, s: str, t: str) -> str:
        from collections import Counter
        # a dict/map with unique key
        # NOTICE: len(counter) not necessarily equals len(t)
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
    def minWindow2(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ''
        from collections import defaultdict
        need = defaultdict(lambda: 0)
        window = defaultdict(lambda: 0)
        for tc in t:
            need[tc] += 1
        min_len = len(s) + 1
        start, end = 0, 0  # final result
        distance = 0
        l, r = 0, 0
        while r < len(s):
            cr = s[r]
            if window[cr] < need[cr]:
                distance += 1
            window[cr] += 1
            r += 1
            while distance == len(t):
                cl = s[l]
                if window[cl] > need[cl]:
                    window[cl] -= 1
                    l += 1
                else:
                    if r - l < min_len:
                        min_len = r - l
                        start, end = l, r
                    break
        return '' if min_len == len(s) + 1 else s[start:end]


sol = Solution()
print(sol.minWindow0("ADOBECODEBANC", "ABC"))
print(sol.minWindow1("ADOBECODEBANC", "ABC"))
print(sol.minWindow2("ADOBECODEBANC", "ABC"))
print(sol.minWindow1("aa", "aa"))
