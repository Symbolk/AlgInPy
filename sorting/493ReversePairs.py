# incorrect
def reversePairs(nums):
    n = len(nums)
    if n < 2:
        return 0
    return merge_sort(nums, 0, n - 1)


def merge_in_place(arr, l, mid, r):
    left = arr[l:mid + 1]
    right = arr[mid + 1:r + 1]
    k = l
    while left and right:
        arr[k] = left.pop(0) if left[0] < right[0] else right.pop(0)
        k += 1
    tail = left if left else right
    for n in tail:
        arr[k] = n
        k += 1


def merge_sort(nums, l, r):
    if l >= r:
        return 0
    m = (l + r) >> 1
    lc = merge_sort(nums, l, m)
    rc = merge_sort(nums, m + 1, r)
    count = 0
    i = l
    for j in range(m + 1, r + 1):
        while i <= m and (nums[i] >> 1) <= nums[j]:
            i += 1
        if i > m:
            break
        else:
            count += m - i + 1
    merge_in_place(nums, l, m, r)
    return lc + count + rc


# correct but TLE
from typing import List
import bisect


def reversePairs2(nums: List[int]) -> int:
    res = 0
    sorted_values = []
    for j in range(len(nums)):
        i = bisect.bisect_right(sorted_values, 2 * nums[j])
        res += (j - i)
        bisect.insort(sorted_values, nums[j])
    return res


# correct
class Solution:
    def __init__(self):
        self.cnt = 0

    def reversePairs(self, nums):
        def msort(arr):
            L = len(arr)
            if L < 2:
                return arr
            else:
                m = L >> 1
                return merge(msort(arr[:m]), msort(arr[m:]))

        def merge(left, right):
            l, r = 0, 0
            while l < len(left) and r < len(right):
                # if (left[l] >> 1) <= right[r]:
                if left[l] <= right[r] * 2:
                    l += 1
                else:
                    self.cnt += len(left) - l
                    r += 1
            return sorted(left + right)

        msort(nums)
        return self.cnt


print(reversePairs2([2, 4, 3, 5, 1]))
sol = Solution()
print(sol.reversePairs([1, 3, 2, 3, 1]))
print(reversePairs([1, 3, 2, 3, 1]))
