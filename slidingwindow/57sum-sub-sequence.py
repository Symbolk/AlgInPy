from typing import List


class Solution:
    # sliding window: O(n)
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # [i, j)
        i, j = 1, 1
        sum = 0
        res = []

        while i <= target // 2:
            if sum < target:
                sum += j
                # move right end
                j += 1
            elif sum > target:
                sum -= i
                # move left end
                i += 1
            else:
                res.append(list(range(i, j)))
                # ! continue sliding
                # sum-=i
                # i+=1
                sum -= (2 * i + 1)
                i += 2
        return res

    # double pointers
    def findContinuousSequence1(self, target: int) -> List[List[int]]:
        i, j = 1, 2
        res = []
        while i <= target // 2:  # or j <= target//2 + 1
            # 等差数列和：(start+end)*num/2
            sum = (i + j) * (j - i + 1) // 2
            if sum < target:
                j += 1
            elif sum == target:
                res.append(list(range(i, j + 1)))
                i += 2  # or j+=1
            elif sum > target:
                i += 1
        return res

    # math: enumerate the range size
    def findContinuousSequence2(self, target: int) -> List[List[int]]:
        res = []
        k = 1  # j-i
        while target - k * (k + 1) / 2 > 0:
            if (target - k * (k + 1) / 2) % (k + 1) == 0:  # 整除
                x = int((target - k * (k + 1) / 2) // (k + 1))
                res.append(list(range(x, x + k + 1)))
            k += 1
        return res[::-1]


sol = Solution()
print(sol.findContinuousSequence(15))
