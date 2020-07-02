class Solution:
    # O(log(mn)), O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        N, M = len(matrix), len(matrix[0])
        l, r = 0, M * N - 1

        while l < r:
            m = l + ((r - l) >> 1)
            i, j = divmod(m, M)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = m
            else:
                l = m + 1
        if matrix[l // M][l % M] == target:
            return True
        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        N, M = len(matrix), len(matrix[0])
        l, r = 0, M * N - 1

        while l <= r:
            m = l + ((r - l) >> 1)
            i, j = divmod(m, M)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = m - 1
            else:
                l = m + 1
        return False
