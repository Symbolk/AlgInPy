class Solution:
    # so smart: O(n), O(1)
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s * 2).index(s, 1) != len(s)

    # remove the first and last char and check contains
    def repeatedSubstringPattern1(self, s: str) -> bool:
        return s in (s+s)[1:-1]

    # enum n (len of repeated s'): O(N^2), O(1)
    # s[i] == s[i-n] for i in [n,N)
    def repeatedSubstringPattern1(self, s: str) -> bool:
        N = len(s)
        for n in range(1, N//2+1):
            if N % n == 0:
                if all(s[i] == s[i-n] for i in range(n, N)):
                    return True
        return False