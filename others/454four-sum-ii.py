class Solution:
    # convert to 2sum: hash to counter sum, O(n^2)
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import defaultdict
        # set type of value to be int with default 0
        lookup = defaultdict(int)

        res = 0
        for a in A:
            for b in B:
                lookup[a + b] += 1

        for c in C:
            for d in D:
                res += lookup[-(c + d)]
        return res

    # use counter to record duplicates: O(n^2)
    def fourSumCount1(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import Counter
        dic = Counter(a + b for a in A for b in B)
        return sum(dic.get(-(c + d), 0) for c in C for d in D)
