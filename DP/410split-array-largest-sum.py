class Solution:
    # min-max DP: O(n^2*m), O(nm)
    def splitArray(self, nums: List[int], m: int) -> int:
        N = len(nums)
        INT_MAX = 2 ** 31 - 1
        f = [[INT_MAX] * (m + 1) for _ in range(N + 1)]
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        # subproblem f[i][j]: split i nums into j groups
        # k: split k nums in i into j-1 groups, and [k,i] into the last jth group
        f[0][0] = 0
        for i in range(1, N + 1):
            # j is the number of groups
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], presum[i] - presum[k]))

        return f[N][m]

    # binary search: O(nlog(sum−maxn))), O(1)
    # assume and try the answer, which must lie between [max(nums), sum(nums)]
    def splitArray1(self, nums: List[int], m: int) -> int:
        # get the #groups with res <= m, and check if cnt within m
        def check(x):
            total, cnt = 0, 1
            for num in nums:
                # assume x is the final result
                if total + num > x:
                    # use num as the start of another group
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        l, r = max(nums), sum(nums)
        while l < r:
            x = (l + r) // 2
            if check(x):
                # less groups than m: x is large
                r = x
            else:
                # more groups than m: x is small
                l = x + 1
        return l
