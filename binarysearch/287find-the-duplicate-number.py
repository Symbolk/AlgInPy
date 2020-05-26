class Solution:
    # nums is not sorted, but [1,n] is!
    # binary guess the duplicate num between its range: [1,n]
    # O(nlogn), O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        n = N - 1  # [1, n]
        l, r = 1, n
        while l < r:
            mid = l + ((r - l) >> 1)
            cnt = 0
            for num in nums:
                if num <= m:
                    cnt += 1
            if cnt > mid:
                # in the left part
                r = mid
            else:
                # in the right part
                l = mid + 1
        return l

    # slow&fast pointers to find loop: O(n), O(1)
    # if there are duplicate num as the index, will form a loop
    def findDuplicate1(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0]
        i = j = 0
        # point to the first i!=nums[i]
        for i in range(len(nums)):
            if i != nums[i]:
                i = j = i
                break

        while True:
            # 1 jump
            i = nums[i]
            # 2 jumps
            j = nums[nums[j]]
            if i == j:
                # find loop
                break
        i = 0
        while True:
            i = nums[i]
            j = nums[j]
            if j == i:
                break
        return i