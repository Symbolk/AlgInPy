import random
import heapq  # min heap by default


class Solution:
    # sort first: O(nlogn), O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

    # built-in heap: O(n), O(logn)
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        q = []
        for c in nums:
            heapq.heappush(q, c)
            # size of heap <= k
            while len(q) > k:
                heapq.heappop(q)
        return heapq.heappop(q)

    def findKthLargest21(self, nums: List[int], k: int) -> int:
        N = len(nums)
        q = []
        for i in range(k):
            heapq.heappush(q, nums[i])

        for i in range(k, N):
            top = q[0]
            if nums[i] > top:
                # Pop and return the current smallest value, and add the new item.
                heapq.heapreplace(q, nums[i])
        return q[0]

    # quicksort: O(n), O(1)
    def partition(self, nums, l, r):
        # randomization for average performance
        random_index = random.randint(l, r)  # [l, r]
        nums[random_index], nums[l] = nums[l], nums[random_index]

        pivot = nums[l]
        j = l
        for i in range(l + 1, r + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[l], nums[j] = nums[j], nums[l]
        # [l+1, j] < pivot, (j, i) >= pivot
        return j

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        N = len(nums)
        target = N - k
        l, r = 0, N - 1
        while True:
            i = self.partition(nums, l, r)
            if i == target:
                return nums[i]
            elif i < target:
                # ans in the right part
                l = i + 1
            else:
                r = i - 1

    def partition4(self, nums, l, r):
        ri = random.randint(l, r)
        nums[l], nums[ri] = nums[ri], nums[l]

        pivot = nums[r]
        index = l

        for i in range(l, r):
            if nums[i] < pivot:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[index], nums[r] = nums[r], nums[index]
        return index

    def findKthLargest4(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l, r = 0, N - 1
        i = self.partition(nums, l, r)
        while i != N - k:
            if i < N - k:
                l = i + 1
            else:
                r = i - 1
            i = self.partition(nums, l, r)
        return nums[i]

    # a + ~a = -1
    def getMedian(self, nums):
        nums.sort()
        middle = len(nums) // 2
        return (nums[middle] + nums[~middle]) / 2
