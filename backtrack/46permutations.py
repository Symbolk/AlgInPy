from typing import List


class Solution:
    # dfs and backtrack on the solution tree: O(n*n!), O(n*n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N == 0:
            return []

        def dfs(nums, length, depth, path, used, res):
            if depth == length:
                # note that path need to be cloned since it's passed by reference
                # res.append(path[:])
                res.append(path.copy())
                return
            for i in range(length):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(nums, N, depth + 1, path, used, res)
                # restore state
                path.pop()
                used[i] = False

        res = []
        used = [False] * N
        dfs(nums, N, 0, [], used, res)
        return res

    # backtrack: O(n*n!), O(n)
    def permute1(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N == 0:
            return []

        def backtrack(depth):
            if depth == N:
                res.append(nums[:])
            for i in range(depth, N):
                # swap two elements
                nums[depth], nums[i] = nums[i], nums[depth]
                backtrack(depth + 1)
                # restore state
                nums[depth], nums[i] = nums[i], nums[depth]

        res = []
        backtrack(0)
        return res


sol = Solution()
print(sol.permute([1, 2, 3]))
print(sol.permute1([1, 2, 3]))
