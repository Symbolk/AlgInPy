from typing import List


class Solution:
    # brutal force (O(n^2), O(1)) TO
    def majorityElement1(self, nums: List[int]) -> int:
        majority_count = len(nums) / 2
        for n in nums:
            count = sum(1 for e in nums if e == n)
            if count > majority_count:
                return n

    # hash table (O(n), O(n))
    def majorityElement2(self, nums: List[int]) -> int:
        import collections
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # hash table (O(n), O(n))
    def majorityElement3(self, nums: List[int]) -> int:
        counter = {}
        N = len(nums)
        if N == 1:
            return nums[0]
        for i in range(N):
            if nums[i] not in counter:
                counter[nums[i]] = 1
            else:
                counter[nums[i]] += 1
                if counter[nums[i]] > N / 2:
                    return nums[i]

    # sorting (notice that the majority must exist) O(nlogn), O(1)
    def majorityElement4(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    # divide and conquer O(nlogn), O(lgn)
    def majorityElement5(self, nums: List[int]) -> int:
        def fun(l, r):
            if l == r:  # only one num
                return nums[l]
            m = l + (r - l) // 2
            left = fun(l, m)
            right = fun(m + 1, r)
            # same maj
            if left == right:
                return left
            left_count = sum(1 for i in range(l, r + 1) if nums[i] == left)
            right_count = sum(1 for i in range(l, r + 1) if nums[i] == right)
            return left if left_count > right_count else right

        return fun(0, len(nums) - 1)

    # Boyer-Moore Majority Vote Algorithm (O(n), O(1))
    def majorityElement6(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif nums[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate


sol = Solution()
# major element means the one whose count > n/2, not the most frequent element
print(sol.majorityElement2([2, 2, 1, 1, 1, 2, 2]))
print(sol.majorityElement5([2, 2, 1, 1, 1, 2, 2]))
