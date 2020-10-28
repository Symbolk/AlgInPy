from collections import Counter


class Solution:
    # O(n), O(n)
    # 48%
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        nums = set()
        times = set()
        for k, v in cnt.items():
            nums.add(k)
            times.add(v)

        return len(times) == len(nums)

    # quicker with pruning
    # 100%
    def uniqueOccurrences1(self, arr: List[int]) -> bool:
        dic = dict()
        for a in arr:
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1

        times = set()
        for n in dic.values():
            if n in times:
                return False
            else:
                times.add(n)

        return True
