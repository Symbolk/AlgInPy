from typing import List


class Solution:
    # temp array: [j,n-i-1] = [i,j]: O(n^2), O(n^2)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        temp = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                temp[j][N - i - 1] = matrix[i][j]

        # slicing assignment
        # cannot be matrix = temp, since ref is copied, the matrix is not changed
        matrix[:] = temp

    # inplace with math: rotation loop: O(n^2), O(1)
    def rotate1(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        # left corner
        for i in range(N // 2):
            for j in range((N + 1) // 2):
                matrix[i][j], matrix[N - j - 1][i], matrix[N - i - 1][N - j - 1], matrix[j][N - i - 1] = \
                    matrix[N - j - 1][i], matrix[N - i - 1][N - j - 1], matrix[j][N - i - 1], matrix[i][j]

    # flip updown and flip main diagonal to rotate: O(n^2), O(1)
    def rotate2(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        # flip updown: [i,j] <-> [n-i-1][j]
        for i in range(N // 2):  # odd or even both ok
            for j in range(N):
                matrix[i][j], matrix[N - i - 1][j] = matrix[N - i - 1][j], matrix[i][j]

        # flip main diagonal: [i,j] <-> [j,i]
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # flip main diagonal and flip leftright to rotate: O(n^2), O(1)
    def rotate3(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        # flip main diagonal
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # flip leftright
        mid = N >> 1
        for i in range(N):
            for j in range(mid):
                matrix[i][j], matrix[i][N - j - 1] = matrix[i][N - j - 1], matrix[i][j]


sol = Solution()
m = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
sol.rotate3(m)
print(m)
