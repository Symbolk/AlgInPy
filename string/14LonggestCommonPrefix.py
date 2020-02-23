from typing import List

class Solution:
    # 行列遍历
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][0:i]

        return strs[0]


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
