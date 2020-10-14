from collections import Counter


class Solution:
    # O(nm): n=len(A), m=avg(sum(len(a)))
    def commonChars(self, A: List[str]) -> List[str]:
        minfreq = [float('inf')] * 26
        for a in A:
            freq = [0] * 26
            for ch in a:
                freq[ord(ch) - ord('a')] += 1
            for i in range(26):
                minfreq[i] = min(minfreq[i], freq[i])

        res = list()
        for i in range(26):
            res.extend([chr(i + ord('a'))] * minfreq[i])
        return res

    def commonChars1(self, A: List[str]) -> List[str]:
        res = None
        for a in A:
            c = Counter(a)
            if res is None:
                res = c
            else:
                res &= c
        return list(res.elements())
