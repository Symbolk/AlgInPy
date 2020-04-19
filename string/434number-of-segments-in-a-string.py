# Notice the definition: where a segment is defined to be a contiguous sequence of non-space characters.
# so "Hello," and ",,,," are segments
class Solution:
    # O(n), O(n)
    def countSegments(self, s: str) -> int:
        # python split will strip first
        # ''.split()=[]
        return len(s.split())

    # O(n), O(1)
    def countSegments1(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # early check if i == 0 or i >= 1
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                res += 1
        return res


sol = Solution()
print(sol.countSegments("Hello, my name is John"))
print(sol.countSegments1(",,,, my name is John"))
