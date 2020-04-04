from typing import List


class Solution:
    # brutal force: O(n^2), O(1)
    # compute the water for each index and sum
    def trap0(self, height: List[int]) -> int:
        res = 0
        N = len(height)
        for i in range(1, N - 1):
            pl, pr = 0, 0
            # left: [0, i]
            for j in range(i, -1, -1):
                pl = max(pl, height[j])
            # right: [i, N-1]
            for j in range(i, N):
                pr = max(pr, height[j])
            res += (min(pl, pr) - height[i])
        return res

    # dp with memo: cache the max height: O(n), O(n)
    def trap1(self, height: List[int]) -> int:
        if not height:
            return 0
        N = len(height)
        l, r = [0] * (N + 1), [0] * (N + 1)
        res = 0
        # [1, N+1] to avoid i-1<0
        for i in range(1, N + 1):
            l[i] = max(l[i - 1], height[i - 1])
        for i in range(N - 1, 0, -1):
            r[i] = max(r[i + 1], height[i])
        for i in range(N):
            res += max(0, min(l[i + 1], r[i]) - height[i])
        return res

    # dp with memo: cache the max height: O(n), O(n)
    def trap2(self, height: List[int]) -> int:
        if not height:
            return 0
        N = len(height)
        res = 0
        l, r = [0] * N, [0] * N
        l[0], r[N - 1] = height[0], height[N - 1]
        for i in range(1, N):
            l[i] = max(height[i], l[i - 1])
        for j in range(N - 2, -1, -1):
            r[j] = max(height[j], r[j + 1])
        for i in range(N):
            res += max(0, min(l[i], r[i]) - height[i])
        return res

    # double pointers: O(n), O(1)
    def trap3(self, height: List[int]) -> int:
        if not height:
            return 0
        N = len(height)
        res = 0

        l, r = 0, N - 1
        max_l, max_r = height[0], height[N - 1]

        while l < r:
            max_l = max(height[l], max_l)
            max_r = max(height[r], max_r)
            # min of max_l, max_r
            if max_l < max_r:
                res += (max_l - height[l])
                l += 1
            else:
                res += (max_r - height[r])
                r -= 1

        # while l <= r:
        #     if max_l < max_r:
        #         if max_l > height[l]:
        #             res += max_l - height[l]
        #         else:
        #             max_l = height[l]
        #         l += 1
        #     else:
        #         if max_r > height[r]:
        #             res += max_r - height[r]
        #         else:
        #             max_r = height[r]
        #         r -= 1
        return res

    # descending stack: O(n), O(n)
    def trap4(self, height: List[int]) -> int:
        if not height:
            return 0
        N = len(height)
        res, i = 0, 0
        # stack stores the index
        stack = []
        while i < N:
            while stack and height[i] > height[stack[-1]]:  # current > min_height_left
                top = stack.pop()
                if not stack:
                    break
                # min height in the left and right sides
                min_height = min(height[i], height[stack[-1]]) - height[top]
                width = i - stack[-1] - 1
                res += (width * min_height)
            stack.append(i)
            i += 1

        return res

    # dp: O(n), O(1)
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        N = len(height)
        res, peak, peak_i = 0, 0, 0
        for i in range(N):
            if height[i] > peak:
                peak = height[i]
                peak_i = i

        peak_left = height[0]
        for i in range(1, peak_i):
            if height[i] < peak_left:
                res += (peak_left - height[i])
            else:
                peak_left = height[i]
        peak_right = height[N - 1]
        for i in range(N - 2, peak_i, -1):
            if height[i] < peak_right:
                res += (peak_right - height[i])
            else:
                peak_right = height[i]
        return res


sol = Solution()
print(sol.trap4([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
