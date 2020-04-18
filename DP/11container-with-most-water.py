from typing import List


class Solution:
    # brutal force: O(n^2)
    # WA
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        ans = 0
        for i in range(1, N):
            l, r = 0, N - 1
            lmax, rmax = height[l], height[r]
            li, ri = l, r
            while l < i:
                if height[l] > lmax:
                    lmax = height[l]
                    li = l
                l += 1

            while r > i:
                if height[r] > rmax:
                    rmax = height[r]
                    ri = r
                r -= 1

            res = max((ri - li) * min(lmax, rmax), (i - li) * min(height[i], lmax), (ri - i) * min(height[i], rmax))
            ans = max(res, ans)

        return ans

    # double pointers: O(n)
    # to max ans, first max width, so start from two ends
    def maxArea1(self, height: List[int]) -> int:
        N = len(height)
        i, j = 0, N - 1
        ans = 0
        while i < j:
            # h = min(h[i], h[j]), so to increase h
            # always move the lower column
            if height[i] < height[j]:
                h = height[i]
                i += 1
            else:
                h = height[j]
                j -= 1
            ans = max((j - i + 1) * h, ans)
        return ans


sol = Solution()
print(sol.maxArea1([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea1([2, 3, 4, 5, 18, 17, 6]))
print(sol.maxArea1([9, 6, 14, 11, 2, 2, 4, 9, 3, 8]))
