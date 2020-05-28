class Solution:
    # O(n^2), O(1)
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        # [j,i]
        for i in range(N):
            sum = 0
            for j in range(i, -1, -1):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res

    # O(n^2), O(1)
    def subarraySum1(self, nums: List[int], k: int) -> int:
        res = 0
        N = len(nums)
        for l in range(N):
            sum = 0
            for r in range(l, N):
                sum += nums[r]
                if sum == k:
                    res += 1
        return res

    # naive presum: O(n^2), O(n)
    # presum[0] = 0
    # nums[i] = presum[i+1] - presum[i]
    # sum[i,j] = presum[j] - presum[i - 1]
    # presum[j] - presum[i] = sum[i, j-1]
    def subarraySum2(self, nums: List[int], k: int) -> int:
        N = len(nums)
        presum = [0] * (N + 1)
        for i in range(N):
            presum[i + 1] = presum[i] + nums[i]
        res = 0
        for l in range(0, N):
            for r in range(l, N):
                if presum[r + 1] - presum[l] == k:
                    res += 1
        return res

    # presum + hashmap: O(n), O(n)
    def subarraySum3(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        # presum: times
        d = {0: 1}
        presum = 0
        res = 0
        for n in nums:
            presum += n
            # presum - (presum - k) = k --> res+=
            if d.get(presum - k):
                res += d[presum - k]
            if d.get(presum):
                d[presum] += 1
            else:
                d[presum] = 1
        return res
