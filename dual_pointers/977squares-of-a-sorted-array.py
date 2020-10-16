from typing import List


class Solution:
    # O(nlogn), O(logn) (stack space)
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x ** 2, A)))

    def sortedSquares1(self, A: List[int]) -> List[int]:
        return sorted(a * a for a in A)

    # double pointers: O(n), O(1)
    def sortedSquares2(self, A: List[int]) -> List[int]:
        res = []
        i, j = 0, len(A) - 1
        while i <= j:
            # -4 3
            if abs(A[i]) > abs(A[j]):
                res.append(A[i] ** 2)
                i += 1
            else:
                res.append(A[j] ** 2)
                j -= 1

        return res[::-1]

    def sortedSquares3(self, A: List[int]) -> List[int]:
        N = len(A)
        res = [0] * N  # pretty sure
        i, j, p = 0, N - 1, N - 1
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                res[p] = A[i] ** 2
                i += 1
            else:
                res[p] = A[j] ** 2
                j -= 1
            p -= 1
        return res


s = Solution()
print(s.sortedSquares2([-4, -1, 0, 3, 10]))
print(s.sortedSquares2([-7, -3, 2, 3, 11]))
