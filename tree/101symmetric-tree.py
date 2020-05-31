# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursion: O(n), O(n)
    def isSymmetric(self, root: TreeNode) -> bool:
        def fun(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return fun(left.left, right.right) and fun(left.right, right.left)

        if not root:
            return True
        return fun(root.left, root.right)

    # level traversal
    def isSymmetric1(self, root: TreeNode) -> bool:
        if not root:
            return True

        def check(seq):
            mid = (len(seq)) // 2
            for i in range(mid):
                # ~ to visit array from two ends
                if seq[i] != seq[~i]:
                    return False
            return True

        from collections import deque
        q = deque([root])
        while q:
            t = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    t.append(node.val)
                    q.extend([node.left, node.right])
                else:
                    t.append('')
            if not check(t):
                return False
        return True

    # iteration: (use a queue to convert recursion to iteration)
    # BFS: O(n), O(n)
    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:
            return True

        from collections import deque
        q = deque([(root, root)])
        while q:
            left, right = q.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            q.append((left.left, right.right))
            q.append((left.right, right.left))
        return True
