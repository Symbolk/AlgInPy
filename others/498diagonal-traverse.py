from typing import List


class Solution:
    # find patterns: read and flip: O(MN), O(min(M,N)
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        M, N = len(matrix), len(matrix[0])
        res, tmp = [], []

        # total M+N-1 diagonals
        for d in range(M + N - 1):
            tmp.clear()  # cost O(k)
            if d < N:
                # diagonals in the left of the main diagonal
                r = 0
                c = d
            else:
                # diagonals in the right
                r = d - N + 1
                c = N - 1

            while r < M and c > -1:
                tmp.append(matrix[r][c])
                r += 1
                c -= 1
            # reverse the even diagonals
            if d % 2 == 0:
                res.extend(tmp[::-1])
            else:
                res.extend(tmp)
        return res

    # simulate:
    def findDiagonalOrder1(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        M, N = len(matrix), len(matrix[0])
        res = []
        i, j = 0, 0
        # up = 1, down = 0
        direction = 1

        while i < M and j < N:
            res.append(matrix[i][j])
            ni = i + (-1 if direction else 1)
            nj = j + (1 if direction else -1)
            if 0 <= ni < M and 0 <= nj < N:
                # not reach the end, no need to go next diagonal and flip
                i, j = ni, nj
            else:
                # reach the bounds, get the head of next diagonal
                if direction:
                    # upward
                    if j == N - 1:
                        # rightmost: next head at down
                        i += 1
                    else:
                        # next head at right
                        j += 1
                else:
                    # downward
                    if i == M - 1:
                        # bottom: next head at right
                        j += 1
                    else:
                        # next head at down
                        i += 1
                # flip
                direction = 1 - direction
        return res


sol = Solution()
print(sol.findDiagonalOrder([[2, 3]]))
print(sol.findDiagonalOrder1([[2, 3]]))
