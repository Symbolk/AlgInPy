from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:  # if not intervals
            return []

        res = []
        # sort intervals by the left border
        intervals.sort()

        left = intervals[0][0]
        right = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] <= right:
                if intervals[i][1] > right:
                    right = intervals[i][1]
            else:
                res.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
        res.append([left, right])
        return res

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        n = len(intervals)
        i = 0
        while i < n:
            left = intervals[i][0]
            right = intervals[i][1]
            while i < n - 1 and intervals[i + 1][0] <= right:
                i += 1
                right = max(intervals[i][1], right)
            res.append([left, right])
            i += 1
        return res


sol = Solution()
print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(sol.merge2([[1, 3], [2, 6], [8, 10], [15, 18]]))
