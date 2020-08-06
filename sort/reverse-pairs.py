from typing import List


class Solution:
    # mergesort with trick: O(nlogn), O(1)
    def reversePairs(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
        mid = N >> 1
        left = nums[:mid]
        right = nums[mid:]
        res = self.reversePairs(left) + self.reversePairs(right)

        left.sort()
        right.sort()
        i = 0
        for j in range(len(right)):
            while i < len(left) and left[i] <= right[j]:
                i += 1
            res += (len(left) - i)
        return res

    # divide and conquer: more regular mergesort: O(nlogn), O(n)
    def reversePairs1(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0

        def merge_count(nums, l, m, r, temp):
            # copy arr to temp arr
            for i in range(l, r + 1):
                temp[i] = nums[i]
            i, j = l, m + 1
            cnt = 0
            for k in range(l, r + 1):
                if i > m:
                    # left is all merged
                    nums[k] = temp[j]
                    j += 1
                elif j > r:
                    # right is all merged
                    nums[k] = temp[i]
                    i += 1
                elif temp[i] <= temp[j]:
                    nums[k] = temp[i]
                    i += 1
                else:
                    assert temp[i] > temp[j]
                    nums[k] = temp[j]
                    j += 1
                    cnt += (m - i + 1)
            return cnt

        def count(nums, l, r, temp):
            if l == r:
                return 0
            mid = l + ((r - l) >> 1)
            left_count = count(nums, l, mid, temp)
            right_count = count(nums, mid + 1, r, temp)

            # all reverse pairs = left count + right count + cross-side count
            cnt = left_count + right_count
            if nums[mid] <= nums[mid + 1]:
                # all nums in the left are no bigger than all nums in the right, so all sorted, no need to merge_count
                return cnt
            # compute cross-side count in merging left and right
            cross_count = merge_count(nums, l, mid, r, temp)
            return cnt + cross_count

        # ! use temp to avoid creating arr in iteration and handle index offset
        temp = [0] * N
        return count(nums, 0, N - 1, temp)

    # RMQ (Range Minimum/Maximum Query)
    # BIT (binary indexed tree/Fenwick Tree): O(nlogn), O(n)
    # Fenwick Tree was proposed to solve the prefix sum problem of a dynamic array in O(logn)
    def reversePairs2(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0

        class FenWickTree:
            def __init__(self, n):
                self.size = n
                # ! store the tree in an array, compute next index in the update/query path with lowbit
                # tree height = log(n)
                self.tree = [0 for _ in range(n + 1)]  # index start from 1

            def __lowbit(self, index):
                return index & (-index)

            # O(logn)
            def update(self, index, delta):
                while index <= self.size:
                    self.tree[index] += delta
                    index += self.__lowbit(index)

            # O(logn)
            def query(self, index):
                res = 0
                while index > 0:
                    res += self.tree[index]
                    index -= self.__lowbit(index)
                return res

        s = list(set(nums))
        import heapq
        # min heap
        heapq.heapify(s)
        rank_map = dict()
        rank = 1
        # number of non-duplicate nums
        rank_map_size = len(s)
        for _ in range(rank_map_size):
            # get the min
            num = heapq.heappop(s)
            rank_map[num] = rank
            rank += 1

        res = 0
        ft = FenWickTree(rank_map_size)
        # from back to front: get one and query forwards #nums smaller than it
        for i in range(N - 1, -1, -1):
            rank = rank_map[nums[i]]
            ft.update(rank, 1)
            res += ft.query(rank - 1)
        return res


sol = Solution()
print(sol.reversePairs([7, 5, 6, 4]))
print(sol.reversePairs1([7, 5, 6, 4]))
print(sol.reversePairs2([7, 5, 6, 4]))
