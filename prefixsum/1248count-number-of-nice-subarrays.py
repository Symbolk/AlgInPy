class Solution:
    # pre odd cnt (number of odds util i): O(n), O(n)
    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # key/index: #odd cnt pre
        # value: times
        preCnt = [0] * (N + 1)
        # handle the case when nums are all odds
        preCnt[0] = 1
        res = 0
        sum = 0
        for n in nums:
            # if odd, add 1; if even, add 0
            sum += (n & 1)
            preCnt[sum] += 1
            if sum >= k:
                res += preCnt[sum - k]
        return res
