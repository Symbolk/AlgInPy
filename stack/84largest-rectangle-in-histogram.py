class Solution:
    # divide and conquer: TLE in py
    def largestRectangleArea(self, heights: List[int]) -> int:
        def compute(l, r):
            if l > r:
                return 0
            min_index = l
            for i in range(l, r + 1):
                min_index = i if heights[i] < heights[min_index] else min_index
            max_area_left = compute(l, min_index - 1)
            max_area_right = compute(min_index + 1, r)
            max_area_current = heights[min_index] * (r - l + 1)
            return max(max_area_current, max_area_left, max_area_right)

        return compute(0, len(heights) - 1)

    # mono stack (ascending): get the first bigger/smaller element in the left/right side of an element
    # if h > top, push; if h < top, pop util top < h
    # O(n), O(n)
    def largestRectangleArea1(self, heights: List[int]) -> int:
        N = len(heights)
        # save the index
        stack = []
        # guard
        heights = [0] + heights + [0]
        res = 0
        for i in range(N):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                # the current element is the first smaller element in the right of the popped
                # top is the first smaller element in the left
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res
