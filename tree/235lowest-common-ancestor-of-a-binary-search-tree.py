# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursion: O(n), O(n)
    # BST: all nodes in the left child < root, all nodes in the right child > root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        if root.val > p.val and root.val > q.val:
            # p and q in left child
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            # p and q in right child
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    # iteration: O(n), O(1)
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node
