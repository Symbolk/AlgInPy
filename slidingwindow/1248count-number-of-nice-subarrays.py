from typing import List


class Solution:
    # enumerate odd pos: O(n), O(n)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # indices of odd nums
        # !add pivot to handle all odds cases
        odd = [-1]
        for i in range(N):
            if nums[i] % 2 == 1:
                odd.append(i)
        # !add pivot to handle all odds cases
        odd.append(N)

        ans = 0
        for i in range(1, len(odd) - k):
            # num of all [l, r] that includes odd[i], odd[i+k-1], which contains k odds
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans

    # sliding window: O(n), O(1)
    def numberOfSubarrays1(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l, r = 0, 0
        odd_cnt = 0
        res = 0
        while r < N:
            if (nums[r] & 1) == 1:
                odd_cnt += 1
            r += 1

            # enough odd
            if odd_cnt == k:
                t = r
                # move r util next odd or the end
                while r < N and (nums[r] & 1) == 0:
                    r += 1
                right_even_cnt = r - t
                left_even_cnt = 0
                while (nums[l] & 1) == 0:
                    l += 1
                    left_even_cnt += 1
                # include [0, left_even_cnt] in left side or [0, right_even_cnt] in right side
                res += (left_even_cnt + 1) * (right_even_cnt + 1)
                # now the l point to the first odd
                l += 1
                odd_cnt -= 1
        return res

    # pre odd cnt (number of odds util i): O(n), O(n)
    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # key/index: #odd cnt pre
        # value: #
        preCnt = [0] * (N + 1)
        # handle the case when nums are all odds
        preCnt[0] = 1
        res = 0
        sum = 0
        for n in nums:
            # if odd, add 1; if even, add 0
            sum += (n & 1)
            preCnt[sum] += 1
            if sum >= k:
                res += preCnt[sum - k]
        return res


sol = Solution()
print(sol.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(sol.numberOfSubarrays1([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(sol.numberOfSubarrays2([1, 1, 2, 1, 1], 3))
