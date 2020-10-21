class Solution:
    # O(n+m), O(1)
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and typed[j] == name[i]:
                i += 1
                j += 1
            elif j >= 1 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)


s = Solution()
# print(s.isLongPressedName('alex', 'aaleex'))
print(s.isLongPressedName("vtkgn", "vttkgnn"))
