from Tree import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []

        def inorder(node):
            if node:
                inorder(node.left)
                vals.append(node.val)
                inorder(node.right)

        def bst(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(vals[m])
            root.left = bst(l, m - 1)
            root.right = bst(m + 1, r)
            return root

        inorder(root)
        return bst(0, len(vals) - 1)


sol = Solution()
arr = [1, None, 2, None, 3, None, 4, None, None]
node_list = build_tree(arr)
bst = sol.balanceBST(node_list[0])
print(bst)
