from typing import List


class Solution:
    # O(nlogC), O(logC) (C is the max range of arr elements, here logC~~20)
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = abs(arr[0] - target)
        valid = {arr[0]}
        for num in arr:
            valid = {x & num for x in valid} | {num}
            ans = min(ans, min(abs(x - target) for x in valid))
        return ans


s = Solution()
print(s.closestToTarget([70, 15, 21, 96], 4))
print(s.closestToTarget([1000000, 1000000, 1000000], target=1))
