# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # in-place: not necessary O(1) space
    # preorder: O(n), O(n)
    def flatten0(self, root: TreeNode) -> None:
        if not root:
            return
        stack = [root]
        # the last node
        pre = None

        while stack:
            cur = stack.pop()
            if pre:
                pre.left = None
                pre.right = cur
            # FILO
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            # move the last node
            pre = cur

    # find pre node: O(n), O(1)
    def flatten1(self, root: TreeNode) -> None:
        while root:  # is not None
            if root.left:
                # find the right-most node of the left subtree
                pre = root.left
                while pre.right:
                    pre = pre.right
                # as the pre of the right subtree
                pre.right = root.right
                # insert left tree to right of the root
                root.right = root.left
                root.left = None
                # consider next node
            root = root.right

    # recursion: O(n), O(n) (stack)
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            pre = root.left
            while pre.right:
                pre = pre.right
            pre.right = root.right
            root.right = root.left
            root.left = None
