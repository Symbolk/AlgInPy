# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iteration
    def generateTrees(self, n: int) -> List[TreeNode]:
        # [start, end]
        def generate(s, e):
            if s > e:
                return [None]
            res = []
            for i in range(s, e + 1):
                left = generate(s, i - 1)
                right = generate(i + 1, e)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return generate(1, n) if n else []

    # memorized searching
    def generateTrees1(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        memo = {}

        def generate(s, e):
            if s > e:
                return [None]
            if (s, e) in memo:
                return memo[(s, e)]
            res = []
            for i in range(s, e + 1):
                left = generate(s, i - 1)
                right = generate(i + 1, e)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            memo[(s, e)] = res
            return res

        return generate(1, n)
