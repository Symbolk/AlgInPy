class Solution:
    # brutal force (TLE)
    def getMaxRepetitions1(self, s1: str, n1: int, s2: str, n2: int) -> int:
        L1, L2 = len(s1), len(s2)
        index = 0
        cnt = 0
        for i in range(n1):
            for j in range(L1):
                if s1[j] == s2[index]:
                    index += 1
                if index == L2:
                    index = 0
                    cnt += 1
        return cnt // n2

    # O(max(|s1|*|s2|, n1)), O(|s2|)
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        L1, L2 = len(s1), len(s2)
        if L1 * n1 < L2 * n2:
            return 0

        # simulate to match s1 with s2[i:]
        # next pos to start in s2
        next_char = {}
        # repeat nums of s2 in single s1
        repeat = {}
        for i in range(L2):
            cnt = 0
            # !use i/j to match s2 in s1 (subseq)
            index = i
            for j in range(L1):
                if s1[j] == s2[index]:
                    index += 1
                if index == L2:
                    cnt += 1
                    index = 0
            next_char[i] = index
            repeat[i] = cnt

        # match in s1*n1
        res = 0
        index = 0
        for i in range(n1):
            res += repeat[index]
            index = next_char[index]

        # num of matched s2
        return res // n2


sol = Solution()
print(sol.getMaxRepetitions1('acb', 4, 'ab', 2))
print(sol.getMaxRepetitions1('acb', 1, 'acb', 1))
print(sol.getMaxRepetitions('abaacdbac', 10, 'adcbd', 4))
