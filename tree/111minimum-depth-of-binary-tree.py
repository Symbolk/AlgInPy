# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # BFS: O(n), O(n)
    def minDepth0(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append((root, 1))
        while q:
            n, d = q.popleft()
            if not n.left and not n.right:
                return d
            if n.left:
                q.append((n.left, d + 1))
            if n.right:
                q.append((n.right, d + 1))

        return res

    # DFS: O(n), O(logn)
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        return min_depth + 1
