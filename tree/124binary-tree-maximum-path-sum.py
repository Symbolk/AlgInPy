# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursion: O(n), O(h)
    # global max
    ans = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        # return the max path sum for sub-tree with node as root
        def func(node):
            # terminator
            if not node:
                return 0
            # the max sub-path sum in sub-trees
            l = max(func(node.left), 0)
            r = max(func(node.right), 0)
            # 2 cases:
            # 1 (lmr): the max path contains the current node and left&right child
            lmr = node.val + l + r
            # 2 (return): the max path contains the current node and left/right child
            ret = node.val + max(l, r, 0)
            # update global max
            self.ans = max(self.ans, lmr, ret)
            return ret

        func(root)
        return self.ans
