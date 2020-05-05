# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # inorder seq is increasing
    # O(n), O(n)
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            seq = []
            if root:
                seq.extend(inorder(root.left))
                seq.append(root.val)
                seq.extend(inorder(root.right))
            return seq

        seq = inorder(root)
        for i in range(1, len(seq)):
            if seq[i] <= seq[i - 1]:
                return False
        return True

    # early return: O(n), O(n)
    def isValidBST1(self, root: TreeNode) -> bool:
        # only keep the last value
        inorder = float('-inf')
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # if the next value is smaller than the last one
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

    # iteration: O(n), O(n) (stack space in wrost case), n is the number of tree nodes
    def isValidBST2(self, root: TreeNode) -> bool:
        def fun(node, lower, upper):
            if not node:
                # empty tree is a BST
                return True
            return lower < node.val < upper and fun(node.left, lower, node.val) and fun(node.right, node.val, upper)

        return fun(root, float('-inf'), float('inf'))

    # only keep the previous value
    def __init__(self):
        self.pre = float('-inf')

    def isValidBST3(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isValidBST3(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST3(root.right)
