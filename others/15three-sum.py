from typing import List


class Solution:
    # sort and enumerate with pruning: O(n^2), O(1)
    # O(n^2) is good enough
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N < 3:
            return []
        res = []
        nums.sort()

        # k, i, j
        for k in range(N - 2):
            if nums[k] > 0:
                # impossible
                break
            if k > 0 and nums[k] == nums[k - 1]:
                # avoid duplicate res
                continue
            # i, c in (k, len(nums))
            i, j = k + 1, N - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    # move i right to increase
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        # jump duplicates
                        i += 1
                elif s > 0:
                    # move j left to decrease
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res

    # hash to achieve O(1) in checking: O(n^2), O(n)
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N < 3:
            return []
        res = []
        nums.sort()
        hashmap = {}

        for i, n in enumerate(nums):
            hashmap[n] = i

        for i in range(N - 2):
            if nums[i] > 0:
                break
            else:
                if i >= 1 and nums[i] == nums[i - 1]:
                    continue
                else:
                    for j in range(i + 1, N):
                        if j >= i + 2 and nums[j] == nums[j - 1]:
                            continue
                        else:
                            s = nums[i] + nums[j]
                            if -s in hashmap:
                                if hashmap.get(-s) > j:
                                    res.append([nums[i], nums[j], -s])
        return res

    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = []

        # i, j, k
        for i in range(N - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = N - 1
            target = - nums[i]
            for j in range(i + 1, N - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
        return res


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum2([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum3([-1, 0, 1, 2, -1, -4]))
