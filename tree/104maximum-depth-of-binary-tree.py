# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # iteration: O(n), O(h)
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        res += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return res

    # BFS/level traversal: O(n), O(n)
    def maxDepth1(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque([root])
        res = 1
        while q:
            num = len(q)
            for i in range(num):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if len(q) != 0:
                res += 1
        return res

    # DFS with stack
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        # (node, level)
        stack = [(root, 1)]
        res = 0
        while stack:
            node, level = stack.pop()
            res = max(res, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return res
