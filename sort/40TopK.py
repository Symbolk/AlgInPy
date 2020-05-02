class Solution:
    # sort: O(nlogn), O(logn)
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

    # heap: O(nlogk) O(k)
    def getLeastNumbers1(self, arr: List[int], k: int) -> List[int]:
        import heapq
        if k == 0:
            return []
        # default: min heap
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            # weed out the big num in heap
            if arr[i] < -hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        return [-x for x in hp]

    # qsort:
    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        def partition(nums, l, r):
            pivot = nums[r]
            i = l - 1
            for j in range(l, r):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[r] = nums[r], nums[i + 1]
            return i + 1

        def randomized_partition(nums, l, r):
            import random
            i = random.randint(l, r)
            nums[r], nums[i] = nums[i], nums[r]
            return partition(nums, l, r)

        def randomized_select(arr, l, r, k):
            pos = randomized_partition(arr, l, r)
            num = pos - l + 1
            if k < num:
                randomized_select(arr, l, pos - 1, k)
            elif k > num:
                randomized_select(arr, pos + 1, r, k - num)

        if k == 0:
            return []
        randomized_select(arr, 0, len(arr) - 1, k)
        return arr[:k]
