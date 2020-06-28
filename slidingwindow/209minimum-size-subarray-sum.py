from typing import List


class Solution:
    # double pointers: O(n), O(1)
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        ans = N + 1
        l, r = 0, 0
        total = 0
        while r < N:
            total += nums[r]
            while total >= s:
                ans = min(ans, r - l + 1)
                # remove the left-most num
                total -= nums[l]
                # move left forward
                l += 1
            r += 1
        return 0 if ans == N + 1 else ans

    # presum (incremental) + binary search: O(nlogn), O(n)
    def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
        import bisect
        if not nums:
            return 0
        N = len(nums)
        ans = N + 1
        sums = [0]
        for i in range(N):
            sums.append(sums[-1] + nums[i])

        for i in range(1, N + 1):
            target = s + sums[i - 1]
            low = bisect.bisect_left(sums, target)
            if low != len(sums):
                ans = min(ans, low - (i - 1))

        return 0 if ans == N + 1 else ans

    # presum + my binary search
    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        def bisect(arr, t):
            l, r = 0, len(sums) - 1
            while l < r:
                m = l + ((r - l) >> 1)
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m
            # find the first >= t index
            return l if arr[l] >= t else -1

        N = len(nums)
        ans = N + 1
        sums = [0] * (N + 1)
        for i in range(1, N + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        for i in range(1, N + 1):
            target = s + sums[i - 1]
            bound = bisect(sums, target)
            if bound >= 0 and bound != len(sums):
                ans = min(ans, bound - (i - 1))
        return 0 if ans == N + 1 else ans


sol = Solution()
print(sol.minSubArrayLen1(s=7, nums=[2, 3, 1, 2, 4, 3]))
print(sol.minSubArrayLen2(s=7, nums=[2, 3, 1, 2, 4, 3]))
