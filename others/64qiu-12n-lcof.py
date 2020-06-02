class Solution:
    # py tricks
    def sumNums(self, n: int) -> int:
        # return sum(range(1, n+1))
        def add(x, y):
            return x + y

        # return reduce(add, range(1, n + 1))
        return reduce(lambda x, y: x + y, range(1, n + 1))

    # iteration: O(n), O(n)
    def sumNums1(self, n: int) -> int:
        # early stop to control terminator
        # and: early stop when false
        # or: early stop when true
        # python的 and 操作如果最后结果为真，返回最后一个表达式的值;
        # or 操作如果结果为真，返回第一个结果为真的表达式的值
        return n and (n + self.sumNums1(n - 1))


sol = Solution()
print(sol.sumNums1(3))
