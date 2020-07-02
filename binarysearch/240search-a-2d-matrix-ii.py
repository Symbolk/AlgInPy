class Solution:
    # search with pruning: O(m+n), O(1)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        N, M = len(matrix), len(matrix[0])

        # start from the left-bottom (or right-up) corner
        x, y = N - 1, 0
        while x >= 0 and y < M:
            if matrix[x][y] > target:
                # move up
                x -= 1
            elif matrix[x][y] < target:
                # move right
                y += 1
            else:
                return True
        return False

    def searchMatrix1(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        N, M = len(matrix), len(matrix[0])
        left_end = [matrix[i][0] for i in range(N)]
        right_end = [matrix[i][-1] for i in range(N)]
        # filtered rows
        rows = []
        for i in range(N):
            if left_end[i] <= target <= right_end[i]:
                rows.append(i)
        for i in rows:
            row = matrix[i]
            l, r = 0, M - 1
            while l <= r:
                m = l + ((r - l) >> 1)
                if row[m] == target:
                    return True
                elif row[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return False
