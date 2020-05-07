# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # convert and compare: !special symbols are used to represent same val but diff pos
    # to generate unique preorder seq for each tree
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def preorder(root, isleft):
            if not root:
                return 'lnull' if isleft else 'rnull'
            res = ''
            res = res + "#" + str(root.val)
            res = res + "#" + preorder(root.left, True)
            res = res + '#' + preorder(root.right, False)
            return res

        ss = preorder(s, False)
        tt = preorder(t, False)

        return tt in ss

    # compare recursively
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # no tree is subtree of None tree
        if not s:
            return False
        # None tree is subtree of any tree
        if not t:
            return True
        return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, s, t):
        # None tree is the same with None tree
        if not s and not t:
            return True
        # None tree is not the same with non-None tree
        if not s or not t:
            return False
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
