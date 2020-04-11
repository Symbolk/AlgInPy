from typing import List


class Solution:
    # append and sort: O((m+n)log(m+n)), O(log(m+n))
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        A[m:] = B
        A.sort()

    # get the min head: left to right: O(m+n), O(m+n)
    def merge1(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        C = []
        i = j = 0
        while i < m or j < n:
            # reach the end, just append
            if i == m:
                C.append(B[j])
                j += 1
            elif j == n:
                C.append(A[i])
                i += 1
            # compare and append min
            elif A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        A[:] = C

    # get the max tail: right to left: O(m+n),  O(1)
    # A always has enough spaces in the tail, so the original nums will not be overwritten
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        tail = m + n - 1
        while i >= 0 or j >= 0:
            if i == -1:
                nums1[tail] = nums2[j]
                j -= 1
            elif j == -1:
                nums1[tail] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[tail] = nums1[i]
                i -= 1
            else:
                nums1[tail] = nums2[j]
                j -= 1
            tail -= 1


sol = Solution()
A = [1]
sol.merge(A,
          1,
          [],
          0)
print(A)
