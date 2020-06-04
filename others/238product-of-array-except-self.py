from typing import List


class Solution:
    # O(n), O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        L = [1] * N  # prefix product
        R = [1] * N  # suffix product
        for i in range(1, N):
            L[i] = L[i - 1] * nums[i - 1]
        # for i in range(N - 2, -1, -1):
        for i in reversed(range(N - 1)):  # use reversed to invert list
            R[i] = R[i + 1] * nums[i + 1]
        res = []
        for i in range(N):
            res.append(L[i] * R[i])
        return res

    # O(n), O(1)
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        # prefix products
        for i in range(1, N):
            res[i] = res[i - 1] * nums[i - 1]
        # suffix product
        r = 1
        for i in reversed(range(N - 1)):
            r *= nums[i + 1]
            res[i] *= r
        return res

    # double pointers: O(n), O(1)
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        l, r = 1, 1
        for i in range(N):
            res[i] *= l
            # res[~i] *= r
            res[-1 - i] *= r
            l *= nums[i]
            r *= nums[-1 - i]
        return res


sol = Solution()
print(sol.productExceptSelf2([1, 2, 3, 4]))
print(sol.productExceptSelf1([1, 2, 3, 4]))
