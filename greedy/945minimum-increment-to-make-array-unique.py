from typing import List


class Solution:
    # sort first, O(nlogn)
    def minIncrementForUnique(self, A: List[int]) -> int:
        # ascending, expect A[i-1] <= A[i]
        A.sort()
        count = 0
        for i in range(1, len(A)):
            if A[i - 1] >= A[i]:
                count += (A[i - 1] - A[i] + 1)
                A[i] = A[i - 1] + 1
        return count

    # consider the problem as a hash addressing problem
    def minIncrementForUnique1(self, A: List[int]) -> int:
        pos = [-1 for _ in range(len(A) + 40000)]

        def findPos(i):
            if pos[i] == -1:
                pos[i] = i
                return i
            else:
                j = findPos(pos[i] + 1)
                pos[i] = j
                return j

        res = 0
        for a in A:
            p = findPos(a)
            res += p - a
        return res

    # count O(n+k)
    def minIncrementForUnique2(self, A: List[int]) -> int:
        N = len(A)
        if N < 2:
            return 0
        counter = [0] * (N + 40000)
        for a in A:
            counter[a] += 1

        res = 0
        for i in range(len(counter)):
            if counter[i] > 1:
                res += counter[i] - 1
                counter[i + 1] += counter[i] - 1
        return res


sol = Solution()
print(sol.minIncrementForUnique([3, 2, 1, 2, 1, 7]))
print(sol.minIncrementForUnique1([3, 2, 1, 2, 1, 7]))
print(sol.minIncrementForUnique2([3, 2, 1, 2, 1, 7]))
