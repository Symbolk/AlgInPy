from typing import List


# key: equal distribution according to odd/even depth
# ! note that the given seq is valid !
class Solution:
    # stack: O(n), O(n)
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = []
        res = []
        for c in seq:
            if c == '(':
                stack.append('(')
                res.append(len(stack) % 2)
            elif c == ')':
                res.append(len(stack) % 2)
                stack.pop()
        return res

    # stack: O(n), O(1): no need for actual stack since only keeps '('
    def maxDepthAfterSplit1(self, seq: str) -> List[int]:
        res = []
        d = 0  # depth of the stack
        for c in seq:
            if c == '(':
                d += 1
                res.append(d % 2)
            elif c == ')':
                res.append(d % 2)
                d -= 1
        return res

    # balance simulation: O(n), O(1)
    def maxDepthAfterSplit2(self, seq: str) -> List[int]:
        ans = []
        a = b = 0  # depth
        for s in seq:
            if s == '(':
                if a <= b:
                    a += 1
                    ans.append(0)
                else:
                    b += 1
                    ans.append(1)
            elif s == ')':
                if a > b:
                    a -= 1
                    ans.append(0)
                else:
                    b -= 1
                    ans.append(1)
        return ans

    # if index('(') is odd, the matched ')' index is even
    # note that the input is guaranteed to be valid
    def maxDepthAfterSplit3(self, seq: str) -> List[int]:
        ans = [0] * len(seq)
        for i in range(len(seq)):
            if seq[i] == '(':
                # i & 1 to get the last of the binary, to check odd(0)/even(1)
                ans[i] = (i & 1)
            else:
                ans[i] = ((i + 1) & 1)
        return ans


sol = Solution()
print(sol.maxDepthAfterSplit3('(()())'))
print(sol.maxDepthAfterSplit3('()(())()'))
