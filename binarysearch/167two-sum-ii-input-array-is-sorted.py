class Solution:
    # double pointers: O(n), O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        l, r = 0, N - 1
        while l < r:
            t = numbers[l] + numbers[r]
            if t == target:
                return [l + 1, r + 1]
            elif t > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]

    # binary search: O(nlogn), O(1)
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        for i in range(N):
            l, r = i + 1, N - 1
            while l <= r:
                m = (l + r) // 2
                t = target - numbers[i]
                if numbers[m] == t:
                    return [i + 1, m + 1]
                elif numbers[m] > t:
                    r = m - 1
                else:
                    l = m + 1
        return [-1, -1]
