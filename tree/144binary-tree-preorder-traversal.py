# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # vars in python: local > global > builtin

    # recursion: O(n), O(n)
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # inner functions can access the global (to inner) vars in the parent function
        def fun(node):
            if not node:
                return
            # if assign (=, +=, -=), then it is local
            # collections and refs, will modify global
            res.append(node.val)
            fun(node.left)
            fun(node.right)

        res = list()
        fun(root)
        return res

    # iteration: O(n), O(n)
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        res = list()
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # FILO, so right first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
