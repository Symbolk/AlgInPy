from typing import List


class Solution:
    # fix two pointers and move two pointers: O(n^3)
    # although O(n^3), with min/max comparing with target, much faster
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        if N < 4:
            return []
        res = []
        nums.sort()

        # at least leave 4 nums, so <= N - 4
        for a in range(N - 3):
            # a > 0 is vital
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            # min_sum > target
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            if nums[a] + nums[N - 3] + nums[N - 2] + nums[N - 1] < target:
                continue
            for b in range(a + 1, N - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c = b + 1
                d = N - 1
                # min_sum > target
                if nums[a] + nums[b] + nums[c] + nums[c + 1] > target:
                    break
                # max_sum > target
                if nums[a] + nums[d - 2] + nums[d - 1] + nums[d] < target:
                    break
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    if s < target:
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                    elif s > target:
                        d -= 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
        return res

    # n sum to target
    def nSum(self, nums: List[int], target: int, n: int) -> List[int]:
        N = len(nums)

        def dfs(pos: int, cur: List[int], n: int, target: int) -> None:
            if n == 2:
                l, r = pos, N - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                    elif s > target:
                        r -= 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                    else:
                        res.append(cur[:] + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
            else:
                i = pos
                while i < N - n + 1:
                    # trick here to prune!
                    if nums[i] * n > target or nums[-1] * n < target:
                        break
                    if i > pos and nums[i] == nums[i - 1]:
                        i += 1
                        continue
                    cur.append(nums[i])
                    dfs(i + 1, cur, n - 1, target - nums[i])
                    cur.pop()
                    i += 1

        # inside nSum()
        res = []
        nums.sort()
        dfs(0, [], n, target)
        return res

    # DFS
    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        return self.nSum(nums, target, 4)

    # hash: O(n^2)
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        if N < 4:
            return []
        # use set to deduplicate
        res = set()
        nums.sort()
        # sum:[(index1, index2)]
        table = {}

        for i in range(N - 1):
            for j in range(i + 1, N):
                s = nums[i] + nums[j]
                if target - s in table:
                    for tmp in table[target - s]:
                        if tmp[1] < i:
                            # use tuple since it is hashable
                            res.add((nums[tmp[0]], nums[tmp[1]], nums[i], nums[j]))
                if s not in table:
                    table[s] = []
                table[s].append((i, j))
        # convert set to list
        ans = []
        for r in res:
            ans.append(list(r))
        return ans


sol = Solution()
print(sol.fourSum2([1, 0, -1, 0, -2, 2], 0))
# print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
# print(sol.fourSum1([1, 0, -1, 0, -2, 2], 0))
# print(sol.fourSum([-1, 2, 2, -5, 0, -1, 4], 3))
# print(sol.fourSum1([0, 0, 0, 0], 0))
