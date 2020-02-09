class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len1 = len(s)
        len2 = len(t)

        if len1 != len2:
            return False
        counter = [0 for _ in range(26)]

        for i in range(len1):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1

        for c in counter:
            if c != 0:
                return False

        return True