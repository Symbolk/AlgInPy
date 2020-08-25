from typing import List
class Solution:
    # dfs or backtrack in the solution tree!
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        def dfs(i, cur):
            if len(cur) > 1:
                res.append(list(cur))
            st = set()
            # find the next element for increasing seq
            for j in range(i+1, N):
                if nums[j] in st:
                    continue
                # deduplicate
                st.add(nums[j])
                if i == -1 or nums[j] >= nums[i]:
                    # select or not
                    cur.append(nums[j])
                    dfs(j, cur)
                    cur.pop()
        dfs(-1, [])
        return res

s = Solution()
print(s.findSubsequences([4, 6, 7, 7]))