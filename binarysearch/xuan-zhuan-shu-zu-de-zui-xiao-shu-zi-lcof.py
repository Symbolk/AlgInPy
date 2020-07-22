class Solution:
    # O(logn), O(1)
    def minArray(self, numbers: List[int]) -> int:
        N = len(numbers)
        if N == 1:
            return numbers[0]
        l, r = 0, N - 1
        m = 0
        while l <= r:
            m = (l + r) // 2
            if numbers[m] < numbers[r]:
                # l | target | m | r
                r = m
            elif numbers[m] > numbers[r]:
                # l | m | target | r
                l = m + 1
            else:
                # duplicates
                r -= 1
        return numbers[m]
        # return min(numbers)

    # even quicker
    def minArray1(self, numbers: List[int]) -> int:
        N = len(numbers)
        if N == 1:
            return numbers[0]
        l, r = 0, N - 1
        while l <= r:
            if numbers[l] < numbers[r] or l == r:
                return numbers[l]
            m = l + ((r - l) >> 1)
            if numbers[l] == numbers[m]:
                l += 1
            elif numbers[l] < numbers[m]:
                l = m + 1
            else:
                r = m