from typing import List


class Solution:
    # presum + brutal force: O(n^2), O(n)
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        presum = [0] * (N + 1)
        for i in range(N):
            presum[i + 1] = presum[i] + nums[i]
        for l in range(0, N - 1):  # at least 2
            for r in range(l + 1, N):
                # sum[l+1,r+1] = presum[r+1] - presum[l+1-1]
                sum = presum[r + 1] - presum[l]
                if sum == k or (k != 0 and sum % k == 0):
                    return True

        return False

    # presum + hashmap: O(n), O(min(n,k))
    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        # sum%k : index
        map = {0: -1}
        cursum = 0
        for i in range(N):
            cursum += nums[i]
            if k != 0:
                cursum %= k
            if cursum in map:
                if i - map[cursum] > 1:
                    return True
            else:
                map[cursum] = i
        return False


sol = Solution()
print(sol.checkSubarraySum([0, 1, 0], 0))
print(sol.checkSubarraySum([0, 0], 0))
