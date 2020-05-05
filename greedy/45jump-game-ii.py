from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N == 1:
            return 0

        res = 0
        far, end = 0, 0
        for i in range(N):
            if far >= N - 1:
                return res
            # i is reachable
            if i < far:
                end = max(end, i + nums[i])
                continue
            res += 1
            far = max(end, i + nums[i])
        return res

    # O(n), O(1)
    def jump1(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return 0
        res = 0
        far, end, cur = 0, 0, 0
        while end < N - 1:
            far = max(far, nums[cur] + cur)
            if cur == end:
                res += 1
                end = far
            cur += 1
        return res

    def jump2(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        # end: cur + nums[cur]
        # maxPos: the farthest reachable pos from cur
        maxPos, end = 0, 0
        for i in range(N - 1):
            if i <= maxPos:
                maxPos = max(maxPos, i + nums[i])
                # reach the end of current jump
                if i == end:
                    end = maxPos
                    # ! when end = 0, res has += 1, so range in N-1
                    res += 1
        return res

    # O(n^2) (worst case), O(1)
    # TLE
    def jump3(self, nums: List[int]) -> int:
        pos = len(nums) - 1
        res = 0
        while pos != 0:
            for i in range(pos):
                if nums[i] >= pos - i:
                    pos = i
                    res += 1
                    break
        return res


sol = Solution()
# print(sol.jump([0]))
# print(sol.jump([1, 2]))
# print(sol.jump([2, 1]))
# print(sol.jump([1, 1, 1, 1]))
print(sol.jump([1, 2, 1, 1, 1]))
print(sol.jump([2, 3, 1, 1, 4]))
