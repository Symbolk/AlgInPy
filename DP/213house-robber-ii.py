class Solution:
    # divide the circle to 2 sub problems of array, then dp 2 times
    # O(n), O(n)
    # max of 3 cases: 0 0, 0 1, 1 0
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def dfs(ns):
            if not ns:
                return 0
            if len(ns) == 1:
                return ns[0]
            N = len(ns)
            dp = [0] * (N + 1)
            dp[1] = ns[0]
            for i in range(2, N + 1):
                # rob i-1 or not
                dp[i] = max(dp[i - 1], dp[i - 2] + ns[i - 1])
            return dp[-1]

        # 2 cases:
        # 0 1: nums[1:n]
        # 1 0: nums[0:n-1]
        return max(dfs(nums[1:]), dfs(nums[:-1]))

    # O(n), O(1)
    def rob1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def fun(ns):
            cur, pre = 0, 0
            for n in ns:
                cur, pre = max(pre + n, cur), cur
            return cur

        return max(fun(nums[1:]), fun(nums[:-1]))
