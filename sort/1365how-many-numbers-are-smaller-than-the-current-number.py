from typing import List


class Solution:
    # O(nlogn), O(n)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nn = sorted(nums)
        dic = {}
        for i, n in enumerate(nn):
            if n not in dic:
                dic[n] = i

        res = []
        for n in nums:
            res.append(dic[n])
        return res

    # one line
    # O(n^2), O(1)
    def smallerNumbersThanCurrent0(self, nums: List[int]) -> List[int]:
        return [len(list(filter(lambda x: x < i, nums))) for i in nums]

    # note that 0 <= nums[i] <= 100
    # counting sort: O(n+k), O(k) (k is the range of num)
    def smallerNumbersThanCurrent1(self, nums: List[int]) -> List[int]:
        bins = [0] * 101
        res = []
        for n in nums:
            bins[n] += 1

        # count for all in [0, 100]
        less = []
        tmp = 0
        for b in bins:
            less.append(tmp)
            tmp += b

        # return what's needed
        for n in nums:
            res.append(less[n])
        return res


s = Solution()

print(s.smallerNumbersThanCurrent1([8, 1, 2, 2, 3]))
